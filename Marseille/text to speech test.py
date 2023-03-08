import os
from gtts import gTTS
from mutagen.mp3 import MP3
from pygame import init, mixer
from time import sleep

reply_text = "Hello world!"
tts_language = "en"
reply_mp3 = gTTS(text = reply_text, lang = tts_language, slow = False)

reply_mp3.save("Media/TTS.mp3")
converted_audio = MP3("Media/TTS.mp3")
print(converted_audio.info.length)
init()
mixer.music.load("Media/TTS.mp3")
mixer.music.play()
sleep(int(converted_audio.info.length + 1))
mixer.music.fadeout(1)