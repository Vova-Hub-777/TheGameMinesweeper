from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys

from MineSweeper.settings import *


class Window(QWidget):
    def __init__(self):
        print("intro")
        super().__init__()
        self.count = 0
        self.initialize()

    def initialize(self):
        self.setGeometry(700, 300, 500, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Minesweeper")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Hack', 15))
        layout.addWidget(self.label)

        btnRun0 = QPushButton("Beginner", self)
        btnRun0.move(BTN_X, BTN_Y)

        btnRun1 = QPushButton("Intermediate", self)
        btnRun1.move(BTN_X, BTN_Y + 30)

        btnRun2 = QPushButton("Expert", self)
        btnRun2.move(BTN_X, BTN_Y + 60)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())