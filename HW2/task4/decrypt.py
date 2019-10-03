import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSlot
from RSAutils import decryption

class DecryptWindow(QMainWindow):

    # The function to select the desired file. Will be called when the user
    # clicks the 'Browse' button
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(QFileDialog.getOpenFileName(self, "Select File", "", "private.key")[0])

    def decryptClick(self):
        # Call function to decrypt.
        if os.path.exists(self.textbox.text()):
            self.plainbox.setText(decryption(self.messagebox.text(), self.textbox.text()))
        else:
            self.plainbox.setText("Invalid file path")

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
        self.textLabel.setText('Private Key:')
        self.textLabel.move(20, 20)

        # The text box for the user's ciphertext
        self.messagebox = QLineEdit(self)
        self.messagebox.move(100, 60)
        self.messagebox.resize(185, 30)

        # The label for the ciphertext box
        self.messageLabel = QLabel(self)
        self.messageLabel.setText('Cipher Text:')
        self.messageLabel.move(20, 60)

        # The decrypt button
        self.decryptButton = QPushButton('Decrypt', self)
        self.decryptButton.move(290, 60)
        self.decryptButton.clicked.connect(self.decryptClick)

        # The text area for the plaintext
        self.plainbox = QTextEdit(self)
        self.plainbox. move(100, 100)
        self.plainbox.resize(290, 130)
        self.plainbox.setReadOnly(True)

        # The label for the decrypted plain text box
        self.decryptLabel = QLabel(self)
        self.decryptLabel.setText('Plain Text:')
        self.decryptLabel.move(20, 100)

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
        self.decryptButton.move(self.width() - 110, 60)
        self.messagebox.resize(self.width() - 215, 30)
        self.textbox.resize(self.width() - 215, 30)
        self.plainbox.resize(self.width() - 110, self.height() - 110)
        QMainWindow.resizeEvent(self, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = DecryptWindow()
    mainWin.show()
    sys.exit( app.exec_() )

