# Main Function
import DeviceInitialization
import Recording
import Processing
import ErrorHandling
import LEDControl


#
fileNameList = []
videoStreams = []
mergedFileName = ""
startTime = 0
stopTime = 0

## Main

DeviceInitialization()
