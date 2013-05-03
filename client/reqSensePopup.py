# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req_sense_client.ui'
#
# Created: Mon Apr 29 20:50:38 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(603, 230)
       
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(30, 60, 431, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(460, 50, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(270, 120, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
       

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Enter format of sense data being returned: 0.Fixed 1.Descriptor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))

