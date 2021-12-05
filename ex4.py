
import os

#select the video
video = str(input("Write the name of the video that you are interested in, in quotes and the extension." "Example: 'container.mp4':" ))

#create video with subtitles
os.system("ffmpeg -i " +video+ " -vf subtitles=goteo.srt mysubtitledmovie.mp4")