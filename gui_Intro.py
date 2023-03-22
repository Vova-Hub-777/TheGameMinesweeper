from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


class Window(QWidget):
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.setGeometry(700, 300, 500, 400)
        layout = QVBoxLayout()
        self.setLayout(layout)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())