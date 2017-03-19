# Serial data intake

import time
import serial



# Open the serial port for nema sentances ----------------------------------------
dataPort = serial.Serial("/dev/ttyUSB1",baudrate = 19200)

# Open the serial port with the line counter ----------------------------------------
lineCounter = serial.Serial("/dev/ttyUSB0",baudrate = 115200, timeout = 3.0)


state = ''
location = ''
data = ''
distance = ''

print("Main loop")

while True:

    # Read nema data from ROV ------------------------------------------------
    if dataPort.inWaiting():
        dataRecived = dataPort.readline()
    elif lineCounter.inWaiting():
        dataRecived = lineCounter.readline()
        
        if dataRecived[0:5] == bytes('$CARE'.encode('utf-8')):
            state = str(dataRecived[7:len(dataRecived)-2])
            print('State: ' + str(dataRecived[7:len(dataRecived)-2]))
            
        
        elif dataRecived[0:5] == bytes('$GPRM'.encode('utf-8')):
            location = str(dataRecived[7:len(dataRecived)-2])
            print('Location: ' + str(dataRecived[7:len(dataRecived)-2]))
            
           
        else:
            print("More Data: ")

        

    # Read Line counter data -----------------------------------------------------
    if 
        
        distanceRecived = lineCounter.readline()
        print('Distance: ' + str(distanceRecived[0:len(distanceRecived)-2]))



            
