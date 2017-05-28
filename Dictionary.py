# Dictionary with serial objects}

import serial

Port1 = serial.Serial(None, timeout = 0.3)
Port2 = serial.Serial(None)
Port3 = serial.Serial(None)
Port4 = serial.Serial(None)


PORTS = ['ttyUSB0','ttyUSB1','ttyUSB2','ttyUSB3','ttyUSB4']

SerialPorts = {}

for port in PORTS:
    SerialPorts[port] = None

print SerialPorts

SerialPorts['ttyUSB0'] = Port1


print SerialPorts['ttyUSB0'].seekable()

print SerialPorts['ttyUSB0'].get_settings()
