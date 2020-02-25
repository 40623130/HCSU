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
gamemode = 2
arduino_connect = 1

if arduino_connect == 1:
    COM_PORT = 'COM5'  # 請自行修改序列埠名稱
    BAUD_RATES = 9600
    ser = serial.Serial(COM_PORT, BAUD_RATES)
    
max_x = None
min_x = None
max_y = None
min_y = None

blue_x = None
blue_y = None
cap = cv2.VideoCapture(0)
if __name__ == '__main__':
    while(True):
        # Capture frame-by-frame
        ret, frame= cap.read()
        #ColorRecognition
        ret_red = color.track_red_object(frame)
        ret_blue = color.track_blue_object(frame)
        #set the position of blue and red
        if ret_blue:
            cv2.rectangle(frame,(ret_blue[0] - 10,ret_blue[1]-10), (ret_blue[0] + 10,ret_blue[1] + 10), (0,255,0), 2)
            blue_y = ret_blue[0]
            blue_x = ret_blue[1]
        else:
            print('unfind blue')
        if ret_red:
            cv2.rectangle( frame, (ret_red[0]-10, ret_red[1]-10), (ret_red[0]+10,ret_red[1]+10), (0,0,255), 2)
            red_y = ret_red[0]
            red_x = ret_red[1]
        else:
            print('unfind red')
            
        #check find the red and blue or not
        if ret_red and ret_blue:
            if arduino_connect == 1:
                ser.write(b'CHECK_ON\n')
                print('red =>(', red_x, ',', red_y, ')')
        else:
            if arduino_connect == 1:
                ser.write(b'CHECK_ON\n')
        #arduino feedback
        if arduino_connect == 1:
            while ser.in_waiting:
                mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                print('Arduino feedback :', mcu_feedback)
                
        #gamemode setting
        # used to setting
        if gamemode ==1:
            #print('blue =>(', blue_x, ',', blue_y, ')')
            print("please move the player to left and down")
            print("and enter the 'd'")
            while(True):
                ret, frame= cap.read()
                ret_red = color.track_red_object(frame)
                cv2.imshow('frame',frame)
                if ret_red:
                    cv2.rectangle( frame, (ret_red[0]-10, ret_red[1]-10), (ret_red[0]+10,ret_red[1]+10), (0,0,255), 2)
                    cv2.imshow('frame',frame)
                    red_y = ret_red[0]
                    red_x = ret_red[1]
                    max_x = red_x
                    max_y = red_y
                    print('red =>(', red_x, ',', red_y, ')')
                    print('max x =' , max_x)
                    print('max y =' , max_y)
                if cv2.waitKey(1) == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    break
        # used to playing
        elif gamemode == 2:
            if ret_red and ret_blue:
                if blue_x < red_x:
                    if arduino_connect == 1:
                        ser.write(b'RIGHT_ON\n')
                        ser.write(b'LEFT_OFF\n')
                elif blue_x > red_x:
                    if arduino_connect == 1:
                        ser.write(b'LEFT_ON\n')
                        ser.write(b'RIGHT_OFF\n')
                else:
                    if arduino_connect == 1:
                        ser.write(b'RIGHT_OFF\n')
                        ser.write(b'LEFT_OFF\n')
        #display the video
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()