import sim
import time
from PIL import Image as I
import array
import cv2, numpy

"""
0 = Auto Defense (done)
1 = Auto Attack + Defense (undone)
2 = Player + player (Application) (undone)
"""

play_mode = 0

def speed(handle,speed):
    sim.simxSetJointTargetVelocity(clientID,handle,speed,sim.simx_opmode_oneshot_wait)
    
def track_green_object(image):
    # Blur the image to reduce noise100
    blur = cv2.GaussianBlur(image, (5,5),0)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image for only green colors
    range = 15
    lower_green = numpy.array([60-range,100,100])
    upper_green = numpy.array([60+range,255,255])
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (5,5),0)
    # Take the moments to get the centroid
    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    # Assume no centroid
    ctr = None
    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr

def track_blue_object(image):
    # Blur the image to reduce noise100
    blur = cv2.GaussianBlur(image, (5,5),0)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image for only green colors
    range = 15
    lower_red = numpy.array([0-range,100,100])
    upper_red = numpy.array([0+range,255,255])
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (5,5),0)
    # Take the moments to get the centroid
    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    # Assume no centroid
    ctr = None
    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr
    
def track_red_object(image):
    # Blur the image to reduce noise100
    blur = cv2.GaussianBlur(image, (5,5),0)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image for only green colors
    range = 15
    lower_blue = numpy.array([120-range,100,100])
    upper_blue = numpy.array([120+range,255,255])
    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (5,5),0)
    # Take the moments to get the centroid
    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    # Assume no centroid
    ctr = None
    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr

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
            ret_green = track_green_object(img2)
            ret_red = track_red_object(img2)
            ret_blue = track_blue_object(img2)
            # Find Green And Red Object
            if ret_green and ret_red and ret_blue:
                cv2.rectangle( img2, (ret_green[0]-3, ret_green[1]-3), (ret_green[0]+3,ret_green[1]+3), (0x99,0xff,0x33), 1)
                cv2.rectangle( img2, (ret_red[0]-3, ret_red[1]-3), (ret_red[0]+3,ret_red[1]+3), (0xff,0x33,0x33), 1)
                cv2.rectangle( img2, (ret_blue[0]-3, ret_blue[1]-3), (ret_blue[0]+3,ret_blue[1]+3), (0xff,0x33,0x33), 1)
                #print('G_X = ', ret_green[0],'G_Y = ', ret_green[1])
                #print('R_X = ', ret_red[0],'R_Y = ', ret_red[1])
                
                # Rx_v  > 0 => the green is at the right of the Red
                Rx = ret_green[0] - ret_red[0]
                #print(Rx)
                # Rx_v  > 0 => the green is at the front of the Red
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
else:
  print("Failed to connect to remote API Server")
  sim.simxFinish(clientID)