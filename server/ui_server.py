# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_server.ui'
#
# Created: Tue Apr 30 17:59:49 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(742, 646)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 591, 511))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 610, 131, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 20, 113, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 20, 111, 21))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 61, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 610, 101, 20))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 171, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", "End Connection", None))
        self.pushButton_3.setText(_translate("Form", "Start Server", None))
        self.label_2.setText(_translate("Form", "Set Port :", None))
        self.pushButton_4.setText(_translate("Form", "Clear Screen", None))
        self.label.setText(_translate("Form", "Set IP :", None))

