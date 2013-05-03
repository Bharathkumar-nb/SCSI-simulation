from TUR_pop import Ui_Dialog
from PyQt4 import QtCore, QtGui
import random


class TurPopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.tur = {}
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.createTur)
		
		
	#package to be sent
	def createTur(self):
		self.tur["operationCode"] = [0x00,0,7,8]
		self.tur["LUN"] = [int(str(self.ui.lineEdit.text())),1,2,3]
		self.tur["reserved1"] = ["reserved",1,7,5]
		self.tur["reserved2.1"] = ["reserved",2,7,8]
		self.tur["reserved2.2"] = ["reserved",3,7,8]
		self.tur["reserved2.3"] = ["reserved",4,7,8]
		self.tur["control"] = ["control",5,7,8]
		self.close()
	
	def getCdb(self):
		return self.tur;


