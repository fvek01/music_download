from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC

def give_properties(file, song, artist, tracknumber, tracks, album, albumartist, year):
    audio = EasyID3(file)

    audio['artist'] = artist
    audio['title'] = song
    audio['tracknumber'] = f'{tracknumber}/{tracks}'
    audio['album'] = album
    audio['date'] = year
    audio['albumartist'] = albumartist
    audio.save()

    audio = ID3(file)
    with open('album_art.jpg', 'rb') as albumart:
        audio['APIC'] = APIC(
                          encoding=3,
                          mime='image/jpeg',
                          type=3, desc=u'Cover',
                          data=albumart.read()
                        )            
    audio.save()
    