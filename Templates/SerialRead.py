import time
import serial
import glob

print(serial.VERSION)


ports = glob.glob('/dev/tty.usbserial*')
print(ports)

port = str(ports)

serialPort1 = serial.Serial('/dev/tty.usbserial',baudrate = 4800, timeout = 0.3)

while True:
    
    if serialPort1.in_waiting:
        while serialPort1.in_waiting:
            data = serialPort1.readline()
        
        print(time.strftime('%I:%M:%S') +" ~ " + data)
