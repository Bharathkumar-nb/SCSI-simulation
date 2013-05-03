from inquiryPopup import Ui_MainWindow
from PyQt4 import QtCore, QtGui


class InquiryPopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.inq_req_cdb = {}
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.createInqCdb)
	
	
		
	def createInqCdb(self):
		
		#value byteno bitno size
		self.inq_req_cdb["operationCode"] = [0x12,0,7,8]
		self.inq_req_cdb["LUN"] = [str(self.ui.lineEdit.text()),1,7,3] #user input
		
		self.inq_req_cdb["reserved1"] = ["RESERVED",1,4,4]
		self.inq_req_cdb["EVPD"] = [str(self.ui.lineEdit_2.text()),1,0,1] #EVPD = 0, receive std inquiry data  -- USER INPUT
		self.inq_req_cdb["pageCode"] = [str(self.ui.lineEdit_3.text()),2,7,8]   #USERINPUT
		self.inq_req_cdb["allocLenMsb"] = [0,3,7,8]
		self.inq_req_cdb["allocLenLsb"] = [96,4,7,8]
		self.inq_req_cdb["control"] = ["control",5,7,8]	
		self.close()

	
	
	def getCdb(self):
		return self.inq_req_cdb;



		



