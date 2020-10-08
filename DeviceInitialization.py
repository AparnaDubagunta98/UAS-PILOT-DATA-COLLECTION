#A1 - DeviceInitialization.py
#Imports:
#  ErrorHandling
#Function Definitions:
#  A1.2 - A1.6: individual functions ; if error : call corresponding error function
#  A1.7 - upon success light led to green
#  Error handling

import ErrorHandling

#A1.2
def detectFaceCam():
    try :
        print("detectFaceCam")
    except:
        ErrorHandling.errorFaceCam()

#A1.3
def detectTabletCam():
    try :
        print("detectTabletCam")
    except:
        ErrorHandling.errorTabletCam()

#A1.4
def detectExternalUSB():
    try :
        print("detectExternalUSB")
    except:
        ErrorHandling.errorUSBDetect()

#A1.5
def verifyStorageCapacity():
    try :
        print("verifyStorageCapacity")
    except:
        ErrorHandling.errorUSBStorage()

#A1.6
def prepLocalStorage():
    print("prepLocalStorage")

#A1.7
def finishInitialization():
    print("finishInitialization")

