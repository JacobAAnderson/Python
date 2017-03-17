# Video Overlay Code
# Sea View
# March 16th 2017

import time
import serial

print("Serial Version: " + serial.VERSION)

from tkinter import *
from tkinter import ttk


# Open Serial Poerts ==========================================================================================
# Open the serial port with the line counter ----------------------------------------
lineCounter = serial.Serial("/dev/ttyUSB0",baudrate = 115200, timeout = 3.0)
print("Line Counter Port: " + lineCounter.name)


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

    while not lineCounter.inWaiting():  pass                            # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))   # line counter responce [ count, feet, meters ]
                
    lineCounter.write(bytes(unit.encode('utf-8')))                                             # send responce to the line counter

    while not lineCounter.inWaiting():  pass                            # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))   # line counter responce

    number = setDistance.get()
    for index in number:                                                # Send number to line counter one charature at a time and waite for it to echo back
        lineCounter.write(bytes(index.encode('utf-8')))  
        while not lineCounter.inWaiting():  pass                        # wait for line counter
        while lineCounter.inWaiting():      print(str(lineCounter.readline()))   # line counter echos charature
                

    lineCounter.write(bytes('\r'.encode('utf-8')))  # send carage return to line counter to indicat the end of the number
        
    while not lineCounter.inWaiting():  pass                            # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))   # line counter responce
                
    lineCounter.write(bytes('y'.encode('utf-8')))

    while not lineCounter.inWaiting():  pass                            # wait for line counter
    while lineCounter.inWaiting():      print(str(lineCounter.readline()))   # line counter responce [ count, feet, meters ]
    
    distance.set('Done')
    
# Read Line counter ----------------------------------------------------------------------------
def ReadLineCounter():
    if lineCounter.inWaiting():
        
        data = str(lineCounter.readline())
        distance.set(data)
        print("\n\nDistance: " + data)

    root.after(100, ReadLineCounter)

# Name Cameras ------------------------------------------------------------------------------------------
def Name(*args):
    print("Project Name: " + name.get())

def NameCom1(*args):
    print("com1: " + com1.get())

def NameCom2(*args):
    print("com2: " + com2.get())

def NameCom3(*args):
    print("com3: " + com3.get())

def NameCom4(*args):
    print("com4: " + com4.get())




# Set up GUI ===========================================================================================    
root = Tk()
root.title("Video Over Lay")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Global variables ------------------------------------------------------------------
name = StringVar()
com1 = StringVar()
com2 = StringVar()
com3 = StringVar()
com4 = StringVar()
distance = StringVar()
depth = StringVar()
imu = StringVar()



setDistance = StringVar()
units = StringVar()


# Project Name ---------------------------------------------------------------------------
name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
name_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Project Name: ").grid(column=1, row=1, sticky=E)
ttk.Button(mainframe, text="set", command= Name).grid(column=3, row=1, sticky=W)


# Cameras ---------------------------------------------------------------------------------
com1_entry = ttk.Entry(mainframe, width=20, textvariable=com1)
com1_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="com1:").grid(column=1, row=2, sticky=E)
ttk.Button(mainframe, text="set", command= NameCom1).grid(column=3, row=2, sticky=W)

com2_entry = ttk.Entry(mainframe, width=7, textvariable=com2)
com2_entry.grid(column=2,row=3, sticky=(W,E))
ttk.Label(mainframe, text="com2:").grid(column=1, row=3, sticky=E)
ttk.Button(mainframe, text="set", command=NameCom2).grid(column=3, row=3, sticky=W)

com3_entry = ttk.Entry(mainframe, width=7, textvariable=com3)
com3_entry.grid(column=2,row=4, sticky=(W,E))
ttk.Label(mainframe, text="com3:").grid(column=1, row=4, sticky=E)
ttk.Button(mainframe, text="set", command=NameCom3).grid(column=3, row=4, sticky=W)

com4_entry = ttk.Entry(mainframe, width=7, textvariable=com4)
com4_entry.grid(column=2,row=5, sticky=(W,E))
ttk.Label(mainframe, text="com4:").grid(column=1, row=5, sticky=E)
ttk.Button(mainframe, text="set", command=NameCom4).grid(column=3, row=5, sticky=W)

# Set Line Counter ----------------------------------------------------------------------------
lineCounter_entry = ttk.Entry(mainframe, width=7, textvariable=setDistance)
lineCounter_entry.grid(column=2,row=6, sticky=(W,E))

units_entry = ttk.Combobox(mainframe, width=7, textvariable=units)
units_entry.grid(column=3, row=6, sticky=(W, E))
units_entry['values'] = ('Count', 'feet', 'meters')

ttk.Button(mainframe, text="set", command=SetDistance).grid(column=4, row=6, sticky=W)
ttk.Label(mainframe, text="Set Distance:").grid(column=1, row=6, sticky=E)


# Display Line Counter, Depth, IMU data -------------------------------------------------------------
ttk.Label(mainframe, text="Line Counter:").grid(column=1, row=7, sticky=E)
ttk.Label(mainframe,width = 50, textvariable=distance).grid(column=2, row=7, sticky=(W, E))
distance.set('No Reading')

ttk.Label(mainframe, text="Depth:").grid(column=1, row=8, sticky=E)
ttk.Label(mainframe, textvariable=depth).grid(column=2, row=8, sticky=(W, E))
depth.set('No Reading')

ttk.Label(mainframe, text="IMU:").grid(column=1, row=9, sticky=E)
ttk.Label(mainframe, textvariable=imu).grid(column=2, row=9, sticky=(W, E))
imu.set('No Reading')

# Make it look nice -----------------------------------------------------------------------
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# Start main loop =========================================================================================
root.after(100, ReadLineCounter)
root.mainloop()

lineCounter.close()
