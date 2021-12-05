import os
import subprocess
from datetime import time


# ask to the user
min = int(input("Which is the minute start?"))
sec = int(input("Which is the sec start?"))

# time(hour, minute and second)
start_time = time(hour=0, minute=min, second=sec)

#encode 12 seconds of the video starting at the time specified by the user
subprocess.call(["ffmpeg", "-i", "BBB.mp4", "-ss", str(start_time), "-t", "00:00:12", "-async", "1", "-c", "copy" ,"BBB_cut.mp4"])

mac = input("Do you want to create the video that shows the macroblocks and motion vectors? [y/n]")

if mac == "y":
    # show the macroblocks and the motion vectors
    os.system("ffmpeg -flags2 +export_mvs -i BBB_cut.mp4 -vf codecview=mv=pf+bf+bb BBB_MBMV.mp4")
    print("Congratulations, you have created a new video")

else:
    print("goodbye!")


