#A2,A3 -- Recording.py
#  Function Defintiions:
#    2.1 Get time
#    2.2 Start Recording
#    2.3 Chnge LED to red (now recording)
#    --- common var : time stamp, video streams ---
#    3.1 Press button to stop ; Save files ; Get Stop time
#    3.2 Verify
#    3.3 change LED to Blue (now processing)

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

#A2.2 -
def startRecording():
    print("startRecording")
    startTime = getStartTime()

#A2.3 -
def changeLEDtoRed():
    LEDControl.turnRed()
    print("changeLEDtoRed")

#A3.1 - Stop the recording streams. Assumes videoStreams is a list of
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
