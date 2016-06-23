# -*- coding: utf-8 -*-
import os
import commands


class SensorView():

    def __init__(self):
        self.gpios = (11, 12, 15, 16, 19, 21, 22, 37, 38, 40)
        for i in range(0, len(self.gpios)):
            os.system('echo ' + self.gpios[i] + ' > /sys/class/gpio/export')
            os.system('echo in > /sys/class/gpio/' + self.gpios[i] + '/direction')
            #gpio.setup(self.gpios[i], gpio.IN)
            #print self.gpios[i]

    def getValue(self):
        value = 0
        for i in range(0, len(self.gpios)):
            valueGpio = commands.getoutput('cat /sys/class/gpio/' + self.gpios[i] + '/value')
            value = value + int(valueGpio) * (2 ** i)
        return value