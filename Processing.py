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
usbPath = "/home/pi/VIDEOS"

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
def sychronizeVideos(FaceCamVideo, TabletCamVideo, duration):
    try:
    	# create merged file
    	fastMerged = timeStamp + "fastMerged.mp4"
    	# use filter complex and stack videos side by side
        os.system("sudo ffmpeg -i " + localPath + "/" + FaceCamVideo + " -i "+ localPath + "/" + TabletCamVideo + " -filter_complex \"[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w\" " + fastMerged)
    except:
    	ErrorHandling.errorBadFile()

    # if merging & synching happens properly, continue to slow and adjust video
    try:
    	#final merged file to be exported and used
    	mergedFileName = timeStamp + "merged.mp4"
        # slow video down
        vidLength = getVideoLength(fastMerged)
        ### test with diff formula ###
        slowingFactor = duration/vidLength
        os.system("sudo ffmpeg -i " + localPath + "/" + fastMerged + " -vf setpts=" + str(slowingFactor) + "*PTS " + localPath + "/" + mergedFileName)
        os.system("sudo rm "+ localPath + "/" + fastMerged)
        return mergedFileName
    except:
        ErrorHandling.errorBadSynch()

#A4.2
# check if synched video is on SD card
def verifySynchedVideos(mergedFileName):
    return (path.exists(localPath + "/" + mergedFileName))

#A4.3
def exportVideos(FaceCamVideo,TabletCamVideo,mergedFileName):
	dest_path = usbPath
	# errorLog = error log path
	filesToBeCopied = [FaceCamVideo,TabletCamVideo,mergedFileName]  #,errorLog]
	try:
		if(path.exists(dest_path) == False):
			os.makedirs(dest_path)

		for f in filesToBeCopied:
    		shutil.copy(f, dest_path)
	except:
		ErrorHandling.errorUSBStorage()



## Main ##
ts = time.time()
timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
mergedFileName = sychronizeVideos(FaceCamVideo,TabletCamVideo,duration)
verifySynchedVideos(mergedFileName)
exportVideos(FaceCamVideo,TabletCamVideo,mergedFileName)
