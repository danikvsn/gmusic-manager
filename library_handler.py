# coding=utf-8

import os
from pprint import pprint
import mutagen
from mutagen.id3 import ID3
from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.flac import FLAC


def read_library():
    library_dir = input("Enter Library Location: ")
    for entry in os.listdir(library_dir):
        print(entry)


def find_favorites(music_dir):
    favorite_tracks = []
    for entry in os.listdir(music_dir):
        entry_path = music_dir + '/' + entry
        # print("============= Current Path", entry_path)
        if os.path.isdir(entry_path):
            favorite_tracks.extend(find_favorites(entry_path))
        else:
            if os.path.splitext(entry)[1].lower() == ".mp3":
                try:
                    audio = MP3(entry_path)
                    id3tag = ID3(entry_path)
                    # if 'TIT2' in audio.tags:
                    #     print(audio.tags['TIT2'])
                    # if 'TPE1' in audio.tags:
                    #  print(audio.tags['TPE1'])
                    # if 'TPE2'in audio.tags:
                    #     print(audio.tags['TPE2'])
                    # if 'TALB' in audio.tags:
                    #     print(audio.tags['TALB'])
                    # if 'TRCK' in audio.tags:
                    #     print(audio.tags['TRCK'])
                    rating_arr = id3tag.getall("POPM")
                    if len(rating_arr) > 0:
                        if rating_arr[0].rating == 255:
                            fav_entry = [entry_path, 'mp3', audio.tags]
                            favorite_tracks.append(fav_entry)
                except HeaderNotFoundError:
                    print('Error Handling ' + entry_path)

            elif os.path.splitext(entry)[1].lower() == ".flac":
                audio = FLAC(entry_path)
                if 'RATING' in audio.tags:
                    if audio.tags['RATING'] == ['100']:
                        fav_entry = [entry_path, 'flac', audio.tags]
                        favorite_tracks.append(fav_entry)
    return favorite_tracks





# def filetype_analysis(music_dir):

fav_tracks = find_favorites("/mnt/d/Music")

for entry in fav_tracks:
    print(entry[0])

# audio = MP3(u'/mnt/d/Music/Хатхур зу/Яда/Хатхур Зу - Уги Няс (Prod by LG).mp3')
# tag = ID3(u'/mnt/d/Music/Хатхур зу/Яда/Хатхур Зу - Уги Няс (Prod by LG).mp3')
#
# print(audio.tags['TIT2'])
# print(audio.tags['TPE1'])
# print(audio.tags['TPE2'])
# print(audio.tags['TALB'])
# print(audio.tags['TRCK'])
# print(tag.getall("POPM"))

# audio = FLAC('/mnt/d/Music/6ix9ine/6IX9INE - DUMMY BOY [2018] [WEB FLAC]/02 FEFE (feat. Nicki Minaj Murda Beatz).flac')
# for entry in audio.tags:
#     print(entry)