import serial
import sys
import time

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

ard = serial.Serial('COM7',115200,timeout=5)
time.sleep(1) # wait for Arduino

if M_status == 0:  #Determent speed's status of distance
    if abs_x <= Ddist & abs_x > Cdist:
        M_status = 1
    elif abs_x <= Cdist & abs_x > Bdist:
        M_status = 2
    elif abs_x <=Bdist & abs_x > Adist:
        M_status = 3
    else :
        M_status = 0

elif gamemode == 2:
    if ret_red and ret_blue:
        if arduino_connect == 1:
            
            if blue_x < red_x:  #Right
                #Mode_1  Range : L~0.6L
                ard.write(b'RIGHT\n')
                ard.write(b'RIGHT\n')
                time.sleep(0.55)
                if M_status == 1:
                    print("Right",A)
                    ard.write(Encode_A)
                    time.sleep(0.55)
                #Mode_2  Range : 0.6~0.2L
                elif M_status == 2:
                    print("Right",B)
                    ard.write(Encode_B)
                    time.sleep(0.55)
                #Mode_3  Range : 0.2~0.02L
                elif M_status == 3:
                    print("Right",C)
                    ard.write(Encode_C)
                    time.sleep(0.55)
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
                #Mode_2  Range : 0.6~0.2L
                elif M_status == 2:
                    print("Left",B)
                    ard.write(Encode_B)
                    time.sleep(0.55)
                #Mode_3  Range : 0.2~0.02L
                elif M_status == 3:
                    print("Left",C)
                    ard.write(Encode_C)
                    time.sleep(0.55)
                elif abs_x >= Adist: 
                    print("Aim",S)
                    ard.write(Encode_S)
                    time.sleep(0.55)
                    M_status = 0
                else :
                    M_status = 0
                    
    F = ard.read(ard.inWaiting())
    print (" ")
    print ("Message from arduino: ")
    print (F)
    ard.flushInput()