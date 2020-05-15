import serial
import sys
import time

ard = serial.Serial('COM7',115200,timeout=5)
time.sleep(1) # wait for Arduino

#setTempCar1 = 8
#setTempCar2 = 7
setTempCar3 =str(8) + str(7)
ard.flush()
#setTemp1 = str(setTempCar1).encode()
#setTemp2 = str(setTempCar2).encode()
setTempCar3 = setTempCar3.encode()
#B = setTemp1 + setTemp2
B = setTempCar3
print ("Python value sent: ")
print (setTemp1,setTemp2)
ard.write(B)
time.sleep(0.55) # I shortened this to match the new value in your Arduino code

# Serial read section
A = ard.read(ard.inWaiting()) # read all characters in buffer
print ("Message from arduino: ")#inWaiting()
print (A)
ard.flushInput()