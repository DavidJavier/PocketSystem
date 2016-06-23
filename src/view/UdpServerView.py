# -*- coding: utf-8 -*-
import socket
import threading


class UdpServerView():

    def __init__(self, callback):
        UDP_IP = "192.168.1.52"
        UDP_PORT = 5005
        self.callback = callback
        self.sock = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))
        self.thread = threading.Thread(target=self.worker)
        self.thread.start()

    def worker(self):
        work = True
        while work:
            data, addr = self.sock.recvfrom(1024)
            self.callback(data)
            if data == "stop":
                work = False

    def start(self):
        pass