from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys

from MineSweeper.settings import *
from MineSweeper import gui


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

        btnRun0 = QPushButton("Beginner", self)  # Button text
        btnRun0.move(BTN_X, BTN_Y)  # Button position
        btnRun0.clicked.connect(self.btnRun_clicked_0)  # Function to be executed when clicked

        btnRun1 = QPushButton("Intermediate", self)  # Button text
        btnRun1.move(BTN_X, BTN_Y + 30)  # Button position
        btnRun1.clicked.connect(self.btnRun_clicked_1)  # Function to be executed when clicked

        btnRun2 = QPushButton("Expert", self)  # Button text
        btnRun2.move(BTN_X, BTN_Y + 60)  # Button position
        btnRun2.clicked.connect(self.btnRun_clicked_2)  # Function to be executed when clicked

    def btnRun_clicked_0(self):  # Run GUI when clicked
        gui.GUI("Beginner")

    def btnRun_clicked_1(self):  # Run GUI when clicked
        gui.GUI("Intermediate")

    def btnRun_clicked_2(self):  # Run GUI when clicked
        gui.GUI("Expert")


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
