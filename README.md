# Youtube Album Downloader

Downloads albums from a youtbe playlist in mp3 format. Gives the tracks metadata related to the album automatically using the MusicBrainz API. This includes album images.

Probably some stuff in the requirements that isn't needed. You will also need ffmpeg for yt_dlp but you may be able to use abother tool and change the ydl_opts just check with the docs for youtube-dl.

## TO-DO

- make it not break when songs have special characters
- Verify Track Titles and rename accordingly
- Fill out rest of track information
- Implement album lookup using youtube api so you don't have to find url
- Get options to download individual songs
- Look into other sources for audio
- Reduce the amount of requests sent out to make the proccess faster
- GUI???