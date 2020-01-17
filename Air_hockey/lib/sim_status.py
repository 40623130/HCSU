import sim
def status_clientID(connectionAddress, connectionPort, waitUntilConnected, doNotReconnectOnceDisconnected, timeOutInMs, commThreadCycleInMs):
    clientID = sim.simxStart(connectionAddress, connectionPort, waitUntilConnected, doNotReconnectOnceDisconnected, timeOutInMs, commThreadCycleInMs)

# clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
def stop():
    errorCode = sim.simxStopSimulation(clientID,sim.simx_opmode_oneshot_wait)

def start():
    errorCode = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot_wait)

def pause():
    errorCode = sim.simxPauseSimulation(clientID,sim.simx_opmode_oneshot_wait)