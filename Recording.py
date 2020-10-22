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
    FaceCamVideo = ts + "_FaceCamVideo.mp4"
    TabletCamVideo = ts + "_TabletCamVideo.mp4" #picam
    return [FaceCamVideo,TabletCamVideo]

#A2.2 - starts two video streams and stores them in videoStreams. The start time is stored in startTime.
#A2.3 - Change LED to Red to singal recording has begun.
def changeLEDtoRed():
    LEDControl.turnRed()
    print("changeLEDtoRed")

def startRecording(videoStreams,fileNameList, startTime,stopTime):
    options_webcam = {"exposure_compensation": 0, "awb_mode": "sun", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080, "CAP_PROP_AUTOFOCUS": 'True'} # define tweak parameters
    options_picam = {"exposure_compensation": 15, "awb_mode": "horizon", "sensor_mode": 0, "CAP_PROP_FRAME_WIDTH ":1920, "CAP_PROP_FRAME_HEIGHT":1080}
    try:
        faceStream = VideoGear(source=0, resolution=(1920,1080), **options_webcam).start()
        print("FaceCam Stream Started")
        tabletStream = VideoGear(source=2, resolution=(1920,1080), **options_picam).start()
        print("TabletCam Stream Started")

        fileNameList = getNewFileNames()
        output_params_faceCam = {"-vcodec":"libx264", "-preset":"slow", "-bitrate":2000000, "-input_framerate":faceStream.framerate}
        output_params_tabletCam = {"-input_framerate":tabletStream.framerate}
        writer_faceCam = WriteGear(output_filename = fileNameList[0], **output_params_faceCam)
        writer_tabletCam = WriteGear(output_filename = fileNameList[1], **output_params_tabletCam)

        startTime = getTime()
        videoStreams.append(faceStream)
        videoStreams.append(tabletStream)

        changeLEDtoRed()

        # record frame by frame
        while(True):
            frame_faceCam = stream_faceCam.read()
            frame_tabletCam = stream_tabletCam.read()
            # read frames from stream2
            # print("stream_faceCam.framerate:" + str(stream_faceCam.framerate))
            # print("stream_tabletCam.framerate:" + str(stream_tabletCam.framerate))

            # check if any of two frame is None
            if frame_faceCam is None or frame_tabletCam is None:
                stopTime = getTime()
                break

            #legacy code for testing
            #cv2.imshow("Output Frame1", frameA)
            #cv2.imshow("Output Frame2", frameB)
            # Show output window of stream1 and stream 2 seperately

            writer_faceCam.write(frame_faceCam)
            writer_tabletCam.write(frame_tabletCam)

            if(button.is_pressed):
                stopTime = getTime()
                break

            return True


    except:
        return False
        #ErrorHandling.errorRecording()



#A3.1 - Stop the recording streams. Assumes videoStreams is a list of the streams (face camera followed by tablet camera).
def stopRecording(videoStreams):
    #maybe error handling
    try:
        for stream in videoStreams:
            stream.stop()
        print("stopRecording")
        return True
    except:
        return False
        #ErrorHandling.errorRecording()

#A3.2 - Checks that the recorded files exist in
def verifyRecordings(fileNameList):
    if((path.exists(localPath + "/" + fileNameList[0]) and path.exists(localPath + "/" + fileNameList[1])) == False):
        return False
        #ErrorHandling.errorBadFile()
    else:
        return True

#A3.3 - Changes LED to blue to signal recording has ended and processing will begin
def changeLEDtoBlue():
    LEDControl.turnBlue()
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
