import serial

class SensorSerialView():

    def __init__(self):
        print 'try to connect'
        self.sensor = serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)
        print("connected to: " + self.sensor.portstr)

    def getValue(self):
        # return self.sensor.read(10)
        value = self.sensor.readline()
        self.sensor.reset_input_buffer()
        return value