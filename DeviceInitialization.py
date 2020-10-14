#A1 - DeviceInitialization.py
#Imports:
#  ErrorHandling
#Function Definitions:
#  A1.2 - A1.6: individual functions ; if error : call corresponding error function
#  A1.7 - upon success light led to green
#  Error handling


import ErrorHandling
from vidgear.gears import VideoGear
from vidgear.gears import PiGear
import cv2
import os

#A1.2 - detects if the face camera (usb Camera) is accessible for recording
def detectFaceCam():
options_webcam = {"iso": 100, "exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters

try :
    video_streams = VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()
    print("detectFaceCam")
    video_stream.stop()
except:
    ErrorHandling.errorFaceCam()

#A1.3 - detects if the tablet camera (pi Camera) is accessible for recording
def detectTabletCam():

    options_picam = {"iso": 1800, "exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080}

    try :
        video_stream = VideoGear(source=2, resolution=(1920,1080), **options_picam).start()
        print("detectTabletCam")
        video_stream.stop()
    except:
        ErrorHandling.errorTabletCam()


#A1.4 - detects if an external storage device is connected to the proper USB port
def detectExternalUSB():
    try :
        print("detectExternalUSB")
    except:
        ErrorHandling.errorUSBDetect()

#A1.5 - detects if the external storage device has enough available video storage
def verifyStorageCapacity():
    try :
        print("verifyStorageCapacity")
    except:
        ErrorHandling.errorUSBStorage()

#A1.6 - prepares device storage for recording - deletes previous recordings and prepares folder
def prepLocalStorage():
    print("prepLocalStorage")

#A1.7 - changes LED to green to indicate device is ready to record.
def finishInitialization():
    print("finishInitialization")

#Calls initialiation functions in order
detectFaceCam()
detectTabletCam()
detectExternalUSB()
verifyStorageCapacity()
prepLocalStorage()
finishInitialization()
