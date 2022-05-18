from pygame import mixer
import os,random
mixer.init()
#here put your music folder path
songs_dir='F:/music/new/'
songs= os.listdir(songs_dir)
#sort songs in ascending order
songs=sorted(songs)
current_song_index=0
print(songs[current_song_index])
# rd= random.choice(songs)
# print(rd)

def next_song(song_index):
    if song_index >len(songs):
        song_index=0
    song_index=song_index+1
    # print(song_index)
    print(songs[song_index])
    mixer.music.load(songs_dir+songs[song_index])
    mixer.music.play()
    return song_index

def previous_song(song_index):
    if song_index==0:
        song_index=len(songs)
    song_index=song_index-1
    # print(song_index)

    print(songs[song_index])
    mixer.music.load(songs_dir+songs[song_index])
    mixer.music.play()
    return song_index


def up_volume():
    current_vol=mixer.music.get_volume()
    current_vol=current_vol +0.1
    if current_vol >= 1.0:
        current_vol=1.0
    mixer.music.set_volume(current_vol)


def down_volume():
    current_vol=mixer.music.get_volume()
    current_vol=current_vol -0.1
    if current_vol < 0.06:
        current_vol=0
    # print(current_vol)
    mixer.music.set_volume(current_vol)

def mute():
    mixer.music.set_volume(0)

mixer.music.load(songs_dir+songs[current_song_index])
mixer.music.play()

# print(mixer.music.get_volume())
while True:
    print("""\n
    Press 'n' : for next song \n
    Press 'p' : for Previous song \n 
    Press 's' : for Stop current song \n 
    Press 'unstop' : for play current song \n 
    Press 'u' : for volume up \n
    Press 'd' : for volume down \n 
    Press 'e' : for exit
    """)
    a=input(">")
    if a=='stop':
        mixer.music.pause()
    # next song
    elif a=='n':
        current_song_index= next_song(current_song_index)

    # previous song
    elif a=='p':
        current_song_index=previous_song(current_song_index)

    elif a=='unstop':
        mixer.music.unpause()
    
    elif a=='u':
        up_volume()
        
    elif a=='d':
        down_volume()
    elif a=='e':
        exit()
