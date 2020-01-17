import sim
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
 
#errorCode,Revolute_joint_handle=sim.simxGetObjectHandle(clientID,'Prismatic_joint',sim.simx_opmode_oneshot_wait)
errorCode,player_x_handle=sim.simxGetObjectHandle(clientID,'player_x_joint',sim.simx_opmode_oneshot_wait)
errorCode,player_y_handle=sim.simxGetObjectHandle(clientID,'player_y_joint',sim.simx_opmode_oneshot_wait)
 
if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
    

#errorCode=sim.simxSetJointTargetVelocity(clientID,Revolute_joint_handle,2, sim.simx_opmode_oneshot_wait)
        
def setJointPositiony(poi, steps):
    for i  in range(steps):
        errorCode=sim.simxSetJointPosition(clientID, player_y_handle, 0.162-i*poi, sim.simx_opmode_oneshot_wait)
        
def setJointPositionx(poi, steps):
    for i  in range(steps):
        errorCode=sim.simxSetJointPosition(clientID, player_x_handle, 0.115-i*poi, sim.simx_opmode_oneshot_wait)
        
        
# 每步 移動0.005m, 移45次
setJointPositionx(0.005, 45)
# 每步 移動0.005m, 移60次
setJointPositiony(0.005, 60)
# 每步 移動0.005m, 移80次
        