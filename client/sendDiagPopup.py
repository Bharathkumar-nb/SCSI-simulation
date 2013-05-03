# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_diagnostic.ui'
#
# Created: Sat Apr 27 09:51:24 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_send_diagnostic(object):
    def setupUi(self, send_diagnostic):
        send_diagnostic.setObjectName(_fromUtf8("send_diagnostic"))
        send_diagnostic.resize(632, 515)
       # send_diagnostic = QtGui.QWidget(send_diagnostic)
       # send_diagnostic.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(send_diagnostic)
        self.label.setGeometry(QtCore.QRect(80, 40, 66, 17))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(send_diagnostic)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(send_diagnostic)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 111, 17))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(send_diagnostic)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 211, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(send_diagnostic)
        self.label_5.setGeometry(QtCore.QRect(60, 160, 211, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(send_diagnostic)
        self.pushButton.setGeometry(QtCore.QRect(320, 370, 101, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(send_diagnostic)
        self.lineEdit.setGeometry(QtCore.QRect(350, 30, 111, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(send_diagnostic)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 150, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(send_diagnostic)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 210, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(send_diagnostic)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 90, 113, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_6 = QtGui.QLabel(send_diagnostic)
        self.label_6.setGeometry(QtCore.QRect(60, 220, 121, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(send_diagnostic)
        self.label_7.setGeometry(QtCore.QRect(60, 240, 211, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
       # send_diagnostic.setCentralWidget(send_diagnostic)
       #self.menuBar = QtGui.QMenuBar(send_diagnostic)
       # self.menuBar.setGeometry(QtCore.QRect(0, 0, 632, 25))
       # self.menuBar.setObjectName(_fromUtf8("menuBar"))
       # send_diagnostic.setMenuBar(self.menuBar)
       # self.mainToolBar = QtGui.QToolBar(send_diagnostic)
        #self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        #send_diagnostic.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        #self.statusBar = QtGui.QStatusBar(send_diagnostic)
        #self.statusBar.setObjectName(_fromUtf8("statusBar"))
        #send_diagnostic.setStatusBar(self.statusBar)

        self.retranslateUi(send_diagnostic)
        QtCore.QMetaObject.connectSlotsByName(send_diagnostic)

    def retranslateUi(self, send_diagnostic):
        send_diagnostic.setWindowTitle(QtGui.QApplication.translate("send_diagnostic", "send_diagnostic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("send_diagnostic", "Self Test Bit (0/1)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("send_diagnostic", "DEVOFFL (Device Offline)  (0/1)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("send_diagnostic", "UNITOFFL (Unit Offline)  (0/1)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("send_diagnostic", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("send_diagnostic", "Self Test Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("send_diagnostic", "(Value between 000 and 111)", None, QtGui.QApplication.UnicodeUTF8))

