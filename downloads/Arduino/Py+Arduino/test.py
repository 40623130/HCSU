import serial
import sys
import time

A = 2
Encode_A = str(A).encode()

ard = serial.Serial('COM4',115200,timeout=5)
time.sleep(3)
ard.flush()

ard.write(b'Right\n')
while True:
    print ("Python value sent: ")
    #print("Right",Encode_A)

    ard.write(Encode_A)
    #ard.write(Encode_A)
    time.sleep(0.55)

    B = ard.read(ard.inWaiting())
    print (" ")
    print ("Message from arduino: ")
    print (B)
    ard.flushInput()