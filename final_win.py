from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle("Final Result")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.final_label = QLabel("Calculating your level...")
        
        self.layout = QVBoxLayout()
        self.layout.addStretch(1)
        self.layout.addWidget(self.final_label, alignment=Qt.AlignCenter)
        self.layout.addStretch(1)
        
        self.setLayout(self.layout)
        
        self.calculate_level()

    def calculate_level(self):
        age = int(self.exp.age)
        result = int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)
        level = "N/A"

        if age >= 15:
            if result >= 15:
                level = "Low"
            elif 11 <= result < 15:
                level = "Satisfactory"
            elif 6 <= result < 11:
                level = "Average"
            elif 0.5 <= result < 6:
                level = "Above average"
            elif result < 0.5:
                level = "High"
        elif age >= 13:
            if result >= 16.5:
                level = "Low"
            elif 12.5 <= result < 16.5:
                level = "Satisfactory"
            elif 7.5 <= result < 12.5:
                level = "Average"
            elif 2 <= result < 7.5:
                level = "Above average"
            elif result < 2:
                level = "High"
        elif age >= 11:
            if result >= 18:
                level = "Low"
            elif 14 <= result < 18:
                level = "Satisfactory"
            elif 9 <= result < 14:
                level = "Average"
            elif 3.5 <= result < 9:
                level = "Above average"
            elif result < 3.5:
                level = "High"
        elif age >= 9:
            if result >= 19.5:
                level = "Low"
            elif 15.5 <= result < 19.5:
                level = "Satisfactory"
            elif 10.5 <= result < 15.5:
                level = "Average"
            elif 5 <= result < 10.5:
                level = "Above average"
            elif result < 5:
                level = "High"
        elif age >= 7:
            if result >= 21:
                level = "Low"
            elif 17 <= result < 21:
                level = "Satisfactory"
            elif 12 <= result < 17:
                level = "Average"
            elif 6.5 <= result < 12:
                level = "Above average"
            elif self.result < 6.5:
                level = "High"

        self.final_label.setText(f"Your level is: {level}")
