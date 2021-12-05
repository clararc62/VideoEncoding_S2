
import os
from datetime import time
import subprocess
import numpy as np

class Exercises:
    # init method or constructor
    def __init__(self, ex):
        self.ex = ex

    def say_hi(self):
        print('You have selected exercise number', self.ex)

    def say_bye(self):
        print('Goodbye :)')

    def select_time(self):
        # ask to the user
        min = int(input("Which is the minute start?"))
        sec = int(input("Which is the sec start?"))

        # time(hour, minute and second)
        start_time = time(hour=0, minute=min, second=sec)


    def ex1(self, start_time):

        subprocess.call(
            ["ffmpeg", "-i", "BBB.mp4", "-ss", str(start_time), "-t",
             "00:00:12", "-async", "1", "-c", "copy", "BBB_cut.mp4"])

        mac = input(
            "Do you want to create the video that shows the macroblocks and motion vectors? [y/n]")

        if mac == "y":
            # show the macroblocks and the motion vectors
            os.system(
                "ffmpeg -flags2 +export_mvs -i BBB_cut.mp4 -vf codecview=mv=pf+bf+bb BBB_MBMV.mp4")
            print("Congratulations, you have created a new video")


    def ex2(self, start_time):
        # encode 1min of the video starting at the time specified by the user
        # Cut BBB into 1 minute only video.
        subprocess.call(
            ["ffmpeg", "-i", "BBB.mp4", "-ss", str(start_time), "-t",
             "00:01:00", "-async", "1", "-c", "copy", "BBB_1min.mp4"])

        # Export BBB(1min) audio as MP3 stereo track.
        subprocess.call(["ffmpeg", "-i", "BBB_1min.mp4", "-vn", "BBB_mp3.mp3"])

        # Export BBB(1min) audio in AAC w/ lower bitrate
        # now 64k is half of the resolution
        subprocess.call(
            ["ffmpeg", "-i", "BBB_1min.mp4", "-codec:a", "aac", "-b:a", "64k",
             "BBB_aac.aac"])

        # package everything in a .mp4
        subprocess.call(
            ["ffmpeg", "-i", "BBB_1min.mp4", "-i", "BBB_mp3.mp3", "-i",
             "BBB_aac.aac", "-map", "0:v", "-map", "1:a", "-map", "2:a", "-c",
             "copy", "container.mp4"])

    def ex3(self):
        video = str(input(
            "Write the name of the container that you are interested in, in quotes and the extension." "Example: 'container.mp4':"))
        # we pass the container information into text
        os.system(
            "ffprobe -v error -show_entries stream=index,codec_name,codec_type " + video + " >list.txt")

        # read the file
        with open('list.txt') as f:
            lines = f.readlines(0)

        # select the formats that the container has, and put them on a list
        arr = []
        for i in lines:
            if i.startswith("codec_name"):
                l = (len("codec_name"))
                arr.append(i[l + 1:-1])

        f.close()
        print("These are the extensions that the container has", arr)

        # conditions of the different broadcast standards

        DVB = ["mpeg2", "h264", "aac", "ac3", "mp3"]
        ISDB = ["mpeg2", "h264", "aac"]
        ATSC = ["mpeg2", "h264", "ac3"]
        DTMB = ["avs", "avs+", "mpeg2", "h264", "dra", "aac", "ac3", "mp2",
                "mp3"]

        BS = [DVB, ISDB, ATSC, DTMB]
        Names = ["DVB", "ISDB", "ATSC", "DTMB"]
        count = 0
        for i in range(len(BS)):
            # compare depending on the broadcast standard

            result = np.intersect1d(arr, BS[i])
            if len(result) == 0:
                count += 1
            if len(result) == len(arr):
                print("The %s is compatible!" % Names[i])

        if count == len(BS):
            print("Error, no broadcasting standard is compatible")

    def ex4(self):
        # select the video
        video = str(input(
            "Write the name of the video that you are interested in, in quotes and the extension." "Example: 'container.mp4':"))
        # create video with subtitles
        os.system(
            "ffmpeg -i " + video + " -vf subtitles=goteo.srt BBB_subtitle.mp4")



# user selects the exercise

num = int(input("Which exercise do you want to execute? (1,2,3,4)"))

while num>4 or num<1:
    print("Try again bro")
    num = int(input("Which exercise do you want to execute? (1,2,3,4)"))

n = Exercises(num)
n.say_hi()

if num==1:
    start_time = n.select_time()
    n.ex1(start_time)

elif num==2:
    start_time = n.select_time()
    n.ex2(start_time)

elif num ==3:
    n.ex3()

elif num ==4:
    n.ex4()

n.say_bye()