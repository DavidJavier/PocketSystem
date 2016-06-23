# -*- coding: utf-8 -*-
import time


class RecordController():

    def __init__(self, recordFactory, sensorView, externalAppView):
        self.recordFactory = recordFactory
        self.records = []
        self.frecuency = 10
        self.a = 0
        self.sensorView = sensorView
        self.externalAppView = externalAppView

    def stopRecord(self):
        print self.records

    def record(self):
        if self.recordFactory.getRecord(0).isRecording():
            self.b = time.time()
            if ((self.b - self.a) > 1 / self.frecuency):
                self.recordFactory.getRecord(0).addValue(self.sensorView.getValue())
                #self.records.append(self.sensorView.getValue())
                self.externalAppView.sendMessage(self.recordFactory.getRecord(0).getValues())
                self.a = time.time()
