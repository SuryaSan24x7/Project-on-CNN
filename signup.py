# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import sqlite3
from tkinter.constants import ALL
from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re
import sys
from tkinter.constants import ALL
import os

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

class Ui_signUp(object):
     def insertData(self):
        username1 = self.uname_lineEdit.text()
        username=str(username1)
        email1 = self.email_lineEdit.text()
        email = str(email1)
        password1 = self.password_lineEdit.text()
        password =str(password1)
        
        connection = sqlite3.connect("Face.db")
        connection.execute("create table if not exists registration(username text not null,email text,password text)")
        s="insert into registration values('"+username+"','"+email+"','"+password+"')"
        print("query is:-"+s)
        result=connection.execute(s)
        if result:
            
                print ('record successfully inserted')
                
        else:
            print ('registration fail')

        connection.commit()
        connection.close()
        self.showmsg()

     def showmsg(self):
        self.showdialog()
     def showdialog(self):
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Information)

         msg.setText("Registration Status")
         msg.setInformativeText("Registration Successful")
         msg.setWindowTitle("Status")
         # msg.setDetailedText("The details are as follows:")
         msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

         retval = msg.exec_()
         print
         "value of pressed message box button:", retval

     def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(540, 370)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 182, 211, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"QLineEdit{\n"
"border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
   
    

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 100, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 81, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 200, 81, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(210, 100, 211, 27))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(210, 150, 211, 27))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(210, 200, 211, 27))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(217, 19, 260, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("\n"
"QDialog{\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 182, 211, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(220, 250, 91, 27))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        #########################EVENT##############
        self.signup_btn.clicked.connect(self.insertData)
############################################
        
        self.signin_btn = QtGui.QPushButton(Dialog)
        self.signin_btn.setGeometry(QtCore.QRect(338, 250, 81, 27))
        self.signin_btn.setObjectName(_fromUtf8("signin_btn"))
        #####################################################
        self.signin_btn.clicked.connect(self.quit)
        ########################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

     def quit(self):
         print('Process end')
         print('******End******')
         sys.exit()

     def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "USERNAME", None))
        self.label_2.setText(_translate("Dialog", "EMAIL ID", None))
        self.label_3.setText(_translate("Dialog", "PASSWORD", None))
        self.label_4.setText(_translate("Dialog", "Registration Form", None))
        self.signup_btn.setText(_translate("Dialog", "Sign Up", None))
        self.signin_btn.setText(_translate("Dialog", "Exit", None))

     def signInCheck(self):
        
        self.signInShow()
        print("SignIp button clicked !")
        
     def signInShow(self):
        self.signInnWindow=QtGui.QDialog()
        self.ui=Ui_Dialog()
        self.ui.setinUi(self.signInnWindow)
        self.signInnWindow.show()
        print("i'm in self signup windows")

     def quit(self):
        print('Process end')
        print('******End******')
        sys.exit()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

