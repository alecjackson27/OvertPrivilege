import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSlot

class EncryptWindow(QMainWindow):

    # The function to select the desired file. Will be called when the user
    # clicks the 'Browse' button
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(QFileDialog.getOpenFileName(self, "Select File", "", "public.key")[0])

    def encryptClick(self):
        # Call function to encrypt message.
        if os.path.exists(self.textbox.text()):
            self.cipherbox.setText(encryption(self.messagebox.text(), self.textbox.text()))
        else:
            self.cipherbox.setText("Invalid file path")

    # The help message box function
    def helpMethod(self):
        QMessageBox.about(
            self,
            "Help",
            """This program encrypts a message using a public key.\
            Type the message in the top textfield and select\
            your desired public.key file, then click 'Encrypt'""".replace("            ", ' ')
            )

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 240))
        self.setWindowTitle("RSA Encryption")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # The text box for the user's desired file
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(185, 30)
        self.textbox.setReadOnly(True)

        # The browse files button
        self.button = QPushButton('Browse', self)
        #self.button.setToolTip('This is an example button')
        self.button.move(290, 20)
        self.button.clicked.connect(self.on_click)

        # The label for the text box
        self.textLabel = QLabel(self)
        self.textLabel.setText('Public Key:')
        self.textLabel.move(20, 20)

        # The text box for the user's message
        self.messagebox = QLineEdit(self)
        self.messagebox.move(100, 60)
        self.messagebox.resize(185, 30)

        # The label for the message box
        self.messageLabel = QLabel(self)
        self.messageLabel.setText('Plain Text:')
        self.messageLabel.move(20, 60)

        # The encrypt button
        self.encryptButton = QPushButton('Encrypt', self)
        self.encryptButton.move(290, 60)
        self.encryptButton.clicked.connect(self.encryptClick)

        # The text area for the ciphertext
        self.cipherbox = QTextEdit(self)
        self.cipherbox. move(100, 100)
        self.cipherbox.resize(290, 130)
        self.cipherbox.setReadOnly(True)

        # The label for the ecrypted ciphertext box
        self.encryptLabel = QLabel(self)
        self.encryptLabel.setText('Cipher Text:')
        self.encryptLabel.move(20, 100)

        # The help option on the toolbar
        helpAct = QAction(QIcon('help.png'), '&Help', self)
        helpAct.triggered.connect(self.helpMethod)

        # The toolbar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Help')
        fileMenu.addAction(helpAct)

        self.show()
    
    # Overwriting the resizeEvent() function so that the proportions of the GUI
    # remain intact
    def resizeEvent(self, event):
        self.button.move(self.width() - 110, 20)
        self.encryptButton.move(self.width() - 110, 60)
        self.messagebox.resize(self.width() - 215, 30)
        self.textbox.resize(self.width() - 215, 30)
        self.cipherbox.resize(self.width() - 110, self.height() - 110)
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

