# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
import sys
from userhome import Ui_HomePage



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

class Ui_Dialog(object):
    def UserHomeCheck(self):
        self.userHomeWindow=QtGui.QMainWindow()
        self.ui=Ui_HomePage()
        self.ui.setupUi(self.userHomeWindow)
        self.userHomeWindow.show()
        
    def signUpShow(self):
        self.signUpWindow=QtGui.QDialog()
        self.ui=Ui_signUp()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        print("i'm in self signup windows")
        
    def loginCheck(self):
        
        username1=self.uname_lineEdit.text()
        username =str(username1)
        password1=self.pass_lineEdit.text()
        password = str(password1)
        print("password is:"+password)
        connection=sqlite3.connect("Face.db")
        s="select *from registration where username='"+username+"' and password='"+password+"'"
        print("query is:"+s)
        result=connection.execute(s)
        if(len(result.fetchall())>0):
         print("user found!")
         self.UserHomeCheck()
        
        else:
         print("user not fount!")
         
    
        
        
    def signupCheck(self):
        
        self.signUpShow()
        print("Signup button clicked !")
    
    
    def setinUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(537, 373)
        Dialog.setStyleSheet(_fromUtf8("QDialog{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 182, 211, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"QLineEdit{\n"
"border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}"))
        self.u_user_label = QtGui.QLabel(Dialog)
        self.u_user_label.setGeometry(QtCore.QRect(90, 150, 91, 31))
        self.u_user_label.setObjectName(_fromUtf8("u_user_label"))
        self.pass_label = QtGui.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(90, 190, 81, 31))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
       
        
        self.uname_lineEdit = QtGui.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(190, 149, 201, 31))
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
       
        
        self.pass_lineEdit = QtGui.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(190, 190, 201, 31))
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        
        
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(220, 250, 61, 31))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
       #####################Button Event####################################
        self.login_btn.clicked.connect(self.loginCheck)
        ####################################################################
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(300, 250, 61, 31))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
       ######################################button event################################
        self.signup_btn.clicked.connect(self.quit)
       ############################################################################
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "login form", None))
        self.u_user_label.setText(_translate("Dialog", "USERNAME", None))
        self.pass_label.setText(_translate("Dialog", "PASSWORD", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))
        self.signup_btn.setText(_translate("Dialog", "Exit", None))
        self.label.setText(_translate("Dialog", "Login Form", None))

    def quit(self):
        print ('Process end')
        print ('******End******')
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setinUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

