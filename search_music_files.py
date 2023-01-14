
# This code search music files in a given directory, including sub-directories

import os
import subprocess

path = "E:\המוזיקה שלי"

def find_files_and_subfolders(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.mp3'):
                # Search for the music file on YouTube
                # video = search_video(filename)
                print(filename)
                video = subprocess.run(["python", "search_video.py", "filename"])
                if video is not None:
                    # Get the name of the directory
                    playlist_name = os.path.basename(dirpath)
                    # Create a new playlist if it doesn't exist
                    if playlist_name not in playlists:
                        playlists[playlist_name] = create_playlist(playlist_name)
                    # Add the video to the playlist
                    add_to_playlist(playlists[playlist_name], video)


find_files_and_subfolders(path)