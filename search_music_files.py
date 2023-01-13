
# This code search music files in a given directory, including sub-directories

import os

path = "E:\המוזיקה שלי"


def find_files_and_subfolders(path):
    files = os.listdir(path)
    for item in files:
        if os.path.isdir(os.path.join(path, item)):
            find_files_and_subfolders(os.path.join(path, item))
        else:
            if item.endswith('.mp3'):
                # print(os.path.join(path, item)) #print path of file
                print(item) # print name of file


find_files_and_subfolders(path)