import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from PyQt5.QtCore import pyqtSlot

class KeyGenWindow(QMainWindow):

    # The function to select the desired directory. Will be called when the user
    # clicks the 'Browse' button
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    def generateClick(self):
        # Call function to generate key. For now, just prints "Generate" to console
        print('Generate')

    def storeClick(self):
        # Call function to generate key. For now, just prints "Store" to console
        print("Store")

    # The help message box function
    def helpMethod(self):
        QMessageBox.about(
            self,
            "Help",
            """This program generates a public key and corresponding\
            private key using the 'Generate' button and stores them\
            in two separate files. You must select the desired\
            directory before storing the keys""".replace("            ", ' ')
            )

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 240))
        self.setWindowTitle("Public/Private Key Generator")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # The text box for the user's desired directory
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(185, 30)
        self.textbox.setText(os.getcwd())

        # The label for the text box
        self.textLabel = QLabel(self)
        self.textLabel.setText('Directory:')
        self.textLabel.move(20, 20)

        # The browse directory button
        self.button = QPushButton('Browse', self)
        #self.button.setToolTip('This is an example button')
        self.button.move(290, 20)
        self.button.clicked.connect(self.on_click)

        # The label for the public key
        self.publicLabel = QLabel(self)
        self.publicLabel.setText('Public Key: ')
        self.publicLabel.move(400 / 3, 80)

        # The label for the private key
        self.privateLabel = QLabel(self)
        self.privateLabel.setText('Private Key: ')
        self.privateLabel.move(400 / 3, 110)

        # The button to generate the keys
        self.generateButton = QPushButton('Generate', self)
        self.generateButton.move(400 / 3 - 50, 165)
        self.generateButton.clicked.connect(self.generateClick)

        # The button to store the keys
        self.storeButton = QPushButton('Store', self)
        self.storeButton.move(800 / 3 - 50, 165)
        self.storeButton.clicked.connect(self.storeClick)

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
        self.textbox.resize(self.width() - 215, 30)
        self.generateButton.move(self.width() / 3 - 50, self.height() - 75)
        self.storeButton.move(2 * self.width() / 3 - 50, self.height() - 75)
        self.publicLabel.move(self.width() / 3, self.height() / 2 - 40)
        self.privateLabel.move(self.width() / 3, self.height() / 2 - 10)
        QMainWindow.resizeEvent(self, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = KeyGenWindow()
    mainWin.show()
    sys.exit( app.exec_() )

