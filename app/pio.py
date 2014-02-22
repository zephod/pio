

channels = [0 for i in range(16)]

def setChannel(id,val):
    channels[id] = val

def getState():
    return {'channels':channels}

