from logsense_pop import Ui_Dialog
from PyQt4 import QtCore, QtGui


class LogsensePopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.logsense_cdb = {}
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.create_logsense_cdb)
		
		
	#package to be sent
	def create_logsense_cdb(self):
		
		self.logsense_cdb = {}	
		self.logsense_cdb["operationCode"] =	[0x4D,0,7,8]
		self.logsense_cdb["reserved1"] = ["RESERVED",1,7,6]
		self.logsense_cdb["ppc"] = [0,1,1,1]
		self.logsense_cdb["sp"] = [str(self.ui.lineEdit.text()),1,0,1]
		self.logsense_cdb["pc"]  = [0b01,2,7,2] #cumulative values
		self.logsense_cdb["pageCode"] = [0x31,2,5,6] 
		self.logsense_cdb["reserved2"] = ["RESERVED",3,7,16]
		self.logsense_cdb["parameterPointer"] = ["PARAMETER POINTER",5,7,16]
		self.logsense_cdb["allocationLength"] = [5000,7,7,16]
		self.logsense_cdb["control"] = ["CONTROL",9,7,8]
		self.close()
	
	def getCdb(self):
		return self.logsense_cdb;
		
