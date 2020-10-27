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
import datetime
from gpiozero import Button


#path for USB drive
usbPath = "/media/pi/VIDEOS"
#path for local storage
localPath = "/home/pi/Documents/localVids"
# button
button = Button(27)


#A2.1 -
def getTime():
    return time.time()

# Helper function : File getNewFileNames
def getNewFileNames():
    ts = time.time()
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    FaceCamVideo = timeStamp + "_FaceCamVideo.mp4"
    TabletCamVideo = timeStamp + "_TabletCamVideo.mp4" #picam
    return [FaceCamVideo,TabletCamVideo]

#A2.3 - Change LED to Red to singal recording has begun.
def changeLEDtoRed():
    os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnRed()'")
    print("changeLEDtoRed")

#A2.2 - starts two video streams and stores them in videoStreams. The start time is stored in startTime.
def startRecording():
    global fileNameList
    global videoStreams
    global startTime
    global stopTime
    global writer_faceCam
    global writer_tabletCam
    stream1 = videoStreams[len(videoStreams) - 2] # penultimate stream
    stream2 = videoStreams[len(videoStreams) - 1] # ultimate stream
    output_params1 = {"-vcodec":"libx264", "-preset":"slow", "-bitrate":2000000, "-input_framerate":stream1.framerate}
    output_params2 = {"-input_framerate":stream2.framerate}

    startTime = getTime()
        
    changeLEDtoRed()

    print("Finished setup")

    fileNameList = getNewFileNames()

    writer1 = WriteGear(output_filename = fileNameList[0], **output_params1) 
    writer2 = WriteGear(output_filename = fileNameList[1], **output_params2)
    
    stream1.start()
    stream2.start()
    # record frame by frame
    while(True):
        frameA = stream1.read()
        # read frames from stream1

        frameB = stream2.read()
        # read frames from stream2
        print("stream1.framerate:" + str(stream1.framerate))
        print("stream2.framerate:" + str(stream2.framerate))

        # check if any of two frame is None
        if frameA is None:
            print("Frame A is none")
            
        if frameB is None:
            #if True break the infinite loop
            print("Frame B is none")
            stopTime = getTime()
            break
        
        #cv2.imshow("Output Frame1", frameA)
        #cv2.imshow("Output Frame2", frameB)
        # Show output window of stream1 and stream 2 seperately

        writer1.write(frameA)
        writer2.write(frameB)
        

        if(button.is_pressed):
            stopTime = getTime()
            break
        
    #cv2.destroyAllWindows()
        


        #ErrorHandling.errorRecording()



#A3.1 - Stop the recording streams. Assumes videoStreams is a list of the streams (face camera followed by tablet camera).
def stopRecording():
    global writer1
    global writer2
    global videoStreams

    #maybe error handling
    try:
        stream1 = videoStreams[len(videoStreams) - 2] # penultimate stream
        stream2 = videoStreams[len(videoStreams) - 1] # ultimate stream
        stream1.stop()
        stream2.stop()
        writer1.close()
        writer2.close()
        print("stopRecording")
        return True
    except:
        return False
        #ErrorHandling.errorRecording()

#A3.2 - Checks that the recorded files exist in
def verifyRecordings():
    if((os.path.exists(localPath + "/" + fileNameList[0]) and os.path.exists(localPath + "/" + fileNameList[1])) == False):
        return False
        #ErrorHandling.errorBadFile()
    else:
        return True

#A3.3 - Changes LED to blue to signal recording has ended and processing will begin
def changeLEDtoBlue():
    os.system("sudo python3 -c 'import LEDControl ;LEDControl.turnBlue()'")
    print("changeLEDtoBlue")

def Recording(videoStreams,fileNameList, startTime, stopTime):
    #wait for press
    while( not button.is_pressed):
        pass
    time.sleep(.5)
    #wait for release
    while (button.is_pressed):
        pass
    # setup streams, turn LED to red, record frame by frame until button is pressed
    startRecording(videoStreams,fileNameList, startTime,stopTime)
    #loop is broken
    stopRecording(videoStreams)
    verifyRecordings(fileNameList)
    changeLEDtoBlue()


def Recording2():
    options_picam = {"exposure_mode": "auto", "iso": 1800, "exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080} # define tweak parameters
    options_webcam = {"exposure_mode": "auto", "iso": 100, "exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters

    videoStreams.append(VideoGear(source=1, resolution=(1280,720), **options_picam).start()) 
    videoStreams.append(VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()) 

    stream1 = videoStreams[len(videoStreams) - 2] # penultimate stream
    stream2 = videoStreams[len(videoStreams) - 1] # ultimate stream

    output_params1 = {"-vcodec":"libx264", "-preset":"slow", "-bitrate":2000000, "-input_framerate":stream1.framerate}
    output_params2 = {"-input_framerate":stream2.framerate}

    writer1 = WriteGear(output_filename = "blank.mkv", **output_params1) #Define writer
    writer2 = WriteGear(output_filename = "blank.mkv", **output_params2) #Define writer

    #stream1.stop()
    #stream2.stop()

    startRecording()

    print("startRecording finished")
    time.sleep(5)
    print("Testing stopRecording")
    stopRecording()
    print("stopRecording finished")
    print("Testing verifyRecordings")

    vR = verifyRecordings()
    print(vR)
    print("verifyRecordings finished")
    changeLEDtoBlue()
    print("FileNameList: " + fileNameList[0] + " " + fileNameList[1])

##TESTTING CODE
print("Testing startRecording")
videoStreams = []
fileNameList = []
startTime = 0
stopTime = 0

options_picam = {"exposure_mode": "auto", "iso": 1800, "exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080} # define tweak parameters
options_webcam = {"exposure_mode": "auto", "iso": 100, "exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters

videoStreams.append(VideoGear(source=2, resolution=(1280,720), **options_picam).start()) 
videoStreams.append(VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()) 

stream1 = videoStreams[len(videoStreams) - 2] # penultimate stream
stream2 = videoStreams[len(videoStreams) - 1] # ultimate stream

output_params1 = {"-vcodec":"libx264", "-preset":"slow", "-bitrate":2000000, "-input_framerate":stream1.framerate}
output_params2 = {"-input_framerate":stream2.framerate}

writer1 = WriteGear(output_filename = "blank.mkv", **output_params1) #Define writer
writer2 = WriteGear(output_filename = "blank.mkv", **output_params2) #Define writer

#stream1.stop()
#stream2.stop()

startRecording()

print("startRecording finished")
time.sleep(5)
print("Testing stopRecording")
stopRecording()
print("stopRecording finished")
print("Testing verifyRecordings")

vR = verifyRecordings()
print(vR)
print("verifyRecordings finished")
changeLEDtoBlue()
print("FileNameList: " + fileNameList[0] + " " + fileNameList[1])
    
