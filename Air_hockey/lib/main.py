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
play_mode = 4
data_number = 10
def speed(handle,speed):
    sim.simxSetJointTargetVelocity(clientID,handle,speed,sim.simx_opmode_oneshot_wait)

if __name__ == '__main__':
    ball_positionX = []
    ball_positionY = []
    sim.simxFinish(-1)
    clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
    if clientID != -1:
        print('Connected to remote API server')
      # get vision sensor objects
        res, v0 = sim.simxGetObjectHandle(clientID, 'vs1', sim.simx_opmode_oneshot_wait)
        res, v1 = sim.simxGetObjectHandle(clientID, 'vs2', sim.simx_opmode_oneshot_wait)
        err, resolution, image = sim.simxGetVisionSensorImage(clientID, v0, 0, sim.simx_opmode_streaming)
        err,Ball_handle=sim.simxGetObjectHandle(clientID,'Ball', sim.simx_opmode_oneshot_wait)
        err,player_x_handle=sim.simxGetObjectHandle(clientID, 'player_x_joint', sim.simx_opmode_oneshot_wait)
        err,player_y_handle=sim.simxGetObjectHandle(clientID, 'player_y_joint', sim.simx_opmode_oneshot_wait)
        time.sleep(1)
        while (sim.simxGetConnectionId(clientID) != -1):
            #print('1')
            err, resolution, image = sim.simxGetVisionSensorImage(clientID, v0, 0, sim.simx_opmode_buffer)
            if err == sim.simx_return_ok:
                #print('2')
                image_byte_array = array.array('b', image)
                image_buffer = I.frombuffer("RGB", (resolution[0],resolution[1]), bytes(image_byte_array), "raw", "RGB", 0, 1)
                img2 = numpy.asarray(image_buffer)
                ret_green = color.track_green_object(img2)
                ret_red = color.track_red_object(img2)
                ret_blue = color.track_blue_object(img2)
                # Find Green And Red Object
                if ret_green and ret_red and ret_blue:
                    cv2.rectangle( img2, (ret_green[0]-3, ret_green[1]-3), (ret_green[0]+3,ret_green[1]+3), (0x99,0xff,0x33), 1)
                    cv2.rectangle( img2, (ret_red[0]-3, ret_red[1]-3), (ret_red[0]+3,ret_red[1]+3), (0xff,0x33,0x33), 1)
                    cv2.rectangle( img2, (ret_blue[0]-3, ret_blue[1]-3), (ret_blue[0]+3,ret_blue[1]+3), (0xff,0x33,0x33), 1)
                    #print('G_X = ', ret_green[0],'G_Y = ', ret_green[1])
                    #print('R_X = ', ret_red[0],'R_Y = ', ret_red[1])
                    ball_positionX.append( ret_green[0])
                    ball_positionY.append( ret_green[1])
                    #print(ball_positionX)
                    #print(ball_positionY)
                    if len(ball_positionX) and len(ball_positionY) == data_number:
                        x1 = ball_positionX[0]
                        y1 = ball_positionY[0]
                        x2 = ball_positionX[4]
                        y2 = ball_positionY[4]
                        if x1 == x2 and y1 == y2:
                            print('ball is not move')
                        else:
                            if x1 == x2: #Vertical
                                x = numpy.arange(x2-10,x2+10)
                                y = y1
                            elif y1 == y2: #Horizontal
                                x = x1
                                y = numpy.arange(y2-10,y2+10)
                            else:
                                m = (y2-y1)/(x2-x1)
                                y = y1 - 250
                                x = (y - y2)/m + x2
                                cv2.line( img2, (x2,y2), (int(x) , int(y)), (0x99,0xff,0x33), 1)
                    # Rx_v  > 0 => the green is at the right of the Red
                    Rx = ret_green[0] - ret_red[0]
                    #print(Rx)
                    # Ry_v  > 0 => the green is at the front of the Red
                    Ry = ret_green[1] - ret_red[1]
                    #print(Ry)
                    
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
                    elif play_mode == 1:
                        print('undone')
                    elif play_mode == 2:
                        print('undone')
                    elif play_mode == 3:
                        print('undone')
                    else:
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