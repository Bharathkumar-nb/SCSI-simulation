# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c.ui'
#
# Created: Tue Apr 30 17:45:51 2013
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
        Form.resize(1047, 650)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 161, 521))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.verticalLayout.addWidget(self.pushButton_15)
        self.pushButton_16 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.verticalLayout.addWidget(self.pushButton_16)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 30, 91, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(360, 100, 511, 511))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_99 = QtGui.QPushButton(Form)
        self.pushButton_99.setGeometry(QtCore.QRect(910, 580, 98, 27))
        self.pushButton_99.setObjectName(_fromUtf8("pushButton_99"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 30, 113, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 30, 191, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 41, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_3.setText(_translate("Form", "TEST UNIT READY", None))
        self.pushButton_4.setText(_translate("Form", "SEND DIAGNOSTIC", None))
        self.pushButton_5.setText(_translate("Form", " START/STOP", None))
        self.pushButton_7.setText(_translate("Form", "REPORT LUNS", None))
        self.pushButton_8.setText(_translate("Form", "MODE SELECT", None))
        self.pushButton_9.setText(_translate("Form", "REQUEST SENSE", None))
        self.pushButton_10.setText(_translate("Form", "MODE SENSE", None))
        self.pushButton_11.setText(_translate("Form", "READ CAPACITY", None))
        self.pushButton_12.setText(_translate("Form", " LOG SENSE", None))
        self.pushButton_13.setText(_translate("Form", "WRITE", None))
        self.pushButton_14.setText(_translate("Form", "FORMAT UNIT", None))
        self.pushButton_15.setText(_translate("Form", "INQUIRY", None))
        self.pushButton_16.setText(_translate("Form", "READ", None))
        self.pushButton_2.setText(_translate("Form", "Connect", None))
        self.pushButton_99.setText(_translate("Form", "Clear Screen", None))
        self.label_2.setText(_translate("Form", "Port : ", None))
        self.label.setText(_translate("Form", "Server IP :", None))

