
import subprocess
from datetime import time

#ask to the user
min = int(input("Which is the minute start?"))
sec=int(input("Which is the sec start?"))

# time(hour, minute and second)
start_time = time(hour = 0, minute = min, second = sec)

#encode 1min of the video starting at the time specified by the user
#Cut BBB into 1 minute only video.
subprocess.call(["ffmpeg", "-i", "BBB.mp4", "-ss", str(start_time), "-t", "00:01:00", "-async", "1", "-c", "copy" ,"BBB_1min.mp4"])

#Export BBB(1min) audio as MP3 stereo track.
subprocess.call(["ffmpeg", "-i" , "BBB_1min.mp4", "-vn", "BBB_mp3.mp3"])

#Export BBB(1min) audio in AAC w/ lower bitrate
#now 64k is half of the resolution
subprocess.call(["ffmpeg", "-i", "BBB_1min.mp4", "-codec:a" ,"aac", "-b:a", "64k", "BBB_aac.aac"])

#package everything in a .mp4
subprocess.call(["ffmpeg", "-i", "BBB_1min.mp4",  "-i", "BBB_mp3.mp3","-i", "BBB_aac.aac", "-map", "0:v", "-map", "1:a", "-map", "2:a", "-c", "copy", "container.mp4"])
