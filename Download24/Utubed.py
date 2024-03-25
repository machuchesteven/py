from pytube import YouTube, Playlist, YouTube
import tkinter as tk
import os
from pathlib import Path
import pytube
import pytube.request


pytube.request.default_range_size = 937184 # by default is 9MBs - 9437184, hence on progress only calls once per chunk

path_to_download = str(os.path.join(Path.home(), "Downloads", "Utubed"))


if not os.path.exists(path_to_download):
    os.mkdir(path_to_download)

download_statuses = ("Null", "Downloading", "Completed", "Failed", "Stopped")

status = download_statuses[0]
downloading_videos = 1

def on_completed_download(stream, chunk):
    print("Download completed")
    global status, download_statuses
    status = download_statuses[2]



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    download_status_label.config(text=f"{status} {downloading_videos}")
    print(f'{percentage_of_completion:0.2f}% downloaded')

src_url = ""
frist_url = 'https://youtube.com/shorts/IX1VWSictTE?si=uOEutyjN9igfOKw_'

def download_video():
    text = url_input_path.get()

    print(text)
    if text != "":
        vid_link = YouTube(text)
        video = vid_link.streams.get_highest_resolution()
        vid_link.register_on_progress_callback(on_progress)
        vid_link._age_restricted = False
        vid_link.register_on_complete_callback(on_completed_download)
        print(f"Video resolution: {video.resolution}")
        print(f"Video title: {video.title}")
        print(f"Video length: {vid_link.length} seconds")
        print(f"Video size {round(video.filesize * 0.000001, 2)} MB")
        text = url_input_path.delete(0, tk.END)
        video.download(path_to_download)
    else:
        print("Could not download video")
# for a specific resolution, you use filter with the specified download resolution
# eg Youtube(url).streams.filter(res="720p").first().download()

def download_playlist():
    text = url_input_path.get()
    print(text)
    if text != "":
        playlist = Playlist(text)
        for video in playlist.videos:
            video.streams.first().download()
    else:
        print("Could not download playlist")
    return 0

window = tk.Tk()

window.title = "Utubed Downloader"
indicate_label = tk.Label(window, text="Paste the video url below")
indicate_label.pack(padx=15, pady=10)
url_input_path = tk.Entry(window, textvariable=src_url)
url_input_path.pack(padx=15, pady=10)
button = tk.Button(window, text="Submit", command=download_video )
button.pack(padx=15, pady=10)
download_status_label = tk.Label(window, text=status)
download_status_label.pack(padx=15, pady=10)
window.mainloop()
