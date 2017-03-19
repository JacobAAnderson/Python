# Line Counter Interface

import time
import serial


#print(time.localtime())

# Open the serial port with the line counter ----------------------------------------
dataPort = serial.Serial("/dev/ttyUSB0",baudrate = 19200)
print("Data Port: " + dataPort.name)


# Read Line counter --------------------------------------------------
print("Main loop")
data = ""

state = ''
location = ''
data = ''

while True:

    if dataPort.inWaiting():
        dataRecived = dataPort.readline()

        #print("\nIn Coming Data: " + str(data))
        #print(data[0:5])
        

        #ident = bytearray()
        
        #for i in data:
        #    print(data(i))
        #    if data(i) == bytes(','.encode('utf-8')):
        #        break
        #    else:
        #        pass #ident.extend(data[i])

        
        #print(str(idnet))
        
        if dataRecived[0:5] == bytes('$CARE'.encode('utf-8')):
            state = str(dataRecived[7:len(dataRecived)-2])
            print('State: ' + str(dataRecived[7:len(dataRecived)-2]))
            print(state)
            
        elif dataRecived[0:5] == bytes('$GPRM'.encode('utf-8')):
            location = str(dataRecived[7:len(dataRecived)-2])
            print('Location: ' + str(dataRecived[7:len(dataRecived)-2]))
            print(location)
        else:
            print("More Data: ")
        
    

    
