from PIL import Image as I
import array
import cv2, numpy

def track_blue_object(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    range = 5
    lower_blue = numpy.array([120-range,200,120])
    upper_blue = numpy.array([120+range,255,160])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    moments = cv2.moments(mask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    ctr = None
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr

def track_green_object(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    range = 5
    lower_green = numpy.array([0-range,150,150])
    upper_green = numpy.array([0+range,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    moments = cv2.moments(mask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    ctr = None
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr
    
def track_red_object(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    range = 5
    lower_red = numpy.array([0-range,160,160])
    upper_red = numpy.array([0+range,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    moments = cv2.moments(mask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)
    ctr = None
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr