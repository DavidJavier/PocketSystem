# -*- coding: utf-8 -*-
from control.RecordController import RecordController
from model.RecordFactory import RecordFactory
from view.SensorView import SensorView
from view.RecordView import RecordView
from control.Umbral import Umbral
from view.UdpServerView import UdpView
from view.SensorSerialView import SensorSerialView

class main():

    def callback(self, data):
        print data
        if data == "stop":
            self.cont = False

    def __init__(self):
        udpView = UdpView()
        recordFactory = RecordFactory()
        recordView = RecordView(udpView)
        # sensorView = SensorView()
        sensorView = SensorSerialView()
        recordFactory.createRecord()
        record = recordFactory.getRecord(0)
        record.startStopRecord(True)

        recordController = RecordController(recordFactory, sensorView)
        recordController.setFilter(Umbral(100))
        recordController.setView(recordView)

        # server.start()
        self.cont = True
        while self.cont:
            recordController.record()
        recordController.stopRecord()

main()
