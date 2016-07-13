# -*- coding: utf-8 -*-
from control.RecordController import RecordController
from model.RecordFactory import RecordFactory
from view.SensorView import SensorView
from view.UdpServerView import UdpServerView


class main():

    def callback(self, data):
        print data
        if data == "stop":
            self.cont = False

    def __init__(self):
        recordFactory = RecordFactory()
        sensorView = SensorView()
        recordFactory.createRecord()
        record = recordFactory.getRecord(0)
        record.startStopRecord(True)
        # server = UdpServerView(self.callback)

        recordController = RecordController(recordFactory, sensorView)
        # server.start()
        self.cont = True
        while self.cont:
            recordController.record()
        recordController.stopRecord()

main()