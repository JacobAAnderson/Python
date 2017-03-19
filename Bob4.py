# Bob4 Interface

import serial
import time

lineCounter = serial.Serial("/dev/ttyUSB0",baudrate = 115200, timeout = 3.0)
dataPort = serial.Serial("/dev/ttyUSB1",baudrate = 19200)
bob4 = serial.Serial('/dev/ttyUSB2', rtscts=True)

ESC = bytearray.fromhex("1b")
CSI = bytearray.fromhex("1b 5b")

CLEAR = CSI+bytes('2J'.encode('utf-8'))
FONT = CSI + bytes('4z'.encode('utf-8'))
ROW1 = CSI+bytes('0;0H'.encode('utf-8'))
ROW2 = CSI+bytes('1;0H'.encode('utf-8'))
ROW3 = CSI+bytes('2;0H'.encode('utf-8'))

bob4.write(CLEAR)
bob4.write(FONT)



state = 'No Data'
location = 'No Data'
distance = 'No Data'

dataRecived = ''
distanceRecived = ''

newInfo = False

while 1:

    

    # Read nema data from ROV ------------------------------------------------
    if dataPort.inWaiting():

        newInfo=True
        
        dataRecived = dataPort.readline()
        
        if dataRecived[0:5] == bytes('$CARE'.encode('utf-8')):
            stateIn = str(dataRecived[7:len(dataRecived)-2])
            state = stateIn[2:len(stateIn)-1]
            print('State: ' + state)
            
        
        elif dataRecived[0:5] == bytes('$GPRM'.encode('utf-8')):
            locationIn = str(dataRecived[7:len(dataRecived)-2])
            location = locationIn[2:len(locationIn)-1]
            print('Location: ' + location)
            
           
        else:
            print("More Data: ")

        

    # Read Line counter data -----------------------------------------------------
    if lineCounter.inWaiting():

        newInfo = True
        
        distanceRecived = lineCounter.readline()
        distanceIn = str(distanceRecived[0:len(distanceRecived)-2])
        distance = distanceIn[2:len(distanceIn)-1]
        print('Distance: ' + distance)

    if newInfo == True:
        bob4.write(CLEAR)
        bob4.write(ROW1)
        bob4.write(bytes(state.encode('utf-8')))
        bob4.write(ROW2)
        bob4.write(bytes(location.encode('utf-8')))
        bob4.write(ROW3)
        bob4.write(bytes(distance.encode('utf-8')))
        newInfo = False

 
