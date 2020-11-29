# UAS Pilot Data Collection Tool
# CSCE 483 - Texas A&M University Fall 2020
# Christopher Wray, Jordan Griffin, Samuel Sells, Venkata Dubagunta
# This code was created for our senior design project intended for UAS Pilot Researchers
# Code was inherited from Spring 2020 Team : Rahul Rana, Aranpreet Gill, Maria Tyas, Juan Minor, Adolfo Herrera
# Previous team version available at : https://github.com/AparnaDubagunta98/UAS-PILOT-DATA-COLLECTION/tree/master/LEGACY


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
x = di.DeviceInitialization()
while(x == -1):
    x = di.DeviceInitialization()


print("SETUP COMPLETE \n")

while(True):
    # Recording
    duration, fileNameList = rc.Recording()
    #print("Done Recording")
    #print("in driver Duration : ",duration)
    #print("in driver FNL : ",fileNameList)

    # Processing
    vr = pro.Processing(fileNameList,duration)
    #print("verify processing return :",vr)
    print("Done Procesing")

    # Finish
    di.finishInitialization()
