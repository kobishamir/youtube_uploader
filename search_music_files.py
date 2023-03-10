
# This code search music files in a given directory, including sub-directories
import google_auth_oauthlib.flow
import os
import argparse
import search_video
import playlist_updates
import playlist_serach

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
client_secrets_file = "client_secret.json"

# TODO: make application authorized only once - half way there
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
credentials = flow.run_console()

path = "E:\המוזיקה שלי"
youtube = playlist_updates.get_authenticated_service()

def createPlaylist(path):

    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            parser = argparse.ArgumentParser()
            parser.add_argument('--title',
                                default='%s' % dirname,
                                help='The title of the new playlist.')
            parser.add_argument('--description',
                                default='This Playlist based on the music folder at your local PC',
                                help='The description of the new playlist.')
            args = parser.parse_args()
            if dirname not in playlist_serach.main(credentials):
                playlist_updates.add_playlist(youtube, args)
                print('''playlist "%s" created''' % dirname)
        break

def find_files_and_subfolders(path):

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.mp3'):
                filename = filename.replace(".mp3", "")
                parser = argparse.ArgumentParser()
                parser.add_argument('--q', help='Search term', default='%s' % filename)
                parser.add_argument('--max-results', help='Max results', default=5)
                args = parser.parse_args()
                # Search for the music file on YouTube
                # video = search_video.youtube_search(args)[0]
                print("the video for: " + filename + "is:")
                # print(video)
                # TODO: add function to find Jaro Distance using jellyfish library
                # if video is not None:
                #     # Get the name of the directory
                #     playlist_name = os.path.basename(dirpath)
                #     # Create a new playlist if it doesn't exist
                #     if playlist_name not in playlists:
                #         playlists[playlist_name] = create_playlist(playlist_name)
                #     # Add the video to the playlist
                #     add_to_playlist(playlists[playlist_name], video)


if __name__ == "__main__":
    createPlaylist(path)
    find_files_and_subfolders(path)