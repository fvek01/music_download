from pytube import YouTube
from pytube import Playlist
import re
import os
import getinfo
import giveprops
import yt_dlp as youtube_dl
import json


playlist = Playlist(input(str("Enter Playlist Url:\n")))

album_name = input(str("Enter Album Name (or leave blank to use playlist name):\n"))

if album_name == '':
    album_name = playlist.title

artist_name = input(str("Enter Artist Name:\n"))

# fixes some shit
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

vid_urls = playlist.video_urls

print(len(vid_urls))

getinfo.get_album_info(album_name, artist_name, str(len(vid_urls)))

# get information
f = open("info.json")
j = json.load(f)

albumartists = []
temp = j["releases"][0]["artist-credit"]
for artist in temp:
    albumartists.append(artist["name"])
album = j["releases"][0]["title"]
year = (j["releases"][0]["date"])[:4]
genre = ''
try:
    temp = j["releases"][0]["tags"] 
    for g in temp:
        tag = g["name"]
        genre += f'{tag}|'
    genres = genre[:-1]
except:
    print("No genres found")
    

path = os.getcwd() + "/" + album

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': path + '/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

f = open("inforec.json")
j = json.load(f)

tracknumber = 0

for url in vid_urls:
    songname = j["recordings"][tracknumber]["title"]
    artists = []
    temp = j["recordings"][tracknumber]["artist-credit"]
    for artist in temp:
        artists.append(artist["name"])


    tracknumber += 1
    title = YouTube(url).title
    file = path + '/' + title + '.mp3'
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    giveprops.give_properties(file, title, artists, str(tracknumber), str(len(vid_urls)), album, albumartists, year)

        

    #giveprops.give_properties(path + '//' + video.title + '.mp3', 'album_art.jpg')