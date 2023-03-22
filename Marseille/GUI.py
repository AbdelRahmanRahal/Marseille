from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QApplication
import sys

# ————— GUI INITIATION FUNCTION —————
def GUI_Initiation():
	app = QApplication(sys.argv)
	QFontDatabase.addApplicationFont("Media\\Anaheim-Regular.ttf")
	app.setFont(QFont("Anaheim", 40))
	window = MainWindow()
	window.show()

	app.exec()

	return

# ————— MAIN WINDOW CLASS —————
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Marseille")
		self.resize(800, 450)
		self.setContentsMargins(20, 20, 20, 20)
		self.button1 = SendButton()
		self.setCentralWidget(self.button1)
 
		label = QLabel("Hello World", self)
		label.move(50, 100)

# ————— SEND BUTTON CLASS —————
class SendButton(QPushButton):
	def __init__(self):
		super().__init__()
		self.setText("A peculiar button...")
		# self.setText("A peculiar button")

