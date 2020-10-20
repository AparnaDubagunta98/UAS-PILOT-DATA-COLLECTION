#A4 Processing.py
#Function Definitions:
#  4.1 Sync with ffmpeg
#  4.2 Verify synced on SD
#  4.3 Export (3 files)
#      Copy of Error Log
import os
import time
import datetime
import pathlib
import subprocess
import ErrorHandling


#path for USB drive
usbPath = "/media/pi/VIDEOS"

#path for local storage -- SD card
localPath = "/home/pi/localVids"
timeStamp = ""


#Helper Function for A4.1
def getVideoLength(videoFile):
	result = subprocess.run(["sudo ffprobe", "-v", "error", "-show_entries",
	                     "format=duration", "-of",
	                     "default=noprint_wrappers=1:nokey=1", videoFile],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	return float(result.stdout)

#A4.1
def sychronizeVideos(fileNameList, duration):
    try:
    	# create merged file
    	fastMerged = timeStamp + "fastMerged.mp4"
    	# use filter complex and stack videos side by side
        os.system("sudo ffmpeg -i " + localPath + "/" + fileNameList[0] + " -i "+ localPath + "/" + fileNameList[1] + " -filter_complex \"[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w\" " + fastMerged)
    except:
    	ErrorHandling.errorBadFile()

    # if merging & synching happens properly, continue to slow and adjust video
    try:
    	#final merged file to be exported and used
    	mergedVideo = timeStamp + "merged.mp4"
		fileNameList.append(mergedVideo)

        # slow video down
        vidLength = getVideoLength(fastMerged)
        ### test with diff formula ###
        slowingFactor = duration/vidLength
        os.system("sudo ffmpeg -i " + localPath + "/" + fastMerged + " -vf setpts=" + str(slowingFactor) + "*PTS " + localPath + "/" + fileNameList[2])
        os.system("sudo rm "+ localPath + "/" + fastMerged)
    except:
        ErrorHandling.errorBadSynch()

#A4.2
# check if synched video is on SD card
def verifySynchedVideos(fileNameList):
    return (path.exists(localPath + "/" + fileNameList[2]))

#A4.3
def exportVideos(fileNameList):
	dest_path = usbPath
	# errorLog = error log path  #,errorLog]
	try:
		if(path.exists(dest_path) == False):
			os.makedirs(dest_path)

		for f in filesNameList:
    		shutil.copy(f, dest_path)
	except:
		ErrorHandling.errorUSBStorage()



## Main ##
ts = time.time()
timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
sychronizeVideos(fileNameList,duration)
verifySynchedVideos(fileNameList)
exportVideos(fileNameList)
