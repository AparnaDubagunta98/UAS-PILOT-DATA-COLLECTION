
# Main Function
import DeviceInitialization
import Recording
import Processing
import ErrorHandling
import LEDControl

fileNameList = []
videoStreams = []
mergedFileName = ""
startTime = 0
stopTime = 0

#Device Initialization Unit Testing
if DeviceInitialization.detectFaceCam():
    print("detectFaceCam SUCCESS")
else:
    print("detectFaceCam FAIL")
if DeviceInitialization.detectTabletCam():
    print("detectTabletCam SUCCESS")
else:
    print("detectTabletCam FAIL")
if DeviceInitialization.detectExternalUSB():
    print("detectExternalUSB SUCCESS")
else:
    print("detectExternalUSB FAIL")
if DeviceInitialization.verifyStorageCapacity():
    print("verifyStorageCapacity SUCCESS")
else:
    print("verifyStorageCapacity FAIL")
if DeviceInitialization.prepLocalStorage():
    print("prepLocalStorage SUCCESS")
else:
    print("prepLocalStorage FAIL")
if DeviceInitialization.finishInitialization():
    print("finishInitialization SUCCESS")
else:
    print("finishInitialization FAIL")

#Recording Unit Testing
#create values to pass
if Recording.startRecording(videoStreams, fileNameList, startTime, stopTime):
    print("startRecording SUCCESS")
else:
    print("startRecording FAIL")
#create values to pass
if Recording.stopRecording(videoStreams):
    print("stopRecording SUCCESS")
else:
    print("stopRecording FAIL")
#create values to pass
if Recording.verifyRecordings(fileNameList):
    print("verifyRecordings SUCCESS")
else:
    print("verifyRecordings FAIL")

#Processing Unit testing
#Create values to pass
if sychronizeVideos(fileNameList, duration):
    print("sychronizeVideos SUCCESS")
else:
    print("sychronizeVideos FAIL")
if verifySynchedVideos(fileNameList):
    print("verifySynchedVideos SUCCESS")
else:
    print("verifySynchedVideos FAIL")
if exportVideos(fileNameList):
    print("exportVideos SUCCESS")
else:
    print("exportVideos FAIL")

#ErrorHandling Unit Testing ~ Visual Testing
ErrorHandling.errorFaceCam()
ErrorHandling.errorTabletCam()
ErrorHandling.errorUSBDetect()
ErrorHandling.errorUSBStorage()
ErrorHandling.errorBadFile()
ErrorHandling.errorBadSynch()
ErrorHandling.errorRecording()
#Give a name and check the error log afterwards
ErrorHandling.upDateErrorLog(errorName)

#LED Unit testing
LEDControl.turnGreen()
LEDControl.turnRed()
LEDControl.turnBlue()

#Button Unit testing
button = Button(27)
if(button.is_pressed()):
    print("Button Pressed")
else:
    print("Button Not Pressed")
