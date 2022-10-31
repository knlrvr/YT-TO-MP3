# import packages
from pytube import YouTube
import os

# url input
yt = YouTube (
    str(input("Enter URL: \n>> "))
)

# audio only 
video = yt.streams.filter(only_audio=True).first()

# save destination
print ("Enter the destination (blank for current directory)")
destination = str(input(">> ")) or '.'

# download file
out_file = video.download(output_path=destination)

# save file 
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

#result
print(yt.title + "has successfully downloaded")