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
Path_Prediction = 0
if arduino_connect == 1:
    COM_PORT = 'COM8'  # 請自行修改序列埠名稱
    BAUD_RATES = 115200
    ser = serial.Serial(COM_PORT, BAUD_RATES)
    
max_x = None
min_x = None
max_y = None
min_y = None

blue_x = None
blue_y = None
cap = cv2.VideoCapture(0)

L = 1000 #Max_X_Distance of Ball & Computer
M_status = 0
Ddist = L ; Cdist = 0.6*L ; Bdist = 0.2*L ; Adist = 0.02*L  #Every leval of distance
Dsp = 200 ; Csp = 135 ; Bsp = 255 ; Asp = 355
Subtraction_x = blue_x - red_x
abs_x = abs(Subtraction_x)
#Mode_1  f(L) = 355, f(0.2L) = 135, f(0.02L) = 200
a = ((Adist-Ddist)*(Csp-Asp)-(Bdist-Ddist)*(Dsp-Asp))/(((Adist-Ddist)*(Bdist-Ddist)*Bdist)-((Bdist-Ddist)*(Adist-Ddist)*Adist))
b = ((Adist-Ddist)*Adist*(Csp-Asp)-(Bdist-Ddist)*Bdist*(Dsp-Asp))/((Adist-Bdist)*(Bdist-Ddist)*(Adist-Ddist))
A = (a*abs_x+b)*(abs_x-Ddist)+Asp
Encode_A = str(A).encode()
#Mode_2  f(0.6L) = 355, f(0.2L) = 135, f(0.02L) = 255
c = ((Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp))/(((Adist-Cdist)*(Bdist-Cdist)*Bdist)-((Bdist-Cdist)*(Adist-Cdist)*Adist))
d = ((Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp))/((Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist))
B = (c*abs_x+d)*(abs_x-Cdist)+Asp
Encode_B = str(B).encode()
#Mode_3  f(0.2L) = 355 , f(0.02L) = 255
C = ((Asp-Bsp)/(Bdist-Adist))*abs_x + (Bsp-Adist*((Asp-Bsp)/(Bdist-Adist)))
Encode_C = str(C).encode()
S = 0 #No speed to move
Encode_S = str(S).encode()

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
                
        #if OPEN Path Prediction
        if Path_Prediction ==1:
            pass
            
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
                if arduino_connect == 1:
                    if M_status == 0 :
                        if Ddist > abs_x  & Cdist <=abs_x :
                            M_status = 1
                        elif Cdist > abs_x  & Bdist <=abs_x :
                            M_status = 2
                        elif Bdist > abs_x  & Adist <=abs_x :
                            M_status = 3
                        else :
                            M_status = 0
                        
                    if blue_x < red_x:  #Right
                        #Mode_1  Range : L~0.6L
                        ard.write(b'RIGHT\n')
                        ard.write(b'RIGHT\n')
                        time.sleep(0.55)
                        if M_status == 1:
                            print("Right",A)
                            ard.write(Encode_A)
                            time.sleep(0.55)
                            if abs_x >= Adist: 
                                M_status = 0
                        #Mode_2  Range : 0.6~0.2L
                        elif M_status == 2:
                            print("Right",B)
                            ard.write(Encode_B)
                            time.sleep(0.55)
                            if abs_x >= Adist: 
                                M_status = 0
                        #Mode_3  Range : 0.2~0.02L
                        elif M_status == 3:
                            print("Right",C)
                            ard.write(Encode_C)
                            time.sleep(0.55)
                            if abs_x >= Adist: 
                                M_status = 0
                        elif abs_x >= Adist: 
                            print("Aim",S)
                            ard.write(Encode_S)
                            time.sleep(0.55)
                            M_status = 0
                        else :
                            M_status = 0
                            
                    elif blue_x > red_x:  #Left
                        #Mode_1  Range : L~0.6L
                        ard.write(b'Left\n')
                        ard.write(b'Left\n')
                        time.sleep(0.55)
                        if M_status == 1:
                            print("Left",A)
                            ard.write(Encode_A)
                            time.sleep(0.55)
                            if abs_x >= Adist: 
                                M_status = 0
                        #Mode_2  Range : 0.6~0.2L
                        elif M_status == 2:
                            print("Left",B)
                            ard.write(Encode_B)
                            time.sleep(0.55)
                            if abs_x >= Adist: 
                                M_status = 0
                        #Mode_3  Range : 0.2~0.02L
                        elif M_status == 3:
                            print("Left",C)
                            ard.write(Encode_C)
                            time.sleep(0.55)
                            if abs_x >= Adist: 
                                M_status = 0
                        elif abs_x >= Adist: 
                            print("Aim",S)
                            ard.write(Encode_S)
                            time.sleep(0.55)
                            M_status = 0
                        else :
                            M_status = 0
                            
    '''F = ard.read(ard.inWaiting()) #Use to repaire
    print (" ")
    print ("Message from arduino: ")
    print (F)'''
    ard.flushInput()
        #display the video
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()