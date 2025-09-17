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
        self.setWindowTitle("Results")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.layout = QVBoxLayout()

        self.txt_name = QLabel(txt_name)
        self.l_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)

        self.setLayout(self.layout)