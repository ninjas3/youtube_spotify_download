from fileinput import filename
import random, os, re, glob
from timeit import repeat
from unicodedata import name
from pytube import YouTube
import youtube_dl
from pytube import Playlist
import moviepy.editor as mp 
from typer import Typer

#song information
import eyed3.id3
from eyed3.id3 import Tag
from eyed3.id3.frames import ImageFrame
from PIL import Image

#thumbnail
import pafy


#------------------------------
# Youtube-Video(360p)
#------------------------------
def download_360p_mp4_videos(url: str, outpath: str = "./"):

    yt = YouTube(url)

    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)


# if __name__ == "__main__":

    # download_360p_mp4_videos(
    #     "https://www.youtube.com/watch?v=szQr7rhEwyE",
    #     "./biology presentation",
    # )


#------------------------------
# Youtube-Audio(Playlist)
#------------------------------

def download():
    global url
    global folder
    global playlist 

    url = input("Add playlist: ")
    folder = input("Add folder: ")

    playlist = Playlist(url)

    #prints each video url, which is the same as iterating through playlist.video_urls
    for url in playlist:
        print(url)
    #prints address of each YouTube object in the playlist
    for vid in playlist.videos:
        print(vid)
    for url in playlist:
        YouTube(url).streams.filter(only_audio=True).first().download(folder)
    
        
    # for url in playlist:
    #     YouTube(url).streams.first().download("./test")
   
    # global file
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

download()

# "https://www.youtube.com/playlist?list=PL9z83dt87nBUz5T9_ZtH71eVhID6JYSqD"
# "./test"


def rename():
    file = folder + "/" + input("song file: ")
    audiofile = eyed3.load(file)
                
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.title = u"fuck"
    audiofile.tag.album = u'fucking'
    audiofile.tag.artist = u'NQ'
    audiofile.tag.images.set(3, open("pics/amadeus.jpg", 'rb').read(), 'image/jpeg')
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

rename()

def thumbnail():
    # web = "https://www.youtube.com/watch?v=IJbBOANg8CQ&list=PL9z83dt87nBUz5T9_ZtH71eVhID6JYSqD&index=1"
    # getting video
    video = pafy.new(url) 
    
    # getting thumbnail of the video
    value = video.thumb
    print("url: "+ value)

thumbnail()

