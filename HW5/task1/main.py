import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSlot

from predict import score_text
from operationalize import identity

class EncryptWindow(QMainWindow):

    # The function to select the desired file. Will be called when the user
    # clicks the 'Browse' button
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(QFileDialog.getOpenFileName(self, "Select File", "", "public.key")[0])


    # The help message box function
    def helpMethod(self):
        QMessageBox.about(
            self,
            "Help",
            """This program ranks the probability of an email\
            being a phishing attempt, from 0 to 3, with 3\
            meaning the highest likelihood of phishing.""".replace("            ", ' ')
            )

    def generateClick(self):
        # Call function to generate key. For now, just prints "Generate" to console
        if self.cipherbox.toPlainText() != "":
            self.textbox.setText(score_text(self.cipherbox.toPlainText()))


    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 240))
        self.setWindowTitle("Phishing Detector")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # The text box for the user's desired file
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(185, 30)
        self.textbox.setReadOnly(True)


        # The label for the text box
        self.textLabel = QLabel(self)
        self.textLabel.setText('Email:')
        self.textLabel.move(10, 20)
        

        # The text box for the user's message
        self.messagebox = QLineEdit(self)
        self.messagebox.move(100, 60)
        self.messagebox.resize(185, 30)

        # The text area for the ciphertext
        self.cipherbox = QTextEdit(self)
        self.cipherbox. move(50, 20)
        self.cipherbox.resize(290, 130)

        # The button to generate the keys
        self.generateButton = QPushButton('Score:', self)
        self.generateButton.move(150, 165)
        self.generateButton.clicked.connect(self.generateClick)

        # The help option on the toolbar
        helpAct = QAction(QIcon('help.png'), '&Help', self)
        helpAct.triggered.connect(self.helpMethod)

        # The toolbar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Help')
        fileMenu.addAction(helpAct)

        # The text box for the user's desired file
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(100, 30)
        self.textbox.setReadOnly(True)

        self.show()
    
    # Overwriting the resizeEvent() function so that the proportions of the GUI
    # remain intact
    def resizeEvent(self, event):
        self.generateButton.move(self.width() / 3 - 50, self.height() - 75)
        self.textbox.move(2 * self.width() / 3 - 50, self.height() - 75)
        self.cipherbox.resize(self.width() - 100, self.height() - 110)
        QMainWindow.resizeEvent(self, event)

    # Keeps the clipboard global on Windows and Mac. Linux requires clipboard manager.
    def closeEvent(self, event):
        clipboard = QGuiApplication.clipboard()
        event = QtCore.QEvent(QtCore.QEvent.Clipboard)
        QGuiApplication.sendEvent(clipboard, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = EncryptWindow()
    mainWin.show()
    sys.exit( app.exec_() )

