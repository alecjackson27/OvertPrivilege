import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *#QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, \
#    QApplication
from PyQt5.QtGui import QIcon, QGuiApplication
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSlot
from RSAutils import *

class KeyGenWindow(QMainWindow):

    # The function to select the desired directory. Will be called when the user
    # clicks the 'Browse' button
    @pyqtSlot()
    def on_click(self):
        self.textbox.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
    
    # Invalid file path message box
    def errorMethod(self):
        QMessageBox.critical(
            self,
            "Error",
            "Path provided is not a valid directory"
        )

    def successMethod(self):
        QMessageBox.about(
            self,
            "Success",
            "Keys successfully generated"
        )

    def generateClick(self):
        # Call function to generate key. For now, just prints "Generate" to console
        # print('Generate')
        self.generateButton.setEnabled(False)
        if os.path.exists(self.textbox.text()):
            if key_generator(self.textbox.text(), self.checkBox.isChecked()):
                self.successMethod()
        else:
            # give error message here
            self.errorMethod()
        self.generateButton.setEnabled(True)

    # The help message box function
    def helpMethod(self):
        QMessageBox.information(
            self,
            "Help",
            """This program generates a public key and corresponding\
            private key using the 'Generate' button and stores them\
            in two separate files. You must select the desired\
            directory before storing the keys""".replace("            ", ' ')
            )

    def helpClick(self):
        QMessageBox.information(
            self,
            "Deterministic vs Probabilistic Help",
            """Checking 'Deterministic' will ensure that the program \
            generates keys using deterministically generated prime\
            numbers, rather than the default probabilistically\
            generated primes. Deterministically generated primes\
            are guaranteed to be prime, but due to the higher\
            number of computations required to deterministically\
            generate primes, the range of primes that can be\
            generated is significantly smaller, making the keys\
            less secure. The default probabilistic method will\
            generate keys using a much larger, 1024-bit number\
            which is almost certainly prime. The probability that\
            it isn't prime is less than that of the program failing\
            due to hardware malfunction.""".replace("            ", ' ')
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

        self.checkBox = QCheckBox("Deterministic", self)
        self.checkBox.move(100, 50)
        self.checkHelpButton = QPushButton("?", self)
        self.checkHelpButton.move(200, 55)
        self.checkHelpButton.resize(20, 20)
        self.checkHelpButton.clicked.connect(self.helpClick)

        # The button to generate the keys
        self.generateButton = QPushButton('Generate', self)
        self.generateButton.move(150, 165)
        self.generateButton.clicked.connect(self.generateClick)

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
        self.generateButton.move(self.width() / 2 - 50, self.height() - 75)
        QMainWindow.resizeEvent(self, event)

    # Keeps the clipboard global on Windows and Mac. Linux requires clipboard manager.
    def closeEvent(self, event):
        clipboard = QGuiApplication.clipboard()
        event = QtCore.QEvent(QtCore.QEvent.Clipboard)
        QGuiApplication.sendEvent(clipboard, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = KeyGenWindow()
    mainWin.show()
    sys.exit( app.exec_() )

