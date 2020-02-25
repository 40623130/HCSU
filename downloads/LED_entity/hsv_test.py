import cv2
import numpy as np
import array

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
        range = 5
        lower_color = np.array([120-range,200,120])
        upper_color = np.array([120+range,255,160])
        mask = cv2.inRange(hsv, lower_color, upper_color)
        # Display the resulting frame
        cv2.imshow('frame',mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()