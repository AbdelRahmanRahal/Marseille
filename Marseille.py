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
	wndw.configure(bg="#FDEBE6")

	# ————— WINDOW INITIATION —————
	wndw.mainloop()
	return 0

def Listen():
	recognizer = sr.Recognizer()

	while True:
		try:
			with sr.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration = 0.1)
				audio = recognizer.listen(mic)

				text = recognizer.recognize_google(audio)
				text = text.lower()

				return text
				
		except sr.UnknownValueError:
			print("Sorry, I didn't catch that.\n")
			recognizer = sr.Recognizer()
			continue

main()