# Main Function
import DeviceInitialization
import Recording
import Processing
import ErrorHandling
import LEDControl

## Main - Runs functions in order (Startup, Record, Process)
#Any encountered errors are handled internally
#Will remove old Data on startup. Allows multiple recordings during session
DeviceInitialization.DeviceInitialization()
while(True){
    #Initialize Variables for this Recording
    fileNameList = []
    startTime = 0
    stopTime = 0
    #Record Videos
    Recording.Recording(fileNameList, startTime, stopTime)
    #Merge and export Videos
    Processing.Processing(fileNameList, stopTime - startTime)
}
