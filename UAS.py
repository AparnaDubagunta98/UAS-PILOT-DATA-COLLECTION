import DeviceInitialization as di
import Recording as rc
import Processing as pro
import ErrorHandling as eh
import LEDControl as lc


#global definitions
usbPath = "/media/pi/VIDEOS"
localPath = "/home/pi/Documents/localVids"



# Main
fileNameList = []
duration = 0
startTime = 0
stopTime = 0

# Device Initialization
di.DeviceInitialization()
print("Done DI")

while(True):
    # Recording
    duration, fileNameList = rc.Recording()
    print("Done Recording")
    print("in driver Duration : ",duration)
    print("in driver FNL : ",fileNameList)

    # Processing
    pro.Processing(fileNameList,duration)
    print("Done Procesing")
   
    # Finish 
    di.finishInitialization()

