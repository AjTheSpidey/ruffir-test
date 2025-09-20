from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.layout = QVBoxLayout()

        self.index = QLabel(txt_index)
        self.layout.addWidget(self.index, alignment = Qt.AlignCenter)

        self.workheart = QLabel(txt_workheart)
        self.layout.addWidget(self.workheart, alignment = Qt.AlignCenter)

        self.setLayout(self.layout)
    def connects(self):
        pass

