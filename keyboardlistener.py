import speech_rec as speech_rec
import keyboard
import string
from threading import *
from playsound import playsound


'''
Created on 2012. 2. 19.
This module is for playing mp3 (limited) and wav formatted audio file
@author: John
'''
import pygame

def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
       This will load the whole sound into memory before playback
    """    
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(1000)

def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)
        

def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
	BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
	FREQ, SIZE, CHAN = getmixerargs()
	pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)


'''You definitely need test mp3 file (a.mp3 in example) in a directory, say under 'C:\\Temp'
   * To play wav format file instead of mp3, 
      1) replace a.mp3 file with it, say 'a.wav'
      2) In try except clause below replace "playmusic()" with "playsound()"
	
'''

def play_song(filename):
    initMixer()
    playmusic(filename)


def start_speech_rec():
    global filename
    command = speech_rec.return_voice()
    if ('motivational song' in str(command).lower()):
        print('playing motivational songs!')
        play_song('./motivational.mp3')
        
    if ('chill song' in str(command).lower()):
        print('playing chill song')
        play_song('./chill.mp3')



# I can't find a complete list of keyboard keys, so this will have to do:
keys = list(string.ascii_lowercase)
keys.append("print_screen")
keys.append('insert')
def listen(key):
    while True:
        keyboard.wait(key)
        if(key == 'print_screen'):
            play_song('beep.mp3')
            start_speech_rec()
        if(key == 'insert'):
            stopmusic()

        print("[+] Pressed", key)


threads = [Thread(target=listen, kwargs={"key": key}) for key in keys]
for thread in threads:
    thread.start()
