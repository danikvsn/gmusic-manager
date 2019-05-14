# coding=utf-8

import os
from pprint import pprint
import mutagen
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC


def read_library():
    library_dir = input("Enter Library Location: ")
    for entry in os.listdir(library_dir):
        print(entry)


def find_favorites(music_dir):
    favorite_tracks = []
    for entry in os.listdir(music_dir):
        if os.path.isdir(entry):
            favorite_tracks.extend(find_favorites(entry))
        else:
            print(mutagen.File(music_dir + '\\' + entry))

# def filetype_analysis(music_dir):


# find_favorites("D:\\Music")

audio = MP3(u'/mnt/d/Music/Хатхур зу/Яда/Хатхур Зу - Уги Няс (Prod by LG).mp3')
tag = ID3(u'/mnt/d/Music/Хатхур зу/Яда/Хатхур Зу - Уги Няс (Prod by LG).mp3')

print(audio.tags['TIT2'])
print(audio.tags['TPE2'])
print(audio.tags['TALB'])
print(tag.getall("POPM"))

print()
