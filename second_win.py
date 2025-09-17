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
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.txt_name = QLabel(txt_name)
        self.l_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)

        self.name = QLineEdit(txt_hintname)
        self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)

        self.txt_hintage = QLabel(txt_hintage)
        self.l_line.addWidget(self.txt_hintage, alignment = Qt.AlignLeft)

        self.age = QLineEdit("0")
        self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)

        self.test1 = QLabel(txt_test1)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)

        self.starttest1 = QPushButton(txt_starttest1)
        self.l_line.addWidget(self.starttest1, alignment = Qt.AlignLeft)

        self.hinttest1 = QLineEdit("0")
        self.l_line.addWidget(self.hinttest1, alignment = Qt.AlignLeft)

        self.test2 = QLabel(txt_test2)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)

        self.starttest2 = QPushButton(txt_starttest2)
        self.l_line.addWidget(self.starttest2, alignment = Qt.AlignLeft)

        self.test3 = QLabel(txt_test3)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)

        self.starttest3 = QPushButton(txt_starttest3)
        self.l_line.addWidget(self.starttest3, alignment = Qt.AlignLeft)

        self.hinttest2 = QLineEdit("0")
        self.l_line.addWidget(self.hinttest2, alignment = Qt.AlignLeft)

        self.hinttest2 = QLineEdit("0")
        self.l_line.addWidget(self.hinttest2, alignment = Qt.AlignLeft)

        self.sendresults = QPushButton(txt_sendresults)
        self.l_line.addWidget(self.sendresults, alignment = Qt.AlignCenter)

        self.timer = QLabel("00:00:09")
        self.r_line.addWidget(self.timer, alignment = Qt.AlignRight)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = FinalWin()
