from pytube import YouTube
import os

url=input("Enter the URL for the video: ")
format=input("video or audio? (answer with video/audio) ")
yt=YouTube(url)

print("title:",yt.title)
print("views:",yt.views)
if(format=='audio'):
    video = yt.streams.filter(only_audio=True).first()
    #replace file path with your one
    #downloaded_file = video.download('filepath')
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
elif(format=='video'):
    yd = yt.streams.get_highest_resolution()
    #replace file path with your one
    #yd.download('filepath')


