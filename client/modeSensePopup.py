# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modeSenseClient.ui'
#
# Created: Mon Apr 29 16:12:08 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(417, 383)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Disable block descriptors(Y/N)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 20, 121, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 171, 31))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Page Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 70, 121, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 91, 31))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "LUN Number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 120, 121, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 171, 31))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Page code 00h/0Ah", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 180, 121, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 121, 21))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "SUBPAGECODE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 161, 41))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "ALLOCATION LENGTH", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 230, 121, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 280, 121, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 340, 101, 31))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

