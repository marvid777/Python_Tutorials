
import sqlite3

from PyQt6.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt6.uic import loadUi
import sys

from qtconsole.qt import QtCore

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
