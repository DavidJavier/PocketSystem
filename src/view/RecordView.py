import socket


class RecordView():

    def __init__(self, udp):
        self.udp = udp
        self.isShowing = False
        self.udp.setCallBack(self)
        self.i = 0

    def setShowing(self, isShowing):
        self.isShowing = isShowing

    def show(self, index, x):
        if self.i == 0:
            self.sum = 1
        if self.i == 10:
            self.sum = -1
        self.i += self.sum
        if self.isShowing:
            self.udp.send(self.i)
        else:
            print "no"
