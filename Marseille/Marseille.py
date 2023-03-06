import speech_recognition as sr
import pyglet, pyttsx3, sys
from tkinter import *
from PIL import ImageTk, Image


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
	titleFrame.pack()

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
	txtbox = Label(
		master = wndw,
		text = "test text",
		font = ("Anaheim", 20),
		fg = "#470FF4",
		bg = "#E8EAFB",
		width = 25,
		# justify = CENTER,
		bd = 0
	)
	txtbox.config(highlightthickness = 0, highlightbackground = "#BB1F1F")
	txtbox.pack()

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

				text = recognizer.recognize_google(audio)

				if text != []:
					active = False
					return text

		except sr.UnknownValueError:
			print("Sorry, I didn't catch that.\n")
			recognizer = sr.Recognizer()
			continue


if __name__ == "__main__":
	sys.exit(main())