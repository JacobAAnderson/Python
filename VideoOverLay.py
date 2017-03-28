#!/usr/bin/env python3
# Video Overlay Code
# Sea View
# March 16th 2017

import time
import serial
import glob

from tkinter import *
from tkinter import ttk




# Define functions =====================================================================================================================
#=======================================================================================================================================
#=======================================================================================================================================
    
# Assigne serial Ports ---------------------------------------------------------------------------------------------------------
# Select serial pors for Line counter, ROV and Sonar
def LineCounterComPort(*args):
    
    lineCounter.port = lcPort.get()
    lineCounter.open()
    
    if lineCounter.isOpen():
        print("Line Counter Serail Port: " + lcPort.get())
    else:
        print("Line Counter Serial Port Did Not Open")
    
def ROVComPort(*args):

    rovData.port = rovPort.get()
    rovData.open()
    
    if rovData.isOpen():
        print("ROV Serail Port: " + rovPort.get())
    else:
        print("ROV Serial Port Did Not Open")
    

def SonarComPort(*args):
    
    sonarData.port = sonarPort.get()
    sonarData.open()
    
    if sonarData.isOpen():
        print("Sonar Serail Port: " + sonarPort.get())
    else:
        print("Sonar Serial Port Did Not Open")



def Cam1SerialPort(*args):
    
    bob1.port = comPort1.get()
    bob1.open()
    
    if bob1.isOpen():
        print("Cam1, " +cam1.get()+" Serail Port: " + comPort1.get())
        bob1.write(CLEAR+FONT+ROW1)
        #bob1.write(CLEARline)
        bob1.write(bytes(("Cam1 on " +comPort1.get()).encode('utf-8')))
        
    else:
        print("Cam1," +cam1.get()+ " Serial Port Did Not Open")

    bob1.close()

def Cam2SerialPort(*args):
    
    bob2.port = comPort2.get()
    bob2.open()
    
    if bob2.isOpen():
        print("Cam2, " +cam2.get()+" Serail Port: " + comPort2.get())
        bob2.write(CLEAR+FONT+ROW1)
        #bob2.write(CLEARline)
        bob2.write(bytes(("Cam2 on " +comPort2.get()).encode('utf-8')))
        
    else:
        print("Cam2," +cam2.get()+ " Serial Port Did Not Open")

    bob2.close()

def Cam3SerialPort(*args):
    
    bob3.port = comPort3.get()
    bob3.open()
    
    if bob3.isOpen():
        print("Cam3, " +cam3.get()+" Serail Port: " + comPort3.get())
        bob3.write(CLEAR+FONT+ROW1)
        #bob3.write(CLEARline)
        bob3.write(bytes(("Cam3 on " +comPort3.get()).encode('utf-8')))
        
    else:
        print("Cam3," +cam3.get()+ " Serial Port Did Not Open")

    bob3.close()

def Cam4SerialPort(*args):
    
    bob4.port = comPort4.get()
    bob4.open()
    
    if bob4.isOpen():
        print("Cam4, " +cam4.get()+" Serail Port: " + comPort4.get())
        bob4.write(CLEAR+FONT+ROW1 + bytes(("Cam4 on " +comPort4.get()).encode('utf-8')))
        
    else:
        print("Cam4," +cam4.get()+ " Serial Port Did Not Open")

    bob4.close()

# Name Cameras and their serial ports ------------------------------------------------------------------------------------------

def Name(*args):
    Bobs(ROW1,bytes((cam1.get()+':  '+name.get()).encode('utf-8')))
    print("Project Name: " + name.get())

    
def NameCam1(*args):
    try:
        bob1.open()    
        bob1.write(CLEAR+FONT+ROW1+CLEARline +bytes((cam1.get()+':  '+name.get()).encode('utf-8')))
        bob1.close()
        print("cam1: " + cam1.get())
    except:
        print("cam1: " + cam1.get() + "Serial Port not Open")
    
def NameCam2(*args):
    try:
        bob2.open()
        bob2.write(CLEAR+FONT+ROW1+CLEARline+bytes((cam2.get()+':  '+name.get()).encode('utf-8')))  
        bob2.close()
        print("cam2: " + cam2.get())
    except:
        print("cam2: " + cam2.get() + "Serial Port not Open")

def NameCam3(*args):
    try:
        bob3.open()
        bob3.write(CLEAR+FONT+ROW1+CLEARline+bytes((cam3.get()+':  '+name.get()).encode('utf-8')))  
        bob3.close()    
        print("cam3: " + cam3.get())
    except:
      print("cam3: " + cam3.get() + "Serial Port not Open")

def NameCam4(*args):
    try:
        bob4.open()
        bob4.write(CLEAR+FONT+ROW1+CLEARline+bytes((cam4.get()+':  '+name.get()).encode('utf-8')))  
        bob4.close()     
        print("cam4: " + cam4.get())
    except:
        print("cam4: " + cam4.get() + "Serial Port not Open")

# Set the line counter=======================================================================================================================
def SetDistance(*args):  

    distance.set('Seting Distance')
    print('Seting Distance')
    
    lineCounter.write(bytes('s'.encode('utf-8')))

    unit = StringVar()
    
    if units.get()  == 'feet':
        unit = 'f'
    elif units.get() == 'meters':
        unit = 'm'
    else:
        unit = 'c' 

    while not lineCounter.inWaiting():  pass                                # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))  # line counter responce [ count, feet, meters ]
                
    lineCounter.write(bytes(unit.encode('utf-8')))                          # send responce to the line counter

    while not lineCounter.inWaiting():  pass                                # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))  # line counter responce

    print('here')
    number = setDistance.get()
    print(number)
    for index in number:                        # Send number to line counter one charature at a time and waite for it to echo back
        lineCounter.write(bytes(index.encode('utf-8')))  
        while not lineCounter.inWaiting():  pass                                # wait for line counter
        while lineCounter.inWaiting():      print(str(lineCounter.readline()))  # line counter echos charature
                

    lineCounter.write(bytes('\r'.encode('utf-8')))  # send carage return to line counter to indicat the end of the number
        
    while not lineCounter.inWaiting():  pass                                # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))  # line counter responce
                
    lineCounter.write(bytes('y'.encode('utf-8')))

    while not lineCounter.inWaiting():  pass                                # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))  # line counter responce [ count, feet, meters ]
    
    distance.set('Done')
    
# Read / write Serial Data =========================================================================================================================
def ReadSerial():
    
    # Read Line Counter Data -----------------------------------------------------
    if lineCounter.isOpen() and lineCounter.inWaiting():
        while lineCounter.inWaiting():        
            data = lineCounter.readline()
            data = str(data[0:len(data)-2])
            data = tuple(data[2:len(data)-1].split(","))
       
            if data[0] == 'Counts':
                try:
                    feet ='Feet: ' + data[3]
                    meters = 'Meters: ' +data[5]
                    station = 'Station: ' +data[7]

                    Bobs(ROW3,station) 
        
                    distance.set(feet + '\t' + meters + '\t' + station)
                    #print("\n\nDistance: " + distance.get())
                except:
                    lineCounter.flushInput()

    # Read data from ROV -------------------------------------------------------
    if rovData.isOpen() and rovData.inWaiting():

        data = rovData.readline()
        data = str(data[0:len(data)-2])
        data = tuple(data[2:len(data)-1].split(","))
        rovData.flush()
        
        if data[0] == '$CMP':  # $CMP for ROV <====> $CAREV for micromoden

            try:
                heading ='Head: ' + data[1]
                pitch = 'Pitch: ' +data[2]
                roll = 'Roll: ' +data[3]
            
                try:
                    bob4.open()
                    bob4.write(ROW2)
                    bob4.write(CLEARline)
                    bob4.write(bytes((heading+'  '+pitch+'  '+roll).encode('utf-8')))
                    bob4.close()
                except:
                    pass

                imu.set(heading+'\t'+pitch+'\t'+roll)
                
            except:
                rovData.flush()

                
        
        elif data[0] == '$ANA':    # $ANA for ROV  <====> $GPRMC for micromoden 

            try:
                hv = 'Hv: ' +data[1]
                Depth = 'Depth: '+data[2]
                v12 = '12v: ' + data[3]
                leak = 'Leak: ' + data[4]

                depth.set(hv+Depth+v12+leak)

                #Bobs(ROW4,Depth)
                
                try:
                    bob4.open()
                    bob4.write(ROW1)
                    bob4.write(CLEARline)
                    bob4.write(bytes((hv+'  '+Depth+'  '+v12+'  '+leak).encode('utf-8')))
                    bob4.close()
                except:
                    pass

                
            except:
               rovData.flush()
            
            
                     
        else:
            print("Unexpectd Data: ")

        
    root.after(100, ReadSerial)

# Display time =================================================================================
def TimeKeeping (*args):
    Bobs(ROW2, time.ctime())
    root.after(500, TimeKeeping)


# Write Seial Data to Bobs ======================================================================
def Bobs(row,data):

    if type(data) == bytes:
        pass
    elif type(data) == str:
        data = bytes(data.encode('utf-8'))
    else:
        data = bytes(str(data).encode('utf-8'))
    

    try:
        bob1.open()
        bob1.write(row)
        bob1.write(CLEARline)
        bob1.write(data)
        bob1.close()
    except:
        pass

    try:
        bob2.open()
        bob2.write(row)
        bob2.write(CLEARline)
        bob2.write(data)
        bob2.close()
    except:
        pass
    
    try:
        bob3.open()
        bob3.write(row)
        bob3.write(CLEARline)
        bob3.write(data)
        bob3.close()
    except:
        pass
    

# ========================================================================================================================================
# ========================================================================================================================================
# ========================================================================================================================================

# Global variables ------------------------------------------------------------------

# Special Cammande for Bob
ESC = bytearray.fromhex("1b")
CSI = bytearray.fromhex("1b 5b")
CLEAR = CSI+bytes('2J'.encode('utf-8'))
CLEARline = CSI+bytes('2K'.encode('utf-8'))
FONT = CSI + bytes('4z'.encode('utf-8'))
ROW1 = CSI+bytes('0;0H'.encode('utf-8'))
ROW2 = CSI+bytes('1;0H'.encode('utf-8'))
ROW3 = CSI+bytes('2;0H'.encode('utf-8'))
ROW4 = CSI+bytes('3;0H'.encode('utf-8'))


# Generate a lost of com-ports ------------------------------------------------------------------------------
ports = glob.glob('/dev/tty*')

coms = []

# Check that the port is good -------------------
print("Serial ports found:")
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        coms.append(port)
        print(port)
            
    except (OSError , serial.SerialException):
        pass

ports = tuple(coms)

# Create Serial Poerts ==========================================================================================
# Create the serial port with the line counter -------------------------------
lineCounter = serial.Serial(None, baudrate = 115200, timeout = 0.3)

# Create the serial port for ROV data ----------------------------------------
rovData = serial.Serial(None, baudrate = 115200) # ROV baudrate 115200

# Create the Serial Port for the Sonar ---------------------------------------
sonarData = serial.Serial(None, baudrate = 4800, timeout = 0.3)

# Create Serial Ports to the Bobs ------------------------------------------------------------------------------
bob1 = serial.Serial(None, baudrate = 9600, timeout = 0.3)
bob2 = serial.Serial(None, baudrate = 9600, timeout = 0.3)
bob3 = serial.Serial(None, baudrate = 9600, timeout = 0.3)
bob4 = serial.Serial(None, baudrate = 9600, timeout = 0.3)

# Set up GUI ================================================================================================    
# Set up main window and text variables ----------------------------------------------------------------------------------------
root = Tk()
root.title("Video Over Lay")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

name = StringVar()
cam1 = StringVar()
cam2 = StringVar()
cam3 = StringVar()
cam4 = StringVar()

distance = StringVar()
depth = StringVar()
imu = StringVar()
setDistance = StringVar()
units = StringVar()

comPort1 = StringVar()
comPort2 = StringVar()
comPort3 = StringVar()
comPort4 = StringVar()
lcPort = StringVar()
rovPort = StringVar()
sonarPort = StringVar()

#=========================================================================================================================================
#=========================================================================================================================================
#=========================================================================================================================================


# Project Name ------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Project Name: ").grid(column=2, row=1, sticky=E)         # Label

name_entry = ttk.Entry(mainframe, width=7, textvariable=name)                       # Project name entry
name_entry.grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="set", command= Name).grid(column=4, row=1, sticky=W)    # Set button
name.set('No Name')

# Cameras --------------------------------------------------------------------------------------------------
# Cam1 -----------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam1:").grid(column=1, row=2, sticky=E)                      # Label

cam1_port = ttk.Combobox(mainframe, width=10, textvariable=comPort1)                     # Select comport
cam1_port.grid(column=2, row=2, sticky=(W, E))
cam1_port['values'] = ports
cam1_port.bind('<<ComboboxSelected>>',Cam1SerialPort)

cam1_name = ttk.Entry(mainframe, width=20, textvariable=cam1)                           # Camera name entry
cam1_name.grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="set", command= NameCam1).grid(column=4, row=2, sticky=W)    # Set button
cam1.set('No Name')

# Cam2 ----------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam2:").grid(column=1, row=3, sticky=E)                  # Label

cam2_port = ttk.Combobox(mainframe, width=10, textvariable=comPort2)                 # Select comport
cam2_port.grid(column=2, row=3, sticky=(W, E))
cam2_port['values'] = ports
cam2_port.bind('<<ComboboxSelected>>',Cam2SerialPort)

cam2_entry = ttk.Entry(mainframe, width=7, textvariable=cam2)                       # Camera name entry
cam2_entry.grid(column=3,row=3, sticky=(W,E))

ttk.Button(mainframe, text="set", command=NameCam2).grid(column=4, row=3, sticky=W) # Set button
cam2.set('No Name')

# Cam 3 --------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam3:").grid(column=1, row=4, sticky=E)                  # Label

cam3_port = ttk.Combobox(mainframe, width=10, textvariable=comPort3)                # Select com port
cam3_port.grid(column=2, row=4, sticky=(W, E))
cam3_port['values'] = ports
cam3_port.bind('<<ComboboxSelected>>',Cam3SerialPort)

cam3_entry = ttk.Entry(mainframe, width=7, textvariable=cam3)                       # Camera name entry
cam3_entry.grid(column=3,row=4, sticky=(W,E))

ttk.Button(mainframe, text="set", command=NameCam3).grid(column=4, row=4, sticky=W) # Set button
cam3.set('No Name')

# Cam 4 -------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam4-Pilot:").grid(column=1, row=5, sticky=E)                  # Label

cam4_port = ttk.Combobox(mainframe, width=10, textvariable=comPort4)                # Select com port
cam4_port.grid(column=2, row=5, sticky=(W, E))
cam4_port['values'] = ports
cam4_port.bind('<<ComboboxSelected>>',Cam4SerialPort)

cam4_entry = ttk.Entry(mainframe, width=7, textvariable=cam4)                       # Camera name entry
cam4_entry.grid(column=3,row=5, sticky=(W,E))

ttk.Button(mainframe, text="set", command=NameCam4).grid(column=4, row=5, sticky=W) # Set button
cam4.set('Pilot')

# Display Line Counter data ---------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Line Counter:").grid(column=1, row=6, sticky=E)                      # Label

lineCounter_port = ttk.Combobox(mainframe, width=10, textvariable=lcPort)                        # Select com port
lineCounter_port.grid(column=2, row=6, sticky=(W, E))
lineCounter_port['values'] = ports
lineCounter_port.bind('<<ComboboxSelected>>',LineCounterComPort)

ttk.Label(mainframe,width = 50, textvariable=distance).grid(column=3, row=6, sticky=(W, E))     # Display lincounter data
distance.set('No Reading')

#ttk.Button(mainframe, text="set", command=LineCounterComPort).grid(column=4, row=6, sticky=W)          # Set button

# Set Line Counter -------------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Set Distance:").grid(column=1, row=7, sticky=E)              # Lable

units_entry = ttk.Combobox(mainframe, width=10, textvariable=units)                     # Select Units to set
units_entry.grid(column=2, row=7, sticky=(W, E))
units_entry['values'] = ('Count', 'feet', 'meters')

lineCounter_entry = ttk.Entry(mainframe, width=7, textvariable=setDistance)             # Input the new distance
lineCounter_entry.grid(column=3,row=7, sticky=(W,E))

ttk.Button(mainframe, text="set", command=SetDistance).grid(column=4, row=7, sticky=W)  # Set button

# Select ROV Com Port --------------------------------------------------------------------
ttk.Label(mainframe, text="ROV:").grid(column=1, row=8, sticky=E)                       # Label

ROV_port = ttk.Combobox(mainframe, width=7, textvariable=rovPort)               # Select com port
ROV_port.grid(column=2, row=8, sticky=(W, E))
ROV_port['values'] = ports
ROV_port.bind('<<ComboboxSelected>>',ROVComPort)


# Dispaly depth Data ---------------------------------------------------------------------
ttk.Label(mainframe, text="Depth:").grid(column=2, row=9, sticky=E)             # Label
ttk.Label(mainframe, textvariable=depth).grid(column=3, row=9, sticky=(W, E))   # Display data
depth.set('No Reading')

# Display IMU Data -----------------------------------------------------------------------
ttk.Label(mainframe, text="IMU:").grid(column=2, row=10, sticky=E)              # Label
ttk.Label(mainframe, textvariable=imu).grid(column=3, row=10, sticky=(W, E))    # Display data
imu.set('No Reading')


# Select Sonar Com Port --------------------------------------------------------------------
ttk.Label(mainframe, text="Sonar:").grid(column=1, row=11, sticky=E)        # Label

sonar_port = ttk.Combobox(mainframe, width=7, textvariable=sonarPort) # Select com port
sonar_port.grid(column=2, row=11, sticky=(W, E))
sonar_port['values'] = ports
sonar_port.bind('<<ComboboxSelected>>',SonarComPort)

ttk.Button(mainframe, text="set", command=SonarComPort).grid(column=4, row=11, sticky=W) # Set button



# Make it look nice -----------------------------------------------------------------------
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# Start main loop =========================================================================================

root.after(100, ReadSerial)
root.after(500, TimeKeeping)
root.mainloop()


# Close Serial ports when program is closed
lineCounter.close()
rovData.close()
sonarData.close()
bob1.close()
bob2.close()
bob3.close()
bob4.close()
