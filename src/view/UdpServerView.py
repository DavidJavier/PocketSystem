# -*- coding: utf-8 -*-
import socket
import threading
from src.view.RecordView import RecordView


class UdpView():

    def __init__(self):
        self.client = socket.socket()
        self.host = "192.168.1.40"
        self.port = 12345
        self.lost = False
        # UDP_IP = "192.168.1.52"
        # UDP_PORT = 5005
        # self.callback = callback
        # self.sock = socket.socket(socket.AF_INET,
        #                      socket.SOCK_DGRAM)
        self.connect()
        self.sock.bind((self.host, self.port))
        # self.thread = threading.Thread(target=self.worker)
        # self.thread.start()

    def connect(self):
        try:
            self.client
            self.client.connect((self.host, self.port))
        except:
            print 'No connection'
            self.client.close()
            self.lost = True

    def setCallBack(self, view):
        if view.__class__ == RecordView:
            self.recordViewCallback = view.setShowing

    def send(self, message):
        try:
            if not self.lost:
                self.connect()
                self.client.send(str(message))
            else:
                self.connect()
        except:
            self.client.close()
            self.lost = True
            print 'Lost connection'

    def listener(self):
        work = True
        while work:
            data, addr = self.sock.recvfrom(1024)
            # self.callback(data)
            if data[1] == "RecordView":
                self.recordViewCallback(data[2] == "True")

    def start(self):
        pass