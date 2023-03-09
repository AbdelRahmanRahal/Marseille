# ————— LIBRARY AND MODULE CALLS —————
import speech_recognition as sr
import os, pyglet, pyttsx3, sys
from gingerit.gingerit import GingerIt
from gtts import gTTS
from mutagen.mp3 import MP3
from PIL import ImageTk, Image as PILImage
from pygame import init, mixer
from time import sleep
from tkinter import *


# ————— MAIN FUNCTION —————
def main():
	print(">>> Initiating Marseille...")
	GUI()

# ————— GUI WINDOW FUNCTION —————
def GUI():
	# ————— GUI WINDOW SETTINGS —————
	wndw = Tk()
	wndw.title("Marseille")
	wndw.geometry("500x500")
	wndw.iconbitmap("Media/rose.ico")
	wndw.configure(bg = "#F3F4FA")
	pyglet.font.add_file("Anaheim-Regular.ttf")

	# ————— TITLE AREA —————
	# ————— FRAME TO CONTAIN THE TITLE AND THE ICON —————
	titleFrame = Frame(wndw, bg = "#F3F4FA")

	# ————— ROSE ICON —————
	rose_icon = PILImage.open("Media/rose.png")
	rose_icon = rose_icon.resize((50, 50), PILImage.LANCZOS)
	rose_icon = ImageTk.PhotoImage(rose_icon)
	rose_panel = Label(
		master = titleFrame,
		image = rose_icon,
		bg = "#F3F4FA"
	)
	rose_panel.image = rose_icon

	# ————— MARSEILLE TITLE —————
	titlelabel = Label(
		master = titleFrame,
		text = "Marseille",
		font = ("Anaheim", 40, "bold"),
		fg = "#CB0025",
		bg = "#F3F4FA",
	)

	# ————— OUTPUT AREA —————
	# ————— FRAME TO CONTAIN THE OUTPUT TEXTBOX AND THE BUTTONS —————
	textboxFrame = Frame(wndw, bg = "#F3F4FA")

	# ————— TEXTBOX —————
	global textbox
	textbox = Entry(
		master = textboxFrame, #30 characters is the max amount of characters for this label at this font size
		font = ("Anaheim", 17),
		fg = "#700018",
		bg = "#E8D1D9",
		width = 30,
		justify = CENTER,
		bd = 0
	)
	textbox.config(highlightthickness = 0, highlightbackground = "#000793")

	# ————— BUTTON IMAGES —————
	# ————— SEND BUTTON IMAGES —————
	# ————— CLICKED SEND —————
	clicked_send = PILImage.open("Media/send_clicked.png")
	clicked_send = clicked_send.resize((40, 40), PILImage.LANCZOS)
	clicked_send = ImageTk.PhotoImage(clicked_send)
	# ————— DEFAULT MIC —————
	default_send = PILImage.open("Media/send_default.png")
	default_send = default_send.resize((30, 30), PILImage.LANCZOS)
	default_send = ImageTk.PhotoImage(default_send)

	# ————— MIC BUTTON IMAGES —————
	# ————— ACTIVE MIC —————
	active_mic = PILImage.open("Media/mic_active.png")
	active_mic = active_mic.resize((40, 40), PILImage.LANCZOS)
	active_mic = ImageTk.PhotoImage(active_mic)
	# ————— INACTIVE MIC —————
	inactive_mic = PILImage.open("Media/mic_inactive.png")
	inactive_mic = inactive_mic.resize((40, 40), PILImage.LANCZOS)
	inactive_mic = ImageTk.PhotoImage(inactive_mic)

	# ————— SEND BUTTON —————
	sendbutton = Label(
		master = textboxFrame,
		image = default_send,
		bg = "#F3F4FA"
	)
	sendbutton.bind("<Button-1>", lambda event: Mic_Press("Listening", micbutton, active_mic, inactive_mic))
	# ————— MIC BUTTON —————
	micbutton = Label(
		master = textboxFrame,
		image = inactive_mic,
		bg = "#F3F4FA"
	)
	micbutton.bind("<Button-1>", lambda event: Mic_Press("Listening", micbutton, active_mic, inactive_mic))

	# ————— GUI WINDOW INITIATION —————
	titleFrame.pack(pady = 45)
	rose_panel.pack(side = LEFT)
	titlelabel.pack(side = RIGHT)
	textboxFrame.pack()
	textbox.pack(ipady = 10, side= LEFT)
	micbutton.pack(pady = 20, side = RIGHT)
	sendbutton.pack(side = RIGHT)
	

	wndw.mainloop()

	return

# ————— SLEEP FUNCTION FOR TKINTER —————
def tksleep(self, time:float) -> None:
	self.after(int(time*1000), self.quit)
	self.mainloop()
Misc.tksleep = tksleep

# ————— MIC ANIMATION AND ACTIVATION FUNCTION —————
def Mic_Press(button_state, button, active_mic, inactive_mic):
	match button_state:
		case "Listening":
			button.configure(image = active_mic)
			button.image = active_mic
			textbox.tksleep(0.1)
			Output(Grammar_Check(Listen()))
			Mic_Press("default", button, active_mic, inactive_mic)
		case _:
			button.configure(image = inactive_mic)
			button.image = inactive_mic
	return

# ————— SPEECH RECOGNITION FUNCTION —————
def Listen():
	active = True
	recognizer = sr.Recognizer()

	# ————— VOICE-TO-TEXT CONVERTER —————
	while active:
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

# ————— CONVERTED TEXT OUTPUT FUNCTION —————
def Output(output_text):
	output_list = output_text.split()
	print(output_list)

	textbox.delete(0, END)
	for word in output_list:
		textbox.insert(END, word + " ")
		textbox.tksleep(0.1)
	return

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

# ————— GRAMMAR CORRECTION —————
def Grammar_Check(output_text):
	try:
		parser = GingerIt()
		corrected_text = parser.parse(output_text)

		return corrected_text["result"]

	except:
		Output("Sorry, I encountered an error.")
		textbox.tksleep(2)
		Output("Try again.")

		return 7

# ————— GET FULL PATH FUNCTION (NOT USED YET, BUT I SUSPECT I'LL HAVE TO USE IT LATER) —————
def Full_Path(relative_path):
	absolute_path = os.path.dirname(__file__)
	return os.path.join(absolute_path, relative_path)


# ————— PROGRAM INITIATION —————
if __name__ == "__main__":
	sys.exit(main())