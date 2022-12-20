# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from AgeGenderLive import AgeEstimator
from Morpher01 import Ui_MainWindow
from Morpher02 import Ui_MainWindow01
from emotion import emotion_webcam as em



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.resize(1200, 900)
        HomePage.setStyleSheet(_fromUtf8("\n""background-image: url(p1.jpg);\n"""))
        self.centralwidget = QtGui.QWidget(HomePage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 80, 130, 41))
        self.pushButton.clicked.connect(self.morpher2)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: white);\n""color: rgb(0, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 170, 130, 41))
        self.pushButton_1.clicked.connect(self.agegender)
        self.pushButton_1.setStyleSheet(_fromUtf8("background-color: white);\n"
                                                  "color: rgb(0, 0, 0);"))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 80, 130, 41))
        self.pushButton_2.clicked.connect(self.morpher1)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: white);\n""color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 170, 130, 41))
        self.pushButton_3.clicked.connect(self.emotionrecognition)
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: white);\n""color: rgb(0, 0, 0);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 260, 130, 41))
        self.pushButton_4.clicked.connect(self.quit)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: white);\n" "color: rgb(0, 0, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_5"))
        HomePage.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HomePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        HomePage.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(HomePage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HomePage.setStatusBar(self.statusbar)
        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow", None))
        self.pushButton.setText(_translate("HomePage", "Face Morpher 2", None))
        self.pushButton_1.setText(_translate("HomePage", "Age-Gender", None))
        self.pushButton_2.setText(_translate("HomePage", "Face Morpher 1", None))
        self.pushButton_3.setText(_translate("HomePage", "Emotion Recognition", None))
        self.pushButton_4.setText(_translate("HomePage", "Exit", None))

    def morpher1(self):
        self.videoWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def morpher2(self):
        self.videoWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow01()
        self.ui.setupUii(self.videoWindow)
        self.videoWindow.show()

    def emotionrecognition(self):
        print ('Process Start')
        em.emotioncap()

    def agegender(self):
        print ('Process Start')
        result1,result2=AgeEstimator(self)
        print("Result of Gender ::", result1)
        print("Result of Age ::", result2)

    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.move(550, 170)
    HomePage.show()
    sys.exit(app.exec_())

