import numpy as np
import array
import cv2
import time
import ColorRecognition as color
import serial
import sys
'''
gamemode
1 = setting
2 = play
'''
gamemode = 1
COM_PORT = 'COM5'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
blue_x = None
blue_y = None
cap = cv2.VideoCapture(0)
if __name__ == '__main__':
    while(True):
        # Capture frame-by-frame
        ret, frame= cap.read()
        #image_byte_array = array.array('b', frame)
        #image_buffer = I.frombuffer("RGB", (resolution[0],resolution[1]), bytes(image_byte_array), "raw", "RGB", 0, 1)
        #img2 = numpy.asarray(image_buffer)
        #ColorRecognition
        ret_green = color.track_green_object(frame)
        ret_blue = color.track_blue_object(frame)
        if ret_blue:
            cv2.rectangle(frame,(ret_blue[0] - 10,ret_blue[1]-10), (ret_blue[0] + 10,ret_blue[1] + 10), (0,255,0), 2)
            blue_x = ret_blue[0]
            blue_y = ret_blue[1]
            ser.write(b'BLUE_ON\n')
            #print('blue =>(', blue_x, ',', blue_y, ')')
        else:
            print('unfind blue')
            ser.write(b'BLUE_OFF\n')
        if ret_green:
            cv2.rectangle( frame, (ret_green[0]-10, ret_green[1]-10), (ret_green[0]+10,ret_green[1]+10), (0,0,255), 2)
            green_x = ret_green[0]
            green_y = ret_green[1]
            ser.write(b'GREEN_ON\n')
            print('green =>(', green_x, ',', green_y, ')')
        else:
            print('unfind green')
            ser.write(b'GREEN_OFF\n')
        while ser.in_waiting:
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            print('Arduino feedback :', mcu_feedback)
        if gamemode ==1:
            print('blue =>(', blue_x, ',', blue_y, ')')
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()