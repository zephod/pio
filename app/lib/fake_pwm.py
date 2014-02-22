class PWM:
    def __init__(self,address,debug):
        self.address = address
        self.debug = debug
    def setPWMFreq(self,x):
        print "Set PWM freq to %d" % x
    def setPWM(self,id,on,off):
        print "Set channel=%d on=%d off=%d" % (id,on,off)

