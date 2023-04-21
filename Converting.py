import os
from pytube import YouTube
import moviepy.editor as mp

yt_link = input("Enter the YouTube link you want to convert: ")
yt = YouTube(yt_link)


stream = yt.streams.first()
stream.download()


video = mp.VideoFileClip(f"{yt.title}.mp4")
audio = video.audio
audio.write_audiofile(f"{yt.title}.mp3")


video.close()
audio.close()
os.remove(f"{yt.title}.mp4")

