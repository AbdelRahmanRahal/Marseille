import speech_recognition as sr
import pyttsx3
from tkinter import *

def main():
	print(">>> Initiating Marseille...")
	GUI()

# ————— GUI WINDOW FUNCTION —————
def GUI():
	wndw = Tk()
	wndw.title("Marseille")
	wndw.geometry("500x500")
	wndw.iconbitmap("rose.ico")
	wndw.configure(bg="#EFF1FF")


	# ————— WINDOW INITIATION —————
	wndw.mainloop()
	return 0

def Listen():

	active = True
	recognizer = sr.Recognizer()

	while active:
		try:
			with sr.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration=0.1)
				audio = recognizer.listen(mic)

				text = recognizer.recognize_google(audio)

				if text != []:
					active = False
					return text

		except sr.UnknownValueError:
			print("Sorry, I didn't catch that.\n")
			recognizer = sr.Recognizer()
			continue

if __name__ == "__main__":
    exit(main())