#A2,A3 -- Recording.py
#  Function Defintiions:
#    2.1 Get time
#    2.2 Start Recording
#    2.3 Chnge LED to red (now recording)
#    --- common var : time stamp, video streams ---
#    3.1 Press button to stop ; Save files ; Get Stop time
#    3.2 Verify
#    3.3 change LED to Blue (now processing)
from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
from vidgear.gears import PiGear
import cv2
import ErrorHandling
import LEDControl
import os
import time

#path for USB drive
usbPath = "~/media/VIDEOS"
#path for local storage
localPath = "/home/pi/Documents/localVids"

#A2.1 -
def getStartTime():
    return time.time()

#A2.2 - starts two video streams and stores them in videoStreams. The start time is stored in startTime.
def startRecording(videoStreams, startTime):
    options_webcam = {"exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters
    options_picam = {"exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080}
    try:
        faceStream = VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()
        print("FaceCam Stream Started")
        tabletStream = VideoGear(source=2, resolution=(1920,1080), **options_picam).start()
        print("TabletCam Stream Started")
        startTime = getStartTime()
        videoStreams.append(faceStream)
        videoStreams.append(tabletStream)
    except:
        ErroHandling.errorRecording()


#A2.3 - Change LED to Red to singal recording has begun.
def changeLEDtoRed():
    LEDControl.turnRed()
    print("changeLEDtoRed")

#A3.1 - Stop the recording streams. Assumes videoStreams is a list of the streams (face camera followed by tablet camera).
def stopRecording(videoStreams):
    #maybe error handling
    for stream in videoStreams:
        stream.stop()
    print("stopRecording")

#A3.2 - Checks that the recorded files exist in
def verifyRecordings(fileNameList):
    return (path.exists(localPath + "/" + FaceCamVideo) and path.exists(localPath + "/" + TabletCamVideo))

#A3.3 - Changes LED to blue to signal recording has ended and processing will begin
def changeLEDtoBlue():
    LEDControl.turnBlue()
    print("changeLEDtoBlue")
