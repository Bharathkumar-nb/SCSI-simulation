import string
from read_pop import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from modeSelectPopup import *



class ModeSelPopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.modesel_cdb = {}
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.create_mode_select)
		
		

	def create_mode_select(self):
		
		send={}
		send["operationCode"]=[0x15,0,7,8]
        	
		send["lun"]=[str(self.ui.lineEdit.text()),1,7,3]
	
		send["sp"]=[str(self.ui.lineEdit_2.text()),1,0,1]
		send["reserved"]=["reserved",1,3,3]
		send["control"]=["control",5,7,8]
		
		send["pf"]=[str(self.ui.lineEdit_3.text()),1,4,1]
        	
		send["paramlength"]=[int(str(self.ui.lineEdit_4.text())),4,7,8]
		send["reserve1"]=["reserved",2,7,16]
                self.modesel_cdb=send
		self.close()
	
	def getCdb(self):
		return self.modesel_cdb;



