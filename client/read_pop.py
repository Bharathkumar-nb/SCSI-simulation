# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_pop_up.ui'
#
# Created: Sat Apr 20 23:15:10 2013
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
        MainWindow.resize(347, 213)
        
        self.lineEdit = QtGui.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 101, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(50, 30, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 60, 101, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(MainWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 90, 101, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(150, 130, 66, 17))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(160, 140, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
       
               
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Enter LUN", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Enter LBA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "TransferLength", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))

