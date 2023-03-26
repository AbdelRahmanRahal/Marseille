from PySide6.QtGui import QFont, QFontDatabase, QIcon, QImage, QPicture, QPixmap
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QMenu, QPushButton, QSystemTrayIcon, QTextEdit, QVBoxLayout, QWidget
import sys


# ————— GUI INITIATION FUNCTION —————
def GUI_Initiation():
	# ————— LOAD USER CONFIGURATION —————
	global loaded_config
	loaded_config = load_config()
	for config, value in loaded_config.items():
		print(f">>> {config} : {value}")

	global app, window, tray_icon
	app = QApplication(sys.argv)
	QFontDatabase.addApplicationFont("Media/Anaheim-Regular.ttf")
	QFontDatabase.addApplicationFont("Media/Segoe UI.ttf")
	app.setFont(QFont("Anaheim"))


	window = MainWindow()	
	tray_icon = SystemTrayIcon(QIcon("Media/rose.png"), window)

	app.exec()

	return

def load_config():
	config = {}
	file = open("config.txt", "r")
	# config_lines = file.read().split("\n")
	config_lines = file.readlines()
	file.close()

	for line in config_lines:
		config_split = line.split(":")
		config[config_split[0]] = eval(config_split[1])

	return config

# ————— MAIN WINDOW CLASS —————
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Marseille")
		self.setWindowIcon(QIcon("Media/rose.png"))
		self.resize(loaded_config["window_width"], loaded_config["window_height"])
		self.setMinimumSize(800, 450)
		self.setContentsMargins(20, 20, 20, 20)
		# button1 = SendButton()

		label = QLabel(self)
		pixmap = QPixmap("Media/rose_resized.png")
		label.setPixmap(pixmap)
		self.setCentralWidget(label)

		if loaded_config["open_window_on_startup"]:
			self.show()

	def closeEvent(self, event):
		if loaded_config["minimise_in_tray_on_quit"]:
			event.ignore()
			window.hide()
			tray_icon.show()
			tray_icon.showMessage('Window minimised', 'Marseille is running in the background.')
			print(">>> Window minimised. Marseille is running in the background.")

# ————— TRAY ICON CLASS —————
class SystemTrayIcon(QSystemTrayIcon):
	def __init__(self, icon, parent = None):
		super().__init__(icon, parent)
		self.setToolTip("Marseille Tray Application")

		menu = QMenu(parent)
		menu.setFont(QFont("Segoe UI", 9))
		open_app = menu.addAction("Open Marseille")
		open_app.triggered.connect(self.showMWindow)
		open_app.setIcon(icon)

		menu.addSeparator()

		quit_app = menu.addAction("Quit")
		quit_app.triggered.connect(lambda self : app.quit())

		self.setContextMenu(menu)
		self.activated.connect(self.onTrayIconActivated)

		if loaded_config["open_window_on_startup"] == False:
			self.show()

	def onTrayIconActivated(self, reason):
		if reason == QSystemTrayIcon.Trigger:
			window.show()
			tray_icon.hide()

	def showMWindow(self):
		window.show()
		tray_icon.hide()

# ————— SEND BUTTON CLASS —————
class SendButton(QPushButton):
	def __init__(self):
		super().__init__()
		self.setText("A peculiar button...")