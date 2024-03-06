import requests
from bs4 import BeautifulSoup
import json

def get_album_info(album, artist, tracks):
    url = f'https://musicbrainz.org/search?query="{album}"+AND+artist%3A{artist}+AND+tracks%3A{tracks}&type=release&limit=25&method=advanced'

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        if link.get('href').startswith("/release/") and link.get('href').endswith("/cover-art"):
            urls.append(link.get('href'))

    running = True

    for link in urls:
        try:
            reid = link[9:][:-10]
            r = requests.get("https://coverartarchive.org" + link[:-10])
            j = r.json()
            image = j["images"][0]["image"]
            break
        except:
            print("No cover art found")

    # download the cover
    img_data = requests.get(image).content
    with open('album_art.jpg', 'wb') as handler:
        handler.write(img_data)

    # download album info
    
    r = requests.get("https://musicbrainz.org/ws/2/release/?query=reid:"+reid+"&fmt=json")
    j = r.json()

    with open('info.json', 'w') as f:
        json.dump(j, f)

    print('Release info downloaded')
    
    # download songs info
    
    r = requests.get("https://musicbrainz.org/ws/2/recording/?query=reid:"+reid+"&fmt=json")
    j = r.json()

    with open('inforec.json', 'w') as f:
        json.dump(j, f)

    print('Recording info downloaded')
    