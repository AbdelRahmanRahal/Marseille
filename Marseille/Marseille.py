# ————— LIBRARY AND MODULE CALLS —————
import speech_recognition as sr
import os, pyglet, pyttsx3, sys
from gingerit.gingerit import GingerIt
from gtts import gTTS
from mutagen.mp3 import MP3
from PIL import ImageTk, Image as PIL_Image
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Cancels the pygame welcome message, sorry it was getting on my nerves :(
from pygame import init, mixer
from time import sleep
from tkinter import *


# ————— MAIN FUNCTION —————
def main():
	print(">>> Initialising Marseille...")
	GUI()

# ————— GUI WINDOW FUNCTION —————
def GUI():
	# ————— GUI WINDOW SETTINGS —————
	wndw = Tk()
	wndw.title("Marseille")
	wndw.geometry("600x400")
	wndw.iconbitmap("Media/rose.ico")
	wndw.configure(bg = "#F3F4FA")
	pyglet.font.add_file("Media/Anaheim-Regular.ttf")

	# ————— TITLE AREA —————
	# ————— FRAME TO CONTAIN THE TITLE AND THE ICON —————
	titleframe = Frame(wndw, bg = "#F3F4FA")

	# ————— ROSE ICON —————
	rose_icon = PIL_Image.open("Media/rose.png")
	rose_icon = rose_icon.resize((50, 50), PIL_Image.LANCZOS)
	rose_icon = ImageTk.PhotoImage(rose_icon)
	rose_panel = Label(
		master = titleframe,
		image = rose_icon,
		bg = "#F3F4FA"
	)
	rose_panel.image = rose_icon

	# ————— MARSEILLE TITLE —————
	titlelabel = Label(
		master = titleframe,
		text = "Marseille",
		font = ("Anaheim", 40, "bold"),
		fg = "#CB0025",
		bg = "#F3F4FA",
	)

	# ————— OUTPUT AREA —————
	# ————— FRAME TO CONTAIN THE OUTPUT TEXTBOX AND THE BUTTONS —————
	textboxframe = Frame(wndw, bg = "#F3F4FA")

	# ————— TEXTBOX —————
	global textbox
	textbox = Text(
		master = textboxframe, #27 characters is the max amount of characters for this label at this font size
		font = ("Anaheim", 17),
		fg = "#700018",
		bg = "#E8D1D9",
		width = 29,
		height = 1,
		wrap = WORD,
		# justify = LEFT,
		bd = 9,
		relief = FLAT
	)
	textbox.config(insertbackground = "#700018")

	# ————— BUTTON IMAGES —————
	# ————— SEND BUTTON IMAGES —————
	# ————— CLICKED SEND —————
	GUI.clicked_send = PIL_Image.open("Media/send_clicked.png")
	GUI.clicked_send = GUI.clicked_send.resize((30, 30), PIL_Image.LANCZOS)
	GUI.clicked_send = ImageTk.PhotoImage(GUI.clicked_send)
	# ————— DEFAULT MIC —————
	GUI.default_send = PIL_Image.open("Media/send_default.png")
	GUI.default_send = GUI.default_send.resize((30, 30), PIL_Image.LANCZOS)
	GUI.default_send = ImageTk.PhotoImage(GUI.default_send)

	# ————— MIC BUTTON IMAGES —————
	# ————— ACTIVE MIC —————
	GUI.active_mic = PIL_Image.open("Media/mic_active.png")
	GUI.active_mic = GUI.active_mic.resize((40, 40), PIL_Image.LANCZOS)
	GUI.active_mic = ImageTk.PhotoImage(GUI.active_mic)
	# ————— INACTIVE MIC —————
	GUI.inactive_mic = PIL_Image.open("Media/mic_inactive.png")
	GUI.inactive_mic = GUI.inactive_mic.resize((40, 40), PIL_Image.LANCZOS)
	GUI.inactive_mic = ImageTk.PhotoImage(GUI.inactive_mic)

	# ————— BUTTONS —————
	# ————— SEND BUTTON —————
	sendbutton = Label(
		master = textboxframe,
		image = GUI.default_send,
		bg = "#E8D1D9",
		height = 48
	)
	sendbutton.bind("<Button-1>", lambda event: print(">>> Fetched text:", Button_Press("Sending", sendbutton)))

	# ————— MIC BUTTON —————
	micbutton = Label(
		master = textboxframe,
		image = GUI.inactive_mic,
		bg = "#E8D1D9",
		height = 48
	)
	micbutton.bind("<Button-1>", lambda event: Button_Press("Listening", micbutton))

	# ————— GUI WINDOW INITIATION —————
	titleframe.pack(pady = (45, 30))
	rose_panel.pack(side = LEFT)
	titlelabel.pack(side = RIGHT)
	textboxframe.pack()
	textbox.pack(padx = (9, 0), ipady = 1, side= LEFT)
	micbutton.pack(side = RIGHT)
	sendbutton.pack(side = RIGHT)

	wndw.mainloop()

	return

# ————— SLEEP FUNCTION FOR TKINTER —————
def tksleep(self, time:float) -> None:
	self.after(int(time*1000), self.quit)
	self.mainloop()
Misc.tksleep = tksleep

# ————— BUTTONS ANIMATION AND ACTIVATION FUNCTION —————
def Button_Press(button_state, button):
	match button_state:
		case "Listening":
			button.configure(image = GUI.active_mic)
			button.image = GUI.active_mic
			textbox.tksleep(0.1)
			Output(Grammar_Check(Listen()))
			Button_Press("Done Listening", button)

		case "Done Listening":
			button.configure(image = GUI.inactive_mic)
			button.image = GUI.inactive_mic

		case "Sending":
			button.configure(image = GUI.clicked_send)
			button.image = GUI.clicked_send
			textbox.tksleep(0.1)
			Button_Press("Default", button)
			return textbox.get(1.0, END)

		case _:
			button.configure(image = GUI.default_send)
			button.image = GUI.default_send
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

# ————— CONVERTED TEXT OUTPUT FUNCTION —————
def Output(output_text):
	print(">>> Transcribed text:", output_text)
	output_list = output_text.split()

	textbox.delete(1.0, END)
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