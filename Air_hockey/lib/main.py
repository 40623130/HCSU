import sim
import time,array
import cv2, numpy
from PIL import Image as I
import ColorRecognition as color

"""
0 = Auto Defense (done)
1 = Auto Attack + Defense (undone)
2 = Player + Player (Application) (undone)
3 = Auto Defense (Path Prediction) (undone)
"""
play_mode = 3

#How much Ball_Position data save (min = 5)
data_number = 10
if data_number < 5:
    data_number = 5
    
ball_positionX = []
ball_positionY = []

wall_X_min = 10
wall_X_max = 248
wall_Y_min = 41
wall_Y_max = 450
# 0 = Stop
# 1 = Up or Right
# 2 = Down or Left
Ball_DirectionX_Movement = 0
Ball_DirectionY_Movement = 0
def speed(handle,speed):
    sim.simxSetJointTargetVelocity(clientID,handle,speed,sim.simx_opmode_oneshot_wait)

if __name__ == '__main__':
    sim.simxFinish(-1)
    clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
        # get vision sensor objects
        res, v0 = sim.simxGetObjectHandle(clientID, 'vs1', sim.simx_opmode_oneshot_wait)
        res, v1 = sim.simxGetObjectHandle(clientID, 'vs2', sim.simx_opmode_oneshot_wait)
        err, resolution, image = sim.simxGetVisionSensorImage(clientID, v0, 0, sim.simx_opmode_streaming)
        
        #get motor objects
        err,Ball_handle=sim.simxGetObjectHandle(clientID,'Ball', sim.simx_opmode_oneshot_wait)
        err,player_x_handle=sim.simxGetObjectHandle(clientID, 'player_x_joint', sim.simx_opmode_oneshot_wait)
        err,player_y_handle=sim.simxGetObjectHandle(clientID, 'player_y_joint', sim.simx_opmode_oneshot_wait)
        #main loop
        while (sim.simxGetConnectionId(clientID) != -1):
            #get vision sensor image
            err, resolution, image = sim.simxGetVisionSensorImage(clientID, v0, 0, sim.simx_opmode_buffer)
            if err == sim.simx_return_ok:
                image_byte_array = array.array('b', image)
                image_buffer = I.frombuffer("RGB", (resolution[0],resolution[1]), bytes(image_byte_array), "raw", "RGB", 0, 1)
                img2 = numpy.asarray(image_buffer)
                #cv2.line( img2, (10,41), (10 , 450), (0xff,0xff,0x99), 2)
                #cv2.line( img2, (248,41), (248 , 450), (0xff,0xff,0x99), 2)
                #cv2.line( img2, (10,41), (248 , 41), (0xff,0xff,0x99), 2)
                #cv2.line( img2, (10,450), (248 , 450), (0xff,0xff,0x99), 2)
                #ColorRecognition
                ret_green = color.track_green_object(img2)
                ret_red = color.track_red_object(img2)
                ret_blue = color.track_blue_object(img2)
                # If Find Green,Blue,Red Object
                if ret_green and ret_red and ret_blue:
                    #Use Rectangle Mark Green,Blue,Red Object
                    cv2.rectangle( img2, (ret_green[0]-10, ret_green[1]-10), (ret_green[0]+10,ret_green[1]+10), (0x99,0xff,0x33), 2)
                    cv2.rectangle( img2, (ret_red[0]-10, ret_red[1] - 10), (ret_red[0]+10,ret_red[1]+10), (0xff,0x33,0x33), 2)
                    cv2.rectangle( img2, (ret_blue[0]-10, ret_blue[1] - 10), (ret_blue[0]+10,ret_blue[1]+10), (0xff,0x33,0x33), 2)
                    #Save the Ball Position
                    ball_positionX.append( ret_green[0])
                    ball_positionY.append( ret_green[1])
                    #If getting enough data
                    # Rx_v  > 0 => the green is at the right of the Red
                    Rx = ret_green[0] - ret_red[0]
                    # Ry_v  > 0 => the green is at the front of the Red
                    Ry = ret_green[1] - ret_red[1]
                    
                    # Auto Defense mode
                    if play_mode == 0:
                        if Rx > 0:
                            Rx_v = Rx**2
                        else:
                            Rx_v = -(Rx**2)
                        if Ry > 0:
                            Ry_v = Ry**2
                        else:
                            Ry_v = -(Ry**2)
                        if ret_red[0] <  ret_green[0]:
                            speed(player_x_handle,-Rx_v*0.1)
                        elif ret_red[0] >  ret_green[0]:
                            speed(player_x_handle,-Rx_v*0.1)
                        else:
                            speed(player_x_handle,0)
                            
                    #Auto Attack + Defense
                    elif play_mode == 1:
                        print('undone')
                    #Player + Player (Application)
                    elif play_mode == 2:
                        print('undone')
                    #Auto Defense (Path Prediction)
                    elif play_mode == 3:
                        #Use to Path Prediction
                        if len(ball_positionX) and len(ball_positionY) == data_number:
                            x1 = ball_positionX[0]
                            y1 = ball_positionY[0]
                            x2 = ball_positionX[data_number-1]
                            y2 = ball_positionY[data_number-1]
                            ball_directionX= ball_positionX[data_number-1] - ball_positionX[data_number-4]
                            ball_directionY= ball_positionY[data_number-1] - ball_positionY[data_number-4]
                            
                            if ball_directionX < 0:
                                Ball_DirectionX_Movement = 1
                            elif ball_directionX > 0:
                                Ball_DirectionX_Movement = 2
                            else:
                                Ball_DirectionX_Movement = 0
                            if ball_directionY < 0:
                                Ball_DirectionY_Movement = 1
                            elif ball_directionY > 0:
                                Ball_DirectionY_Movement = 2
                            else:
                                Ball_DirectionY_Movement = 0
                                
                            if x1 == x2 and y1 == y2:
                                print('ball is not move')
                            else:
                                #Vertical
                                if x1 == x2: 
                                    x = numpy.arange(x2-10,x2+10)
                                    y = y1
                                #Horizontal
                                elif y1 == y2: 
                                    x = x1
                                    y = numpy.arange(y2-10,y2+10)
                                else:
                                    m = (y2-y1)/(x2-x1)
                                    if Ball_DirectionY_Movement == 1:
                                        y = y1-125
                                        if y < 40:
                                            y = 40
                                            x = (y - y2)/m + x2
                                            cv2.line( img2, (x2,y2), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                            m = -m
                                            y2 = y
                                            x2 = x
                                            y = y2 +60
                                            x = (y - y2)/m + x2
                                            cv2.line( img2, (int(x2),int(y2)), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                        else:
                                            x = (y - y2)/m + x2
                                            cv2.line( img2, (x2,y2), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                            
                                    if Ball_DirectionY_Movement == 2:
                                        y = y1 + 125
                                        if y > 450 :
                                            y = 450
                                            x = (y - y2)/m + x2
                                            cv2.line( img2, (x2,y2), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                            m = -m
                                            y2 = y
                                            x2 = x
                                            y = y2 -60
                                            x = (y - y2)/m + x2
                                            cv2.line( img2, (int(x2),int(y2)), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                        else:
                                            x = (y - y2)/m + x2
                                            cv2.line( img2, (x2,y2), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                        
                                    '''
                                    y = y1+125
                                    x = (y - y2)/m + x2
                                    cv2.line( img2, (x2,y2), (int(x) , int(y)), (0x99,0xff,0x33), 2)
                                    '''
                        else:
                            pass
                        #play_mode  3 end
                    #Use to Test
                    else:
                        speed(player_x_handle,0)
                        speed(player_y_handle,0)
                        pass
                else:
                    if not ret_green:
                        print('Not Found Green Object')
                    if not ret_red:
                        print('Not Found Red Object')
                    if not ret_blue:
                        print('Not Found Blue Object')
                
                # vs2 display
                img2 = img2.ravel()
                sim.simxSetVisionSensorImage(clientID, v1, img2, 0, sim.simx_opmode_oneshot)
                
            elif err == sim.simx_return_novalue_flag:
                print("no image yet")
                pass
            else:
                print(err)
            if len(ball_positionX) > (data_number - 1):
                del ball_positionX[0]
            if len(ball_positionY) > (data_number - 1):
                del ball_positionY[0]
    else:
      print("Failed to connect to remote API Server")
      sim.simxFinish(clientID)