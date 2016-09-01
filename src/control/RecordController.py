# -*- coding: utf-8 -*-
import time
import Filter

class RecordController():

    def __init__(self, recordFactory, sensorView):
        self.recordFactory = recordFactory
        self.records = []
        self.frecuency = 10
        self.a = 0
        self.sensorView = sensorView
        self.filter = Filter.filter()
        # self.externalAppView = externalAppView

    def stopRecord(self):
        print self.records

    def setFilter(self, filter):
        self.filter = filter

    def setView(self, view):
        self.recordView = view

    def record(self):
        if self.recordFactory.getRecord(0).isRecording():
            self.b = time.time()
            if ((self.b - self.a) > 1 / self.frecuency):
                self.sensorView.getGpio()
                value = self.sensorView.getValue()
                valueFiltred = self.filter.filterSignal(value)
                self.recordFactory.getRecord(0).addValue(valueFiltred)
                self.recordView.show(0, valueFiltred)
                # print valueFiltred
                #self.records.append(self.sensorView.getValue())
                # self.externalAppView.sendMessage(self.recordFactory.getRecord(0).getValues())
                self.a = time.time()
