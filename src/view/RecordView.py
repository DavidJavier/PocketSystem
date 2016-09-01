import socket


class RecordView():

    def __init__(self, udp):
        self.udp = udp
        self.isShowing = False
        self.udp.setCallback(self)

    def setShowing(self, isShowing):
        self.isShowing = isShowing

    def show(self, index, x):
        if self.isShowing:
            self.udp.send(x)
