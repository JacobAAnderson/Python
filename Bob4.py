# Bob4 Interface

import serial
import time

bob4 = serial.Serial('/dev/ttyUSB2', rtscts=True)
print("Bob4: "+bob4.name)

ESC = bytearray.fromhex("1b")
CLI = bytearray.fromhex("1b 5b")
CLEAR = CLI+bytes('2J'.encode('utf-8'))
bob4.write(CLEAR)


while 1:

    data = str(input()) + '\r\n'
    bob4.write(bytes(data.encode('utf-8')))

 
