# -*- coding: utf-8 -*-
from Record import Record


class RecordFactory():

    def __init__(self):
        self.records = []

    def createRecord(self):
        self.records.append(Record())

    def getRecord(self, index):
        return self.records[index]

    def getAllRecords(self):
        return self.records