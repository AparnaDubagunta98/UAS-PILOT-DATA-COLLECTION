#A1 - DeviceInitialization.py
#Imports:
#  ErrorHandling
#Function Definitions:
#  A1.2 - A1.6: individual functions ; if error : call corresponding error function
#  A1.7 - upon success light led to green
#  Error handling


import ErrorHandling
from vidgear.gears import VideoGear
import os

#A1.2
def detectFaceCam():
    video_streams = []
    options_picam = {"exposure_mode": "auto", "iso": 1800, "exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080}
    try :
        video_streams.push(VideoGear(source=2, resolution=(1920,1080), **options_picam).start())
        print("detectFaceCam")
    except:
        ErrorHandling.errorFaceCam()
    video_streams[0].stop()

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

detectFaceCam()
detectTabletCam()
detectExternalUSB()
verifyStorageCapacity()
prepLocalStorage()
finishInitialization()
