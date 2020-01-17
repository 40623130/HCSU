import sim
import keyboard
from time import sleep
import sys, math
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
 
sim.simxFinish(-1)
 
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

errorCode,Ball_handle=sim.simxGetObjectHandle(clientID,'Ball',sim.simx_opmode_oneshot_wait)
errorCode,player_x_handle=sim.simxGetObjectHandle(clientID,'player_x_joint',sim.simx_opmode_oneshot_wait)
errorCode,player_y_handle=sim.simxGetObjectHandle(clientID,'player_y_joint',sim.simx_opmode_oneshot_wait)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()

def stop():
    errorCode = sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot_wait)
    
def start():
    errorCode = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot_wait)
    
def pause():
    errorCode = sim.simxPauseSimulation(clientID,sim.simx_opmode_oneshot_wait)


def keyboard_control():
    while True:
        try:
            if keyboard.is_pressed('a'):
                sim.simxSetJointTargetVelocity(clientID, player_x_handle, 2, sim.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('d'):
                sim.simxSetJointTargetVelocity(clientID, player_x_handle, -2, sim.simx_opmode_oneshot_wait)
            else:
                sim.simxSetJointTargetVelocity(clientID, player_x_handle, 0, sim.simx_opmode_oneshot_wait)
            if keyboard.is_pressed('w'):
                sim.simxSetJointTargetVelocity(clientID, player_y_handle, -2, sim.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('s'):
                sim.simxSetJointTargetVelocity(clientID, player_y_handle, 2, sim.simx_opmode_oneshot_wait)
            else:
                sim.simxSetJointTargetVelocity(clientID, player_y_handle, 0, sim.simx_opmode_oneshot_wait)
        except:
            break 
    
sim.simxSetJointTargetVelocity(clientID,player_x_handle,0,sim.simx_opmode_oneshot_wait)
sim.simxSetJointTargetVelocity(clientID,player_y_handle,0,sim.simx_opmode_oneshot_wait)

start()
keyboard_control()
stop()




