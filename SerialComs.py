# Line Counter Interface

import time
import serial


# Enter location name ----------------
#name = raw_input("Name: ")
#print(name)


# Open the serial port with the line counter ----------------------------------------
lineCounter = serial.Serial("/dev/ttyUSB0",baudrate = 115200, timeout = 3.0)
print("Line Counter Port: " + lineCounter.name)


# Set Line Counter distance ----------------------------------------------------

if raw_input("Set Line counter? y/n") == "y":

    done = 'n'
    
    while done == 'n':  # Repeat until set point is correct

        lineCounter.write('s')          # enter set mode

        while not lineCounter.inWaiting():  pass                             # wait for line counter
        while lineCounter.inWaiting():      print(lineCounter.readline())    # line counter responce [ count, feet, meters ]
                
        units = raw_input("Enter Units: ")  # enter responce
        lineCounter.write(units)            # send responce to the line counter

        while not lineCounter.inWaiting():  pass                            # wait for line counter
        while lineCounter.inWaiting():      print(lineCounter.readline())   # line counter responce

        number = str(raw_input()) 

        for index in number:    # Send number to line counter one charature at a time and waite for it to echo back
            lineCounter.write(index)  
            while not lineCounter.inWaiting():  pass                            # wait for line counter
            while lineCounter.inWaiting():      print(lineCounter.readline())   # line counter echos charature
                

        lineCounter.write("\r")  # send carage return to line counter to indicat the end of the number
        
        while not lineCounter.inWaiting():  pass                            # wait for line counter
        while lineCounter.inWaiting():      print(lineCounter.readline())   # line counter responce
            

        done = str(raw_input("Done? (y/n) "))
        lineCounter.write(done)
        # End Line counter set loop --------------------------------------------------------------------

    while not lineCounter.inWaiting():  pass                            # wait for line counter
    while lineCounter.inWaiting():      print(lineCounter.readline())   # line counter responce
         
# Read Line counter --------------------------------------------------
print("Main loop")
distance = ""

while True:

    
    if lineCounter.inWaiting():
        distance = lineCounter.readline()
        print("\n\nDistance: " + distance)
        #print(time.localtime())
    

    
