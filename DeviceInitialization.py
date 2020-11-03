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
usbPath = "/media/pi/VIDEOS"
#path for local storage
localPath = "/home/pi/Documents/localVids"

#A1.2 - detects if the face camera (usb Camera) is accessible for recording
def detectFaceCam():
    options_webcam = {"exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters

    try:
        video_stream = VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()
        video_stream.stop()
        print("FaceCam Detected")
        return True
    except:
        return False
        ErrorHandling.errorFaceCam()

#A1.3 - detects if the tablet camera (pi Camera) is accessible for recording
def detectTabletCam():

    options_picam = {"exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080}

    try:
        try:
            video_stream = VideoGear(source=2, resolution=(1920,1080), **options_picam).start()
            video_stream.stop()
        except:
            video_stream = VideoGear(source=1, resolution=(1920,1080), **options_picam).start()
            video_stream.stop()
        print("TabletCam Detected")
        return True
    except:
        return False
        ErrorHandling.errorTabletCam()


#A1.4 - detects if an external storage device is connected to the proper USB port
def detectExternalUSB():

    try :
        disk = os.statvfs(usbPath)
        print("External Storage USB Detected")
        return True
    except:
        return False
        ErrorHandling.errorUSBDetect()

#A1.5 - detects if the external storage device has enough available video storage
def verifyStorageCapacity():

    try:
        disk = os.statvfs(usbPath)
        availableSpaceMB = (disk.f_bfree * disk.f_bsize /1024/ 1024)
        print("Storage Available: %.3f MB" % (availableSpaceMB))
        if(availableSpaceMB > 330):
            print("External Storage Space Adequate")
            return True
        else:
            return True
            ErrorHandling.errorUSBStorage()
    except:
        return False
        ErrorHandling.errorUSBStorage()

#A1.6 - prepares device storage for recording - deletes previous recordings and prepares folder
def prepLocalStorage():

    try:
        if(os.path.exists(localPath)):
            for file in os.listdir(localPath):
                print(file)
                if(file.endswith(".mp4")):
                    print("removed")
                    os.system("sudo rm "+localPath+"/"+file)
        else:
            os.system("sudo mkdir " + localPath)
        print("Local Storage " + localPath + " prepared")
        return True
    except:
        return False

#A1.7 - changes LED to green to indicate device is ready to record.
def finishInitialization():
    #currently does not actually verify that all tests passed
    #calls LEDControl.turnGreen() function
    try:
        os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnGreen()'")
        print("Initialization Complete")
        return True
    except:
        return False

#Calls initialiation functions in order
def DeviceInitialization():
    detectFaceCam()
    detectTabletCam()
    detectExternalUSB()
    verifyStorageCapacity()
    prepLocalStorage()
    finishInitialization()
