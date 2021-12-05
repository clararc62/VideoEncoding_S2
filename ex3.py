import subprocess
import os
import struct
import numpy as np

video = str(input("Write the name of the container that you are interested in, in quotes and the extension." "Example: 'container.mp4':" ))
#we pass the container information into text
os.system("ffprobe -v error -show_entries stream=index,codec_name,codec_type " + video + " >list.txt")


#read the file
with open('list.txt') as f:
    lines = f.readlines(0)

#select the formats that the container has, and put them on a list
arr = []
for i in lines:
    if i.startswith("codec_name"):
        l=(len("codec_name"))
        arr.append(i[l+1:-1])

f.close()
print("These are the extensions that the container has", arr)


#conditions of the different broadcast standards

DVB = ["mpeg2", "h264", "aac","ac3", "mp3"]
ISDB = ["mpeg2", "h264", "aac"]
ATSC = ["mpeg2", "h264", "ac3"]
DTMB = ["avs", "avs+", "mpeg2", "h264", "dra", "aac", "ac3", "mp2", "mp3"]

BS = [DVB, ISDB, ATSC, DTMB]
Names = ["DVB", "ISDB", "ATSC", "DTMB"]

count = 0
for i in range(len(BS)):
    #compare depending on the broadcast standard

    result = np.intersect1d(arr,BS[i])
    if len(result) == 0:
        count+=1
    if len(result) == len(arr):
        print("The %s is compatible!"%Names[i])

if count == len(BS):
    print("Error, no broadcasting standard is compatible")