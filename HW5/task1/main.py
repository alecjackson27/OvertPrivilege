import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSlot

from predict import score_text, suspicious_url
from operationalize import process_text, identity

class EncryptWindow(QMainWindow):

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
        # Call function to generate score.
        if self.emailbox.toPlainText() != "":
            classifier_score = score_text([self.emailbox.toPlainText()])
            suspicious_score = suspicious_url(self.emailbox.toPlainText())
            if suspicious_score[0]:
                print("yup")
            score = classifier_score + suspicious_score[0]
            self.textbox.setText(str(score))


    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 240))
        self.setWindowTitle("Phishing Detector")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # The text box for the output score
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(185, 30)
        self.textbox.setReadOnly(True)


        # The label for the email box
        self.textLabel = QLabel(self)
        self.textLabel.setText('Email:')
        self.textLabel.move(10, 20)
        

        # The text area for the email.
        self.emailbox = QTextEdit(self)
        self.emailbox. move(50, 20)
        self.emailbox.resize(290, 130)

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
        self.emailbox.resize(self.width() - 100, self.height() - 110)
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

