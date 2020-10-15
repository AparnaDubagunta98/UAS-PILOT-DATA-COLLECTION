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
localPath = "~/Documents/localVids"

#A2.1
def getStartTime():
    print("getStartTime")

#A2.2
def startRecording():
    print("startRecording")

#A2.3
def changeLEDtoRed():
    LEDControl.turnRed()
    print("changeLEDtoRed")

#A3.1
def stopRecording():
    print("stopRecording")

#A3.2
def verifyRecordings():
    print("verifyRecordings")

#A3.3
def changeLEDtoBlue():
    LEDControl.turnBlue()
    print("changeLEDtoBlue")
