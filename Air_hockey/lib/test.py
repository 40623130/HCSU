import sim
import sim_status as status
import sys, math

sim.simxFinish(-1)
status.status_clientID('127.0.0.1', 19997, True, True, 5000, 5)
# clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')


status.start()