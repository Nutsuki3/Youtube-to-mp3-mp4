import os
import pytube
import moviepy.editor as mp
from pytube.exceptions import VideoUnavailable

def Convertor(url, omp):
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(file_extension='mp4').first()
        filename = stream.default_filename
        stream.download()
        video = mp.VideoFileClip(filename)
        audio = video.audio    
        if omp == "-mp3":  
            audio.write_audiofile(os.path.splitext(filename)[0] + ".mp3")
            print(f"Download {omp[1:]} finished!")
            video.close()
            audio.close()
            os.remove(filename)
        elif omp == "-mp4":    
            print(f"Download {omp[1:]} finished!")
            video.close()
            audio.close()    
        else:
            audio.write_audiofile(os.path.splitext(filename)[0] + ".mp3")
            print("Download mp3, mp4 finished!")
            video.close()
            audio.close()
    except VideoUnavailable:
        print("Videno Not Found")

while True:
    info = input(">>> ")
    omp = info[0:4]
    url = info[5:]
    Convertor(url, omp)
