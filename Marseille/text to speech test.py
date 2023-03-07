import os
from gtts import gTTS
from mutagen.mp3 import MP3
import pygame, time

mytext = "Hi! How are you?"
language = "en"
myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save("Hello.mp3")
audio = MP3("Hello.mp3")
print(audio.info.length)
pygame.init()
pygame.mixer.music.load("Hello.mp3")
pygame.mixer.music.play()
time.sleep(audio.info.length + 1)
pygame.mixer.music.fadeout(audio.info.length + 1)

# music = pyglet.resource.media("Hello.mp3")
# music.play()
# pyglet.app.run(STOP())


# pyglet.app.event_loop.sleep(2)
# os.popen("mpg321 Hello.mp3", "w")