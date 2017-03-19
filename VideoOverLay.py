# Video Overlay Code
# Sea View
# March 16th 2017

import time
import serial
import glob

from tkinter import *
from tkinter import ttk

# Generate a lost of com-ports ------------------------------------------------------------------------------
ports = glob.glob('/dev/ttyUSB*')

coms = []

# Check that the port is good -------------------
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        coms.append(port)
        print(port)
            
    except (OSError , serial.SerialException):
        pass

ports = tuple(coms)

# Open Serial Poerts ==========================================================================================
# Open the serial port with the line counter ----------------------------------------
lineCounter = serial.Serial("/dev/ttyUSB0",baudrate = 115200, timeout = 0.3)

# Open the serial port for ROV data ----------------------------------------
rovData = serial.Serial("/dev/ttyUSB1",baudrate = 19200)

# Open Serial Port to Bob 4 ----------------------------------------------------
bob4 = serial.Serial('/dev/ttyUSB2', rtscts=True)



# Define functions ============================================================================================
# Set the line counter----------------------------------------------------------------------------------------
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
    
# Read Serial Data ----------------------------------------------------------------------------
def ReadSerial():
    
    # Read Line Counter Data -----------------------------------------------------
    if lineCounter.inWaiting():
                
        data = lineCounter.readline()
        lineCounter.flushInput()

        Bobs(ROW2,data[0:len(data)-2]) 
        
        data2 = str(data[0:len(data)-2])
        distance.set(data2[2:len(data)])
        print("\n\nDistance: " + distance.get())


    # Read data from ROV -------------------------------------------------------
    if rovData.inWaiting():

        dataRecived = rovData.readline()
        rovData.flush()
        
        if dataRecived[0:5] == bytes('$CARE'.encode('utf-8')):
            
            Bobs(ROW4, dataRecived[7:len(dataRecived)-2])
           
            state = str(dataRecived[7:len(dataRecived)-2])
            imu.set(state[2:len(state)-1])
            print('State: ' + imu.get())   
        
        elif dataRecived[0:5] == bytes('$GPRM'.encode('utf-8')):
            
            Bobs(ROW3, dataRecived[7:len(dataRecived)-2])
            
            alt = str(dataRecived[7:len(dataRecived)-2])
            depth.set(alt[2:len(alt)-1])
            print('Location: ' + depth.get())
                     
        else:
            print("Unexpectd Data: ")

        
    root.after(100, ReadSerial)


# Write Seial Data to Bobs
def Bobs(row,data):

    bob4.write(row)
    bob4.write(CLEARline)
    bob4.write(data)
    

# Name Cameras and their serial ports ------------------------------------------------------------------------------------------
def Name(*args):
    Bobs(ROW1,bytes((cam1.get()+':  '+name.get()).encode('utf-8')))
    print("Project Name: " + name.get())

    
def NameCam1(*args):

    bob4.write(ROW1)
    bob4.write(CLEARline)
    bob4.write(bytes((cam1.get()+':  '+name.get()).encode('utf-8')))
    
    print("com1: " + cam1.get())
    print("Serail Port: " + comPort1.get())

def NameCam2(*args):
    print("com2: " + cam2.get())
    print("Serail Port: " + comPort2.get())

def NameCam3(*args):
    print("com3: " + cam3.get())
    print("Serail Port: " + comPort3.get())

def NameCam4(*args):
    print("com4: " + cam4.get())
    print("Serail Port: " + comPort4.get())

# Select serial pors for Line counter, ROV and Sonar
def LineCounterComPort(*args):
    print("Line Counter Serail Port: " + lcPort.get())

def ROVComPort(*args):
    print("ROV Serail Port: " + rovPort.get())

def SonarComPort(*args):
    print("Sonar Serail Port: " + sonarPort.get())


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

bob4.write(CLEAR)
bob4.write(FONT)


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

cam1_name = ttk.Entry(mainframe, width=20, textvariable=cam1)                           # Camera name entry
cam1_name.grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="set", command= NameCam1).grid(column=4, row=2, sticky=W)    # Set button
cam1.set('No Name')

# Cam2 ----------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam2:").grid(column=1, row=3, sticky=E)                  # Label

cam2_port = ttk.Combobox(mainframe, width=10, textvariable=comPort2)                 # Select comport
cam2_port.grid(column=2, row=3, sticky=(W, E))
cam2_port['values'] = ports

cam2_entry = ttk.Entry(mainframe, width=7, textvariable=cam2)                       # Camera name entry
cam2_entry.grid(column=3,row=3, sticky=(W,E))

ttk.Button(mainframe, text="set", command=NameCam2).grid(column=4, row=3, sticky=W) # Set button
cam2.set('No Name')

# Cam 3 --------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam3:").grid(column=1, row=4, sticky=E)                  # Label

cam3_port = ttk.Combobox(mainframe, width=10, textvariable=comPort3)                # Select com port
cam3_port.grid(column=2, row=4, sticky=(W, E))
cam3_port['values'] = ports

cam3_entry = ttk.Entry(mainframe, width=7, textvariable=cam3)                       # Camera name entry
cam3_entry.grid(column=3,row=4, sticky=(W,E))

ttk.Button(mainframe, text="set", command=NameCam3).grid(column=4, row=4, sticky=W) # Set button
cam3.set('No Name')

# Cam 4 -------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam4:").grid(column=1, row=5, sticky=E)                  # Label

cam4_port = ttk.Combobox(mainframe, width=10, textvariable=comPort4)                # Select com port
cam4_port.grid(column=2, row=5, sticky=(W, E))
cam4_port['values'] = ports

cam4_entry = ttk.Entry(mainframe, width=7, textvariable=cam4)                       # Camera name entry
cam4_entry.grid(column=3,row=5, sticky=(W,E))

ttk.Button(mainframe, text="set", command=NameCam4).grid(column=4, row=5, sticky=W) # Set button
cam4.set('No Name')

# Display Line Counter data ---------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Line Counter:").grid(column=1, row=6, sticky=E)                      # Label

lineCounter_port = ttk.Combobox(mainframe, width=10, textvariable=lcPort)                        # Select com port
lineCounter_port.grid(column=2, row=6, sticky=(W, E))
lineCounter_port['values'] = ports

ttk.Label(mainframe,width = 50, textvariable=distance).grid(column=3, row=6, sticky=(W, E))     # Display lincounter data
distance.set('No Reading')

ttk.Button(mainframe, text="set", command=LineCounterComPort).grid(column=4, row=6, sticky=W)          # Set button

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

lineCounter_port = ttk.Combobox(mainframe, width=7, textvariable=rovPort)               # Select com port
lineCounter_port.grid(column=2, row=8, sticky=(W, E))
lineCounter_port['values'] = ports

#ttk.Label(mainframe,width = 50, textvariable=distance).grid(column=3, row=8, sticky=(W, E))
#distance.set('No Reading')

ttk.Button(mainframe, text="set", command=ROVComPort).grid(column=4, row=8, sticky=W)   # Set button


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

lineCounter_port = ttk.Combobox(mainframe, width=7, textvariable=sonarPort) # Select com port
lineCounter_port.grid(column=2, row=11, sticky=(W, E))
lineCounter_port['values'] = ports

#ttk.Label(mainframe,width = 50, textvariable=distance).grid(column=3, row=8, sticky=(W, E))
#distance.set('No Reading')

ttk.Button(mainframe, text="set", command=SonarComPort).grid(column=4, row=11, sticky=W) # Set button



# Make it look nice -----------------------------------------------------------------------
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# Start main loop =========================================================================================

root.after(100, ReadSerial)
root.mainloop()


# Close Serial ports when program is closed
lineCounter.close()
rovData.close()
bob4.close()
