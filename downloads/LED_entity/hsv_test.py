import cv2
import numpy as np
import array
kernel = np.ones((5,5),np.uint8)
cap = cv2.VideoCapture(0)
'''
range = 5
lower_blue = np.array([120-range,200,120])
upper_blue = np.array([120+range,255,160])

range = 10
lower_green = np.array([60-range,100,100])
upper_green = np.array([60+range,255,255])
'''

if __name__ == '__main__':
    while(True):
        ret, frame= cap.read()
        # Our operations on the frame come here
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        range = 10
        lower_color = np.array([0-range,100,100])
        upper_color = np.array([0+range,255,255])
        mask = cv2.inRange(hsv, lower_color, upper_color)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # Display the resulting frame
        #cv2.imshow('frame',opening)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()