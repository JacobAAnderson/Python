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
    
# Find available serial Ports ----------------------------------------------------------------------------------------------------------
def CheckSerialPorts (*args): pass
#    PORTS = glob.glob('/dev/ttyUSB*') # Get a list of the availalbe USB-serial ports

#    global ports        # Call serial ports list
    
#    ports = []

    # Check that the port is good
#   for port in PORTS:
#        try:
#            s = serial.Serial(port)
#            s.close()
#            ports.append(port)
            
#        except (OSError , serial.SerialException):
#            pass

#    print (SerialPorts)
#    print(ports)


# Select serial port for Line counter -------------------------------------------------------------------------------------------------
def LineCounterComPort(*args):

    try:
        lineCounter.close() # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise

    

    # If anoter device is alredy using this serial port, shut it down and reassign its port to None
    if SerialPorts[lcPort.get()] != None:   

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[lcPort.get()].close()
            SerialPorts[lcPort.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                print(str(e))
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")

    
    lineCounter.port = lcPort.get() # Assign the serial port to the lineCounter object
    lineCounter.open()
    
    
    
    if lineCounter.isOpen():    # Check that the port opens
        print("Line Counter Serail Port: " + lcPort.get())

        try:
            SerialPorts[lcPort.get()] = lineCounter
        except serial.SerialException as e:
            print(str(e))

    else:
        print("Line Counter Serial Port Did Not Open")


# Select serial port for ROV -----------------------------------------------------------------------------------------------------------
def ROVComPort(*args):

    try:
        rovData.close() # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise


   
    # If anoter device is alredy using this serial port, shut it down and reassign its port to None
    if SerialPorts[rovPort.get()] != None:   

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[rovPort.get()].close()
            SerialPorts[rovPort.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                print(str(e))
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")


    # Assign the serial port to the rovData object    
    rovData.port = rovPort.get() 
    rovData.open()
    
    if rovData.isOpen():    # Make sure the serial port opens
        print("ROV Serail Port: " + rovPort.get())

        try:
            SerialPorts[rovPort.get()] = rovData
        except serial.SerialException as e:
            print(str(e))

        
    else:
        print("ROV Serial Port Did Not Open")
    
# Select serial port for Sonar ---------------------------------------------------------------------------------------------------------
def SonarComPort(*args):

    try:
        sonarData.close()   # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise

    
    # If anoter device is alredy using this serial port, shut it down and reassign its port to None
    if SerialPorts[sonarPort.get()] != None:   

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[sonarPort.get()].close()
            SerialPorts[sonarPort.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                print(str(e))
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")


    # Assign the serial port to the sonarData object
    sonarData.port = sonarPort.get()
    sonarData.open()
    
    if sonarData.isOpen():  # Make sure the serial port opens
        sonarData.close()
        print("Sonar Serail Port: " + sonarPort.get())

        try:
            SerialPorts[sonarPort.get()] = sonarData
        except serial.SerialException as e:
            print(str(e))

    else:
        print("Sonar Serial Port Did Not Open")


# Select Serial Port for Camara 1 -------------------------------------------------------------------------------------------------------
def Cam1SerialPort(*args):

    try:
        bob1.port.close()   # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise



    # If anoter device is alredy using this serial port, shut it down and reassign its port to None
    if SerialPorts[comPort1.get()] != None:

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[comPort1.get()].close()
            SerialPorts[comPort1.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                pass
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")


    bob1.port = comPort1.get()  # Assign the serial port to the bob1 object ie.. first Bob4
    bob1.open()
    
    if bob1.isOpen():   # Make sure the serial port opens
        print("Cam1, " +cam1.get()+" Serail Port: " + comPort1.get())
        bob1.write(CLEAR+FONT+ROW1)
        bob1.write(bytes(("Cam1 on " +comPort1.get()).encode('utf-8')))
         
        try:
            SerialPorts[comPort1.get()] = bob1
        except serial.SerialException as e:
            print(str(e))
        
    else:
        print("Cam1," +cam1.get()+ " Serial Port Did Not Open")

    bob1.close()


# Select Serial Port for Camara 2 -------------------------------------------------------------------------------------------------------
def Cam2SerialPort(*args):

    try:
        bob2.port.close()   # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise



    # If anoter device is alredy using this serial port, shut it down and reassign its port to None
    if SerialPorts[comPort2.get()] != None:   

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[comPort2.get()].close()
            SerialPorts[comPort2.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                print(str(e))
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")


    
    bob2.port = comPort2.get()  # Assign the serial port to the bob2 object
    bob2.open()
    
    if bob2.isOpen():   # Make sure the serial port is open
        print("Cam2, " +cam2.get()+" Serail Port: " + comPort2.get())
        bob2.write(CLEAR+FONT+ROW1)
        bob2.write(bytes(("Cam2 on " +comPort2.get()).encode('utf-8')))

        try:
            SerialPorts[comPort2.get()] = bob2
        except serial.SerialException as e:
            print(str(e))
        
    else:
        print("Cam2," +cam2.get()+ " Serial Port Did Not Open")

    bob2.close()


# Select Serial Port for Camara 3 -------------------------------------------------------------------------------------------------------
def Cam3SerialPort(*args):

    try:
        bob3.port.close()   # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise


    # If anoter device is alredy using this serial port, shut it down and reassign its port to None
    if SerialPorts[comPort3.get()] != None:   # If anoter device is alredy using this serial port, shut it down and reassign its port to None

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[comPort3.get()].close()
            SerialPorts[comPort3.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                print(str(e))
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")

    
    bob3.port = comPort3.get()  # Assign the serial port to the bob3 object
    bob3.open()
    
    if bob3.isOpen():   # Make sure the serial port opens
        print("Cam3, " +cam3.get()+" Serail Port: " + comPort3.get())
        bob3.write(CLEAR+FONT+ROW1)
        bob3.write(bytes(("Cam3 on " +comPort3.get()).encode('utf-8')))

        try:
            SerialPorts[comPort3.get()] = bob3
        except serial.SerialException as e:
            print(str(e))

        
    else:
        print("Cam3," +cam3.get()+ " Serial Port Did Not Open")

    bob3.close()


# Select Serial Port for Camara 4 -------------------------------------------------------------------------------------------------------
def Cam4SerialPort(*args):

    try:
        bob4.port.close()   # Make sure the port isn't already open
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise
    except AttributeError as e:
        if str(e) == "'str' object has no attribute 'close'":
            pass
        elif str(e) =="'NoneType' object has no attribute 'close'":
            pass
        else:
            raise
    except:
        raise



    # If anoter device is alredy using this serial port, shut it down and reassign its port to None    
    if SerialPorts[comPort4.get()] != None:   

        print('This port is alreay taken.\nShutting done the exisitng port\n\n')

        try:
            SerialPorts[comPort4.get()].close()
            SerialPorts[comPort4.get()].port = None
        except serial.SerialException as e:
            if str(e) =='Port must be configured before it can be used.':
                print(str(e))
            elif str(e) == 'Port is already closed.':
                pass
            else:
                raise

    else:
        print("Serial port is free")


    # Assign serial port to the bob4 object. This is the Pilot's monitoir
    bob4.port = comPort4.get()  
    bob4.open()
    
    if bob4.isOpen():
        print("Cam4, " +cam4.get()+" Serail Port: " + comPort4.get())
        bob4.write(CLEAR+FONT+ROW1 + bytes(("Cam4 on " +comPort4.get()).encode('utf-8')))

        try:
            SerialPorts[comPort4.get()] = bob4
        except serial.SerialException as e:
            print(str(e))

        
    else:
        print("Cam4," +cam4.get()+ " Serial Port Did Not Open")

    bob4.close()


# Send Project Name to cameras ------------------------------------------------------------------------------------------------------------
def Name(*args):
    Bobs(ROW1,bytes((cam1.get()+':  '+name.get()).encode('utf-8')))
    print("Project Name: " + name.get())


# Assign name to camara 1 ------------------------------------------------------------------------------------------------------------------
def NameCam1(*args):
    try:
        bob1.open()    
        bob1.write(CLEAR+FONT+ROW1)
        bob1.write(bytes((cam1.get()+':  '+name.get()).encode('utf-8')))
        bob1.close()
        print("cam1: " + cam1.get())
    except:
        print("cam1: " + cam1.get() + "Serial Port not Open")


# Assign name to camara 2 ------------------------------------------------------------------------------------------------------------------
def NameCam2(*args):
    try:
        bob2.open()
        bob2.write(CLEAR+FONT+ROW1)
        bob2.write(bytes((cam2.get()+':  '+name.get()).encode('utf-8')))  
        bob2.close()
        print("cam2: " + cam2.get())
    except:
        print("cam2: " + cam2.get() + "Serial Port not Open")


# Assign name to camara 3 ------------------------------------------------------------------------------------------------------------------
def NameCam3(*args):
    try:
        bob3.open()
        bob3.write(CLEAR+FONT+ROW1)
        bob3.write(bytes((cam3.get()+':  '+name.get()).encode('utf-8')))  
        bob3.close()    
        print("cam3: " + cam3.get())
    except:
      print("cam3: " + cam3.get() + "Serial Port not Open")


# Assign name to camara 4 ------------------------------------------------------------------------------------------------------------------
def NameCam4(*args):
    try:
        bob4.open()
        bob4.write(CLEAR+FONT+ROW1)
        bob3.write(bytes((cam4.get()+':  '+name.get()).encode('utf-8')))  
        bob4.close()     
        print("cam4: " + cam4.get())
    except:
        print("cam4: " + cam4.get() + "Serial Port not Open")


# Set the line counter=======================================================================================================================
def SetDistance(*args):  

    # Check that the line counter serial port is opend and raise errors unless the serial port hasn't been configured
    try:
        lineCounter.open()
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            print('Select a serial port for the line counter befor setting distance')
        elif str(e) == 'Port is already open.':
            pass
        else:
            raise  
 

    feet.set('Seting Distance')
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
    
    feet.set('Done')


# Read / write Serial Data =========================================================================================================================
def ReadSerial():

    # Check that the line counter serial port is opend and raise errors unless the serial port hasn't been configured
    try:
        lineCounter.open()
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        elif str(e) == 'Port is already open.':
            pass
        else:
            raise  
    
    # Read Line Counter Data 
    if lineCounter.isOpen() and lineCounter.inWaiting():

        data = ()
        
        while lineCounter.inWaiting():        
            data = lineCounter.readline()

        data = str(data[0:len(data)-2])
        data = tuple(data[2:len(data)-1].split(","))
       
        if data[0] == 'Counts':
            try:
                counts.set(str(data[1]))
                feet.set(str(data[3]))
                meters.set(str(data[5]))
                station.set(str(data[7]))

                distance = ''
                if useFeet.get():
                    distance += 'Feet: ' + feet.get()
                    distance += '  '

                if useMeters.get():
                    distance += 'Meters: ' + meters.get()
                    distance += '  '

                if useStation.get():
                    distance += 'Station: ' + station.get()

                Bobs(ROW3,distance) 

            except:
                print('Flushing line counter serial buffer')
                lineCounter.flushInput()



    # Read data from ROV 

    # Check that the ROV serial port is opend and raise errors unless the serial port hasn't been configured
    try:
        rovData.open()
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        elif str(e) == 'Port is already open.':
            pass
        else:
            raise

    if rovData.isOpen() and rovData.inWaiting():

        data = rovData.readline()
        data = str(data[0:len(data)-2])
        data = tuple(data[2:len(data)-1].split(","))
        rovData.flush()
        
        if data[0] == '$CMP' or data[0] == '$CAREV':  # $CMP for ROV <====> $CAREV for micromoden

            try:
                heading ='Head: ' + data[1]
                pitch = 'Pitch: ' +data[2]
                roll = 'Roll: ' +data[3]
            
                try:
                    bob4.open()
                    bob4.write(ROW2)
                    bob4.write(bytes((heading+'  '+pitch+'  '+roll).encode('utf-8')))
                    bob4.write(CLEARafter)
                    bob4.close()
                except:
                    pass

                imu.set(heading+'\t'+pitch+'\t'+roll)
                
            except:
                print( 'Flush ROV serial buffer')
                rovData.flush()

                
        
        elif data[0] == '$ANA' or data[0] == '$GPRMC':    # $ANA for ROV  <====> $GPRMC for micromoden 

            try:
                hv = 'Hv: ' +data[1]
                Depth = 'Depth: '+data[2]
                v12 = '12v: ' + data[3]
                leak = 'Leak: ' + data[4]

                depth.set(hv+Depth+v12+leak)

                
                try:
                    bob4.open()
                    bob4.write(ROW1)
                    bob4.write(bytes((hv+'  '+Depth+'  '+v12+'  '+leak).encode('utf-8')))
                    bob4.write(CLEARafter)
                    bob4.close()
                except:
                    pass

                
            except:
                print( 'Flush ROV serial buffer')
                rovData.flush()
            
            
                     
        else:
            print("Unexpectd Data: ")

        
    root.after(100, ReadSerial)


# Send Data to the Sonar =======================================================================
def SendToSonar (*args):

    
    data = '$GPGLL,-'+meters.get().zfill(6)+'00,S,-'+feet.get().zfill(6)+'000,E,-'+counts.get().zfill(5)+'.000,A*2D\r\n'
    
    try:    
        sonarData.open()
        sonarData.write(data.encode('utf-8'))
        sonarData.close()

        #print(data)
        
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise


    root.after(100, SendToSonar)
    

# Display time =================================================================================
def TimeKeeping (*args):
    Bobs(ROW2, time.strftime('%d/%m/%Y  %I:%M:%S'))
    root.after(250, TimeKeeping)


# Write Seial Data to Bobs ======================================================================
def Bobs(row,data):

    if type(data) == bytes:
        pass
    elif type(data) == str:
        data = bytes(data.encode('utf-8'))
    else:
        data = bytes(str(data).encode('utf-8'))
    
    # Write to first Bob4
    try:
        bob1.open()
        bob1.write(row)
        bob1.write(data)
        bob1.write(CLEARafter)
        bob1.close()
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise

    # Write to second Bob4
    try:
        bob2.open()
        bob2.write(row)
        bob2.write(data)
        bob2.write(CLEARafter)
        bob2.close()
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise

    # Write to third Bob4
    try:
        bob3.open()
        bob3.write(row)
        bob3.write(data)
        bob3.write(CLEARafter)
        bob3.close()
    except serial.SerialException as e:
        if str(e) =='Port must be configured before it can be used.':
            pass
        else:
            raise


# ========================================================================================================================================
# ========================================================================================================================================
# ========================================================================================================================================

# Global variables ------------------------------------------------------------------

# Special Cammande for Bob
ESC = bytearray.fromhex("1b")                   # Escape sequence
CSI = bytearray.fromhex("1b 5b")                # Control sequence introducer
CLEAR = CSI+bytes('2J'.encode('utf-8'))         # Clear the entier screen,
CLEARline = CSI+bytes('2K'.encode('utf-8'))     # Clear the line that the cursor is on
CLEARafter = CSI+bytes('0K'.encode('utf-8'))    # Clear from the cursor to the end of the line
FONT = CSI + bytes('4z'.encode('utf-8'))        # Font style 6X10 --> Smallest font
ROW1 = CSI+bytes('0;0H'.encode('utf-8'))        # Move cursor to line 1
ROW2 = CSI+bytes('1;0H'.encode('utf-8'))        # Move cursor to line 2
ROW3 = CSI+bytes('2;0H'.encode('utf-8'))        # Move cursor to line 3
ROW4 = CSI+bytes('3;0H'.encode('utf-8'))        # Move cursor to line 4



# Create Serial Instances ===============================================================================================================
# Find available serial ports -----------------------------------------------------------------------------------------------------------
SerialPorts = {}    # Dictionary that tracks the sertial instances
ports = []          # List of available USB serial ports

PORTS = glob.glob('/dev/ttyUSB*') # Get a list of the availalbe USB-serial ports

# Check that the port is good
for port in PORTS:
    try:
        s = serial.Serial(port)
        s.close()
        ports.append(port)
        print(port)
        SerialPorts[port] = None

            
    except (OSError , serial.SerialException):
        pass


# Create serial instance for the line counter -------------------------------
lineCounter = serial.Serial(None, baudrate = 115200, timeout = 0.3)

# Create serial instance for for ROV data ----------------------------------------
rovData = serial.Serial(None, baudrate = 19200) # ROV baudrate 115200

# Create Serial instance for the Sonar ---------------------------------------
sonarData = serial.Serial(None, baudrate = 4800, timeout = 0.3)

# Create Serial instance for the Bobs ------------------------------------------------------------------------------
bob1 = serial.Serial(None, baudrate = 9600, timeout = 0.3)
bob2 = serial.Serial(None, baudrate = 9600, timeout = 0.3)
bob3 = serial.Serial(None, baudrate = 9600, timeout = 0.3)
bob4 = serial.Serial(None, baudrate = 9600, timeout = 0.3)


# Set up GUI =======================================================================================================================
#===================================================================================================================================
#===================================================================================================================================

# Set up main window and text variables ----------------------------------------------------------------------------------------
root = Tk()
root.title("Video Over Lay")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# GUI specific varialbes ------------------------------------------------------------------------------------------------------

name = StringVar()
cam1 = StringVar()
cam2 = StringVar()
cam3 = StringVar()
cam4 = StringVar()

depth = StringVar()
imu = StringVar()
setDistance = StringVar()
units = StringVar()

counts = StringVar()
feet = StringVar()
meters = StringVar()
station = StringVar()

useFeet = BooleanVar()
useMeters = BooleanVar()
useStation = BooleanVar()

comPort1 = StringVar()
comPort2 = StringVar()
comPort3 = StringVar()
comPort4 = StringVar()
lcPort = StringVar()
rovPort = StringVar()
sonarPort = StringVar()


# GUI widgets ============================================================================================================================
# Project Name ------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Project Name: ").grid(column=2, row=1, sticky=E)         # Label

name_entry = ttk.Entry(mainframe, width=50, textvariable=name)                       # Project name entry
name_entry.grid(column=3, row=1, columnspan =2, sticky=W)

ttk.Button(mainframe, text="set", command= Name).grid(column=5, row=1, sticky=W)    # Set button
name.set('No Name')

# Cameras --------------------------------------------------------------------------------------------------
# Cam1 -----------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam1:").grid(column=1, row=2, sticky=E)                      # Label

cam1_port = ttk.Combobox(mainframe, width=10, textvariable=comPort1, values = ports, postcommand = CheckSerialPorts)    # Select comport
cam1_port.grid(column=2, row=2, sticky=(W, E))
cam1_port.bind('<<ComboboxSelected>>',Cam1SerialPort)

cam1_name = ttk.Entry(mainframe, width=50, textvariable=cam1)                           # Camera name entry
cam1_name.grid(column=3, row=2, columnspan =2, sticky=W)

ttk.Button(mainframe, text="set", command= NameCam1).grid(column=5, row=2, sticky=W)    # Set button
cam1.set('No Name')

# Cam2 ----------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam2:").grid(column=1, row=3, sticky=E)                  # Label

cam2_port = ttk.Combobox(mainframe, width=10, textvariable=comPort2,values = ports, postcommand = CheckSerialPorts) # Select comport
cam2_port.grid(column=2, row=3, sticky=(W, E))
cam2_port.bind('<<ComboboxSelected>>',Cam2SerialPort)

cam2_name = ttk.Entry(mainframe, width=50, textvariable=cam2)                       # Camera name entry
cam2_name.grid(column=3,row=3, columnspan =2, sticky=W)

ttk.Button(mainframe, text="set", command=NameCam2).grid(column=5, row=3, sticky=W) # Set button
cam2.set('No Name')

# Cam 3 --------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam3:").grid(column=1, row=4, sticky=E)                  # Label

cam3_port = ttk.Combobox(mainframe, width=10, textvariable=comPort3,values = ports, postcommand = CheckSerialPorts) # Select com port
cam3_port.grid(column=2, row=4, sticky=(W, E))
cam3_port.bind('<<ComboboxSelected>>',Cam3SerialPort)

cam3_name = ttk.Entry(mainframe, width=50, textvariable=cam3)                       # Camera name entry
cam3_name.grid(column=3,row=4, columnspan =2, sticky=W)

ttk.Button(mainframe, text="set", command=NameCam3).grid(column=5, row=4, sticky=W) # Set button
cam3.set('No Name')

# Cam 4 -------------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Cam4-Pilot:").grid(column=1, row=5, sticky=E)                  # Label

cam4_port = ttk.Combobox(mainframe, width=10, textvariable=comPort4,values = ports, postcommand = CheckSerialPorts) # Select com port
cam4_port.grid(column=2, row=5, sticky=(W, E))
cam4_port.bind('<<ComboboxSelected>>',Cam4SerialPort)

cam4_name = ttk.Entry(mainframe, width=50, textvariable=cam4)                       # Camera name entry
cam4_name.grid(column=3,row=5, columnspan =2, sticky=W)

ttk.Button(mainframe, text="set", command=NameCam4).grid(column=5, row=5, sticky=W) # Set button
cam4.set('Pilot')

# Line Counter data ---------------------------------------------------------------------------------------------
ttk.Label(mainframe, text="").grid(column=1, row=6, sticky=E) # Insert a space between the camera names and the data intake
ttk.Label(mainframe, text="Line Counter:").grid(column=1, row=7, sticky=E)                      # Label

lineCounter_port = ttk.Combobox(mainframe, width=10, textvariable=lcPort,values = ports, postcommand = CheckSerialPorts)  # Select serial port                       # Select com port
lineCounter_port.grid(column=2, row=7, sticky=(W, E))
lineCounter_port.bind('<<ComboboxSelected>>',LineCounterComPort)


# Set Line Counter -------------------------------------------------------------------------------------------------------
units_entry = ttk.Combobox(mainframe, width=10, textvariable=units)                     # Select Units to set
units_entry.grid(column=3, row=7, sticky=(W, E))
units_entry['values'] = ('Count', 'feet', 'meters')

lineCounter_entry = ttk.Entry(mainframe, width=20, textvariable=setDistance)             # Input the new distance
lineCounter_entry.grid(column=4,row=7, sticky=(W,E))

ttk.Button(mainframe, text="set", command=SetDistance).grid(column=5, row=7, sticky=W)  # Set button


# Select which line counter measurments to display--------------------------------
feet_select = ttk.Checkbutton(mainframe, text = 'Feet', variable = useFeet)
feet_select.grid(column=2, row=8, sticky=W)
useFeet.set('0')
ttk.Label(mainframe,width = 10, textvariable=feet).grid(column=3, row=8, sticky= W)
feet.set('No Reading')

meters_select = ttk.Checkbutton(mainframe, text = 'Meters', variable = useMeters)
meters_select.grid(column=2, row=9, sticky=W)
useMeters.set('0')
ttk.Label(mainframe,width = 10, textvariable=meters).grid(column=3, row=9, sticky= W)
meters.set('No Reading')

Station_select = ttk.Checkbutton(mainframe, text = 'Station', variable = useStation)
Station_select.grid(column=2, row=10, sticky=W)
useStation.set('0')
ttk.Label(mainframe,width = 10, textvariable=station).grid(column=3, row=10, sticky= W)
station.set('No Reading')

# Select ROV Com Port --------------------------------------------------------------------
ttk.Label(mainframe, text="ROV:").grid(column=1, row=12, sticky=E)                       # Label

ROV_port = ttk.Combobox(mainframe, width=7, textvariable=rovPort, values = ports, postcommand = CheckSerialPorts)   # Select com port
ROV_port.grid(column=2, row=12, sticky=(W, E))
ROV_port.bind('<<ComboboxSelected>>',ROVComPort)


# Dispaly depth Data ---------------------------------------------------------------------
ttk.Label(mainframe, text="Depth:").grid(column=2, row=13, sticky=E)             # Label
ttk.Label(mainframe, textvariable=depth).grid(column=3, row=13, sticky=(W, E))   # Display data
depth.set('No Reading')

# Display IMU Data -----------------------------------------------------------------------
ttk.Label(mainframe, text="IMU:").grid(column=2, row=14, sticky=E)              # Label
ttk.Label(mainframe, textvariable=imu).grid(column=3, row=14, sticky=(W, E))    # Display data
imu.set('No Reading')


# Select Sonar Com Port --------------------------------------------------------------------
ttk.Label(mainframe, text="Sonar:").grid(column=1, row=15, sticky=E)        # Label

sonar_port = ttk.Combobox(mainframe, width=7, textvariable=sonarPort,values = ports, postcommand = CheckSerialPorts) # Select com port
sonar_port.grid(column=2, row=15, sticky=(W, E))
sonar_port.bind('<<ComboboxSelected>>',SonarComPort)

#ttk.Button(mainframe, text="set", command=SonarComPort).grid(column=4, row=15, sticky=W) # Set button



# Make it look nice -----------------------------------------------------------------------
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# Initiate repeted function and Start main loop =========================================================================================

root.after(50, ReadSerial)         # Read Serial Porst every 100 milliseconds
root.after(75, TimeKeeping)        # Update time twice a second
root.after(100, SendToSonar)

root.mainloop()


# Close Serial ports when program is closed
lineCounter.close()
rovData.close()
sonarData.close()
bob1.close()
bob2.close()
bob3.close()
bob4.close()
