from PySide6.QtWidgets import QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Marseille")
		self.button1 = SendButton()
		self.setCentralWidget(self.button1)
		# button = QPushButton("A button of sorts (press me)")
		# self.setCentralWidget(button)

class SendButton(QPushButton):
	def __init__(self):
		super().__init__()
		self.setText("A peculiar button...")
		# self.setText("A peculiar button")
		