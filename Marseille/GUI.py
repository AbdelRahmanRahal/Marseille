from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class TestWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("A test window of sorts")
		button = QPushButton("A button of sorts (press me)")
		self.setCentralWidget(button)