#A5 ErrorHandling.py 
#Function Definitions:
#  Error5.1-5.6:
#    Error log update
#    Change LED pattern
#    Call UpdateErrorLog(time,ErrorName)

import LEDControl
import os
from time import sleep
import datetime

#A5.1
def errorFaceCam():
    print("errorFaceCam")
    updateErrorLog("No Face Cam detected")

    for i in range(10):
        #dot 1
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
        
        #dot 2
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

        #dot 3
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
    
    os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")


#A5.2
def errorTabletCam():
    print("errorTabletCam")
    updateErrorLog("Tablet Cam not detected")

    for i in range(10):
        #dot 1
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
        
        #dot 2
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

        #dot 3
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

    

#A5.3
def errorUSBDetect():
    print("errorUSBDetect")
    updateErrorLog("No USB Detected")

    for i in range(10):

        #dot 1
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
        
        #dot 2
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

        #dot 3
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

#A5.4
def errorUSBStorage():
    print("errorUSBStorage")
    updateErrorLog("No USB Storage")
    for i in range(10):

        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
        
        #dot 2
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

        #dot 3
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

#A5.5
def errorBadFile():
    print("errorBadFile")
    updateErrorLog("Bad File Save")
    for i in range(10):

        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
        
        #dot 2
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

        #dot 3
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

#A5.6
def errorBadSynch():
    print("errorBadSynch")
    updateErrorLog("Bad Vid Sync")
    for i in range(10):

        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)
        
        #dot 2
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

        #dot 3
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        sleep(1.5)
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnCustom(0, 0, 0)'")
        sleep(.5)

#A5.7
def updateErrorLog(errorName):
    ts = datetime.datetime.now().timestamp()

    usbLog = open("/media/pi/VIDEOS/errorLog.txt", "a")
    sdLog = open("/home/pi/Documents/localVids/errorLog.txt", "a")

    usbLog.write(errorName + " " + ts)
    sdLog.write(errorName + " " + ts)

    print(errorName)

    usbLog.close()
    sdLog.close()

