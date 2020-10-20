# Main Function
import DeviceInitialization
import Recording
import Processing
import ErrorHandling
import LEDControl


def button_setup():
    print("button")



#
fileNameList = []
videoStreams = []
mergedFileName = ""
startTime = 0
stopTime = 0

## Main
button_setup()

DeviceInitialization()
