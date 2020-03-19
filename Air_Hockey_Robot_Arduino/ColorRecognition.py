from PIL import Image as I
import array
import cv2, numpy
kernel = numpy.ones((5,5),numpy.uint8)
def track_blue_object(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    range = 10
    lower_blue = numpy.array([120-range,100,100])
    upper_blue = numpy.array([120+range,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
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
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
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
    range = 10
    lower_red = numpy.array([0-range,100,100])
    upper_red = numpy.array([0+range,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
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