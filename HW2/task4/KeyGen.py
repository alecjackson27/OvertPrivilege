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
        print('PyQt5 button click')

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

        self.button = QPushButton('Browse', self)
        #self.button.setToolTip('This is an example button')
        self.button.move(self.width() - 110, 20)
        self.button.clicked.connect(self.on_click)

        helpAct = QAction(QIcon('help.png'), '&Help', self)
        helpAct.triggered.connect(self.helpMethod)

        #file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Help')
        fileMenu.addAction(helpAct)

        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(self.width() - 375, 30)
        self.textbox.setText(os.getcwd())

        self.textLabel = QLabel(self)
        self.textLabel.setText('Directory:')
        self.textLabel.move(20, 20)

        
        #self.setGeometry(300, 300, 300, 200)
        self.show()
        
        #self.setGeometry(300, 300, 250, 150)   
        # self.show()
    
    def resizeEvent(self, event):
        self.button.move(self.width() - 110, 20)
        self.textbox.resize(self.width() - 215, 30)
        QMainWindow.resizeEvent(self, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = KeyGenWindow()
    mainWin.show()
    sys.exit( app.exec_() )

