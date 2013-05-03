# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_cap.ui'
#
# Created: Tue Apr 30 16:56:50 2013
#      by: PyQt4 UI code generator 4.9.3
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
        Dialog.resize(350, 212)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 113, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 86, 113, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 140, 51, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Enter PMI bit(0/1):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Enter LBA:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

