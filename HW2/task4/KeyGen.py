import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from PyQt5.QtCore import pyqtSlot

class KeyGenWindow(QMainWindow):
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    def generateClick(self):
        # Call function to generate key. For now, just prints "Generate" to console
        print('Generate')

    def storeClick(self):
        # Call function to generate key. For now, just prints "Store" to console
        print("Store")

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

        self.setMinimumSize(QSize(480, 320))
        self.setWindowTitle("Public/Private Key Generator")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(self.width() - 375, 30)
        self.textbox.setText(os.getcwd())

        self.textLabel = QLabel(self)
        self.textLabel.setText('Directory:')
        self.textLabel.move(20, 20)

        self.publicLabel = QLabel(self)
        self.publicLabel.setText('Public Key: ')
        self.publicLabel.move(self.width() / 3, self.height() / 2 - 40)

        self.privateLabel = QLabel(self)
        self.privateLabel.setText('Private Key: ')
        self.privateLabel.move(self.width() / 3, self.height() / 2 - 10)

        self.button = QPushButton('Browse', self)
        #self.button.setToolTip('This is an example button')
        self.button.move(self.width() - 110, 20)
        self.button.clicked.connect(self.on_click)

        self.generateButton = QPushButton('Generate', self)
        self.generateButton.move(self.width() / 3 - 50, self.height() - 100)
        self.generateButton.clicked.connect(self.generateClick)

        self.storeButton = QPushButton('Store', self)
        self.storeButton.move(2 * self.width() / 3 - 50, self.height() - 100)
        self.storeButton.clicked.connect(self.storeClick)

        helpAct = QAction(QIcon('help.png'), '&Help', self)
        helpAct.triggered.connect(self.helpMethod)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Help')
        fileMenu.addAction(helpAct)

        self.show()
    
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

