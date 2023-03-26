# ————— LIBRARY AND MODULE CALLS —————
import speech_recognition as sr
import os, sys
from gtts import gTTS
from mutagen.mp3 import MP3
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Cancels the pygame welcome message, sorry it was getting on my nerves :(
from pygame import init, mixer
from time import sleep
from GUI import *


# ————— MAIN FUNCTION —————
def main():
	print(">>> Initialising Marseille...")
	GUI_Initiation()

	return

# ————— SPEECH RECOGNITION FUNCTION —————
def Listen():
	active = True
	recognizer = sr.Recognizer()

	# ————— VOICE-TO-TEXT CONVERTER —————
	while active:
		print(">>> Taking voice input...")
		try:
			with sr.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration = 0.1)
				audio = recognizer.listen(mic)
				converted_text = recognizer.recognize_google(audio)

				if converted_text != [] or "":
					active = False
					return converted_text

		# ————— REDO THE FUNCTION WHEN IT GETS UNRECOGNISED INPUT —————
		except sr.UnknownValueError:
			Output("Sorry, I didn't catch that.")
			recognizer = sr.Recognizer()
			continue

# ————— CONVERT REPLY TTS —————
def TTS_Output(reply_text, tts_language):
	reply_mp3 = gTTS(text = reply_text, lang = tts_language, slow = False)
	reply_mp3.save("Media/TTS.mp3")
	converted_audio = MP3("Media/TTS.mp3")

	# ————— AUDIO INITIATION —————
	init()
	mixer.music.load("Media/TTS.mp3")
	mixer.music.play()
	sleep(int(converted_audio.info.length + 1))
	mixer.music.fadeout(1)

# ————— GET FULL PATH FUNCTION (NOT USED YET, BUT I SUSPECT I'LL HAVE TO USE IT LATER) —————
def Full_Path(relative_path):
	absolute_path = os.path.dirname(__file__)
	return os.path.join(absolute_path, relative_path)


# ————— PROGRAM INITIATION —————
if __name__ == "__main__":
	sys.exit(main())