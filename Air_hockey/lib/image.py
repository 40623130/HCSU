import sim
import time
from PIL import Image as I
import array
import cv2, numpy


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

if clientID!=-1:
    print('Connected to remote API server')
  # get vision sensor objects
    res, v0 = sim.simxGetObjectHandle(clientID, 'vs1', sim.simx_opmode_oneshot_wait)
    res, v1 = sim.simxGetObjectHandle(clientID, 'vs2', sim.simx_opmode_oneshot_wait)
    err, resolution, image = sim.simxGetVisionSensorImage(clientID, v0, 0, sim.simx_opmode_streaming)
    err,Ball_handle=sim.simxGetObjectHandle(clientID,'Ball',sim.simx_opmode_oneshot_wait)
    err,player_x_handle=sim.simxGetObjectHandle(clientID,'player_x_joint',sim.simx_opmode_oneshot_wait)
    err,player_y_handle=sim.simxGetObjectHandle(clientID,'player_y_joint',sim.simx_opmode_oneshot_wait)
    time.sleep(1)
    while (sim.simxGetConnectionId(clientID) != -1):
        print('1')
        err, resolution, image = sim.simxGetVisionSensorImage(clientID, v0, 0, sim.simx_opmode_buffer)
        if err == sim.simx_return_ok:
            print('2')
            image_byte_array = array.array('b', image)
            image_buffer = I.frombuffer("RGB", (resolution[0],resolution[1]), bytes(image_byte_array), "raw", "RGB", 0, 1)
            img2 = numpy.asarray(image_buffer)
            ret_green = track_green_object(img2)
            ret_red = track_red_object(img2)
            ret_blue = track_blue_object(img2)
            if ret_green:
                print('3')
                cv2.rectangle(img2,(ret_green[0]-10,ret_green[1]-10), (ret_green[0]+10,ret_green[1]+10), (0x99,0xff,0x33), 1)
            if ret_red:
                print('4')
                cv2.rectangle(img2,(ret_red[0]-10,ret_red[1]-10), (ret_red[0]+10,ret_red[1]+10), (0xff,0x33,0x33), 1)
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