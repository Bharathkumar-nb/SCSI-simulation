from sendDiagPopup import *
from PyQt4 import QtCore, QtGui
import random


class SendDiagPopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.send_diagnostic = {}
		self.ui = Ui_send_diagnostic()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.create_send_diagnostic)
		
	
	def create_send_diagnostic(self):
		
		self.send_diagnostic["operationCode"]=[0x1D,0,7,8]
		#print "Enter the self bit(1/0)"	
		self_test=str(self.ui.lineEdit.text())
		
		self_code=str(self.ui.lineEdit_3.text())
		
		self.send_diagnostic["Self Test Code"]=[int(self_code,2),1,7,3] 
		
		self.send_diagnostic["PFbit"]=[0,1,4,1]
		self.send_diagnostic["Reserved1"]=["reserved",1,3,1]
		self.send_diagnostic["Self Test"]=[int(self_test),1,2,1]
		devoff=str(self.ui.lineEdit_4.text())
		
		self.send_diagnostic["DevOffl"]=[int(devoff),1,1,1]
		unitoff = str(self.ui.lineEdit_2.text())
		
		self.send_diagnostic["UnitOffl"]=[int(unitoff),1,0,1]
		self.send_diagnostic["Reserved2"]=["reserved",2,7,8]
		self.send_diagnostic["Param MSB"]=["MSB",3,7,1]
		self.send_diagnostic["Param List1"]=["Parameter List",3,6,7]
		self.send_diagnostic["Param List2"]=["Parameter List",4,7,7]
		self.send_diagnostic["Param LSB"]=["LSB",4,0,1]
		self.send_diagnostic["Control"]=["Control",5,7,8]
		self.close()
		
	
	
	def getCdb(self):
		return self.send_diagnostic


