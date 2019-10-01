import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from PyQt5.QtCore import pyqtSlot

class DecryptWindow(QMainWindow):

    # The function to select the desired directory. Will be called when the user
    # clicks the 'Browse' button
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    def decryptClick(self):
        # Call function to decrypt. For now, just prints "Decrypt" to console
        print('Decrypt')

    # The help message box function
    def helpMethod(self):
        QMessageBox.about(
            self,
            "Help",
            """This program decrypts a message using a private key.\
            Type the message in the top textfield and select\
            your desired private.key file, then click 'Decrypt'""".replace("            ", ' ')
            )

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 240))
        self.setWindowTitle("RSA Decryption")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # The text box for the user's desired directory
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(self.width() - 375, 30)

        # The browse files button
        self.button = QPushButton('Browse', self)
        #self.button.setToolTip('This is an example button')
        self.button.move(self.width() - 110, 20)
        self.button.clicked.connect(self.on_click)

        # The label for the text box
        self.textLabel = QLabel(self)
        self.textLabel.setText('Public Key:')
        self.textLabel.move(20, 20)

        # The text box for the user's ciphertext
        self.messagebox = QLineEdit(self)
        self.messagebox.move(100, 60)
        self.messagebox.resize(self.width() - 375, 30)

        # The label for the ciphertext box
        self.messageLabel = QLabel(self)
        self.messageLabel.setText('Cipher Text:')
        self.messageLabel.move(20, 60)

        # The encrypt button
        self.encryptButton = QPushButton('Decrypt', self)
        self.encryptButton.move(self.width() - 110, 60)
        self.encryptButton.clicked.connect(self.decryptClick)

        # The text area for the plaintext
        self.cipherbox = QTextEdit(self)
        self.cipherbox. move(100, 100)
        self.cipherbox.resize(self.width() - 275, 100)
        self.cipherbox.setReadOnly(True)

        # The label for the decrypted plain text box
        self.encryptLabel = QLabel(self)
        self.encryptLabel.setText('Plain Text:')
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = DecryptWindow()
    mainWin.show()
    sys.exit( app.exec_() )

