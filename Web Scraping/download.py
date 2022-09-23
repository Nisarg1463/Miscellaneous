from time import sleep
import time
import pytube
from pytube import YouTube
import re
import os
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import threading

start = time.time()


def download_mp3(query):
    id = pytube.Search(query).results[0].video_id
    base_url = "https://www.youtube.com/watch?v="
    url = f"{base_url}{id}"
    yt = YouTube(url)
    status = yt.vid_info["playabilityStatus"]["status"]
    if status == "UNPLAYABLE":
        print(f"Song name: {query} is not playable, cannot download.")
        return

    try:
        isinstance(yt.length, int)
    except:
        print(f"Could not get video length for {query}. Skipping download.")
        return

    # create condition - if the yt.length > 600 (10 mins), then don't download it
    if yt.length > 600:
        print(f"Song name: {query} is longer than 10 minutes, will not download.")
        return

    video = yt.streams.filter(only_audio=True).first()

    try:
        song_title_raw = yt.title
    except:
        print(f"Unable to get title for id {id}. Skipping download.")
        return
    song_title = re.sub("\W+", " ", song_title_raw).lower().strip()
    song_path = f"{song_title}"

    download_path = f"saved_mp3s/{song_path}"
    out_file = video.download(download_path)

    # save the file (which will be mp4 format)
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp3"
    count = 0
    while True:
        try:
            count += 1
            print(count)
            os.rename(
                out_file, new_file,
            )
            out_file = new_file
            # move the mp3 to the root dir
            p = Path(new_file).absolute()
            parent_dir = p.parents[1]
            p.rename(parent_dir / p.name)
            break
        except FileExistsError:
            base, _ = os.path.splitext(new_file)
            new_file = f"{base}[{count}]" + ".mp3"
        # except FileNotFoundError:
        #     base, _ = os.path.splitext(new_file)
        #     new_file = f"{base}[{count}]" + ".mp3"

    # delete the child dir
    os.rmdir(download_path)

    # rename the mp3 to remove the bad chars
    source_name = f"saved_mp3s/{song_title_raw}.mp3"
    dest_name = f"saved_mp3s/{song_path}.mp3"
    try:
        os.rename(source_name, dest_name)
    except:
        print(f"Failed to rename the file: {song_title_raw}")

    # result of success
    print(f"{song_path} has been successfully downloaded. Song name: {query}")


env = dict(os.environ)

api_creds = {
    "SPOTIPY_CLIENT_ID": "Your-client-id",
    "SPOTIPY_CLIENT_SECRET": "your-client-secret",
    "GENIUS_ACCESS_TOKEN": "access-token",
}

os.environ.update(api_creds)

# playlist_id = "4Axpteo8oGeDIqMffURnoE"
playlist_id = "2rozMxDmkgGVofpHwHNcrW"

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

res = sp.playlist_items(playlist_id)
total = res["total"]
offset = 0
tracks = []
sets = []
while True:
    for i in range(len(res["items"])):
        artists = []

        for j in range(len(res["items"][i]["track"]["album"]["artists"])):
            artists.append(res["items"][i]["track"]["album"]["artists"][j]["name"])
        sets.append(
            [
                res["items"][i]["track"]["name"],
                artists,
                res["items"][i]["track"]["album"]["name"],
            ]
        )
        if len(sets) % 5 == 0:
            tracks.append(sets)
            sets = []
    total -= len(res["items"])
    offset += len(res["items"])
    if total <= 0:
        break
    if total > 100:
        limit = 100
    else:
        limit = total
    res = sp.playlist_items(playlist_id, offset=offset, limit=limit)

for sets in tracks:
    threads = []
    for track in sets:
        threads.append(
            threading.Thread(target=download_mp3, args=(f"{track[0]} {track[2]}",))
        )
        threads[-1].start()
    sleep(20)

threads[-1].join()
print(time.time() - start)

