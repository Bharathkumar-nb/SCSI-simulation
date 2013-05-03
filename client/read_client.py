from read_pop import Ui_MainWindow
from PyQt4 import QtCore, QtGui

class ReadPopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.read_cdb = {}
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.createReadCdb)
		
		
	#package to be sent
	def createReadCdb(self):
		self.read_cdb["operationCode"] = [0x08,0,7,8]
		#LUN from user
		self.read_cdb["LUN"] = [str(self.ui.lineEdit.text()),1,7,3]
		#LBA from user
		self.read_cdb["LBA_first"] = [0,1,4,5]
		self.read_cdb["LBA_sec"] = [0,2,7,8]
		self.read_cdb["LBA_third"] = [int(str(self.ui.lineEdit_2.text())),3,7,8]

		#transfer length from user
		self.read_cdb["transferLength"] = [str(self.ui.lineEdit_3.text()),4,7,8]
		#flag and link bits to be implemented later
		self.read_cdb["control"] = ["CONTROL",5,7,8]
		self.close()
	
	def getCdb(self):
		return self.read_cdb;


