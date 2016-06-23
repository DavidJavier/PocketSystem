# -*- coding: utf-8 -*-
import socket


class UdpClientView():

    def __init__(self):
        self.UDP_IP = "192.168.1.43"
        self.UDP_PORT = 5005
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def sendMessage(self, message):
        self.sock.sendto(message, (self.UDP_IP, self.UDP_PORT))