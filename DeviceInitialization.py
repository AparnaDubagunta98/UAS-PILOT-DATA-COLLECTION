#A1 - DeviceInitialization.py
#Imports:
#  ErrorHandling
#Function Definitions:
#  A1.2 - A1.6: individual functions ; if error : call corresponding error function
#  A1.7 - upon success light led to green
#  Error handling


import ErrorHandling
import LEDControl
from vidgear.gears import VideoGear
from vidgear.gears import PiGear
import cv2
import os

#path for USB drive
usbPath = "~/media/VIDEOS"
#path for local storage
localPath = "~/Documents/localVids"

#A1.2 - detects if the face camera (usb Camera) is accessible for recording
def detectFaceCam():
options_webcam = {"iso": 100, "exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters

try :
    video_streams = VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()
    print("FaceCam Detected")
    video_stream.stop()
except:
    ErrorHandling.errorFaceCam()

#A1.3 - detects if the tablet camera (pi Camera) is accessible for recording
def detectTabletCam():

    options_picam = {"iso": 1800, "exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080}

    try :
        video_stream = VideoGear(source=2, resolution=(1920,1080), **options_picam).start()
        print("TabletCam Detected")
        video_stream.stop()
    except:
        ErrorHandling.errorTabletCam()


#A1.4 - detects if an external storage device is connected to the proper USB port
def detectExternalUSB():

    try :
        disk = os.statvfs(usbPath)
        print("External Storage USB Detected")
    except:
        ErrorHandling.errorUSBDetect()

#A1.5 - detects if the external storage device has enough available video storage
def verifyStorageCapacity():

    try :
        disk = os.statvfs(usbPath)
        availableSpaceMB = (disk.f_bfree * disk.f_bsize /1024/ 1024)
        print("Storage Available: %.3f MB" % (availableSpaceMB))
        if(availableSpaceMB > 200)
            print(External Storage Space Adequate)
        else
            ErrorHandling.errorUSBStorage()
    except:
        ErrorHandling.errorUSBStorage()

#A1.6 - prepares device storage for recording - deletes previous recordings and prepares folder
def prepLocalStorage():
    if(os.path.exists(localPath))
        for file in os.listdir(localPath):
            #os.remove(file)
            #maybe have to add localPath to file disk_name
            print(file)
    else
        os.mkdir(path)
    print("Local Storage " + localPath + "prepared")

#A1.7 - changes LED to green to indicate device is ready to record.
def finishInitialization():
    #currently does not actually verify that all tests passed
    LEDControl.turnGreen()
    print("Initialization Complete")

#Calls initialiation functions in order
detectFaceCam()
detectTabletCam()
detectExternalUSB()
verifyStorageCapacity()
prepLocalStorage()
finishInitialization()
