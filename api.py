import lyricsgenius as lg
import re
import os

token = "ybsd5TsGZ-xJbwlbaQ6iHpB-b92qbdPJHlKYBgsr5x0Ugq7RdbDSrhb057ngOJ3S"

genius = lg.Genius(token)

def get_lyrics(song_name):
    lyrics = genius.search_song(song_name)
    lyrics = re.sub('\\[.+?\\]','',lyrics)
    lyrics = clean_lyrics(lyrics)
    return lyrics

audio_root = "."

for fname in os.listdir(audio_root):
    # look for dirs that don't start with a dot
    if not os.path.isdir(fname) or fname[0]=='.':
        continue
    genre = fname
    print("GENRE: "+genre)
    for fname in os.listdir(audio_root+"/"+genre):
        print(fname)