from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QLineEdit
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
