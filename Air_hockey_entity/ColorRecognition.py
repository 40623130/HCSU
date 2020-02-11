from PIL import Image as I
import array
import cv2, numpy
    
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
    blur = cv2.GaussianBlur(image, (9,9),0)
    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image for only blue colors
    ran = 15
    lower_blue = numpy.array([120-ran,100,100])
    upper_blue = numpy.array([120+ran,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (9,9),0)
    canny_output = cv2.Canny(bmask, 50, 150 ,2)
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Get the moments
    mu = [None]*len(contours)
    for i in range(len(contours)):
        mu[i] = cv2.moments(contours[i])
    # Get the mass centers
    mc = [None]*len(contours)
    for i in range(len(contours)):
        # add 1e-5 to avoid division by zero
        mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
    return mc
'''
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
'''
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