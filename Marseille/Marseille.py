import speech_recognition as sr
import pyglet, pyttsx3, sys
from tkinter import *
from PIL import ImageTk, Image
from time import sleep


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
	wndw.iconbitmap("rose.ico")
	wndw.configure(bg = "#F3F4FA")
	pyglet.font.add_file("Anaheim-Regular.ttf")

	# ————— FRAME TO CONTAIN THE TITLE AND THE ICON —————
	titleFrame = Frame(wndw, bg = "#F3F4FA")
	titleFrame.pack(pady = 45)

	image1 = Image.open("rose.png")
	image1 = image1.resize((50, 50), Image.LANCZOS)
	image1 = ImageTk.PhotoImage(image1)
	panel = Label(
		master = titleFrame,
		image = image1,
		bg = "#F3F4FA"
	)
	panel.image = image1
	panel.pack(side = LEFT)

	titlelabel = Label(
		master = titleFrame,
		text = "Marseille",
		font = ("Anaheim", 40, "bold"),
		fg = "#CB0025",
		bg = "#F3F4FA",
	)
	titlelabel.pack(side = RIGHT)

	# ————— OUTPUT AREA (NOT DONE, I HAVE TO GO TO SLEEP) —————
	global textbox
	textbox = Entry(
		master = wndw, #30 characters is the max amount of characters for this label at this font size
		font = ("Anaheim", 17),
		fg = "#700018",
		bg = "#E8D1D9",
		width = 30,
		justify = CENTER,
		bd = 0
	)
	textbox.config(highlightthickness = 0, highlightbackground = "#000793")
	textbox.pack(ipady = 10)

	global button_text
	button_text = StringVar()
	button_text.set("Listen")

	sbmt = Button(
		textvariable = button_text,
		font = ("Anaheim", 15, "bold"),
		fg = "#FFFAF6",
		bg = "#BB1F1F",
		activeforeground = "#FFFAF6",
		activebackground = "#9E1A1A",
		width = 10,
		bd = 3,
		relief = "ridge",
		command = lambda: Click("Listening")
	)
	sbmt.pack(pady = 15, ipadx = 15)

	# ————— WINDOW INITIATION —————
	wndw.mainloop()
	return 0

# ————— SPEECH RECOGNITION FUNCTION —————
def Listen():
	active = True
	recognizer = sr.Recognizer()

	while active:
		try:
			with sr.Microphone() as mic:
				recognizer.adjust_for_ambient_noise(mic, duration = 0.1)
				audio = recognizer.listen(mic)
				converted_text = recognizer.recognize_google(audio)

				if converted_text != []:
					active = False
					return converted_text

		except sr.UnknownValueError:
			print("Sorry, I didn't catch that.\n")
			recognizer = sr.Recognizer()
			continue

def Click(button_state):
	match button_state:
		case "Listening":
			button_text.set("Listening")
			textbox.tksleep(0.1)
			Output()
			Click("default")
		case _:
			button_text.set("Listen")

def Output():
	output_list = Listen().split()
	print(output_list)

	textbox.delete(0, END)
	for word in output_list:
		textbox.insert(END, word + " ")
		textbox.tksleep(0.1)

# ————— SLEEP FUNCTION FOR TKINTER —————
def tksleep(self, time:float) -> None:
	self.after(int(time*1000), self.quit)
	self.mainloop()
Misc.tksleep = tksleep

if __name__ == "__main__":
	sys.exit(main())