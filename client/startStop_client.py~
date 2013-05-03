from startStopPopup import Ui_Dialog
from PyQt4 import QtCore, QtGui
activeLun=[]


class startStopPopUp(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.startStop = {}
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.createStartStopCdb)
	
	def createStartStopCdb(self):
		
		self.startStop["operationCode"]=[0x1B,0,7,8]
		if(self.ui.immed0.isChecked()):
		  self.startStop["IMMED"]=[0b0,1,0,1]
		if(self.ui.immed1.isChecked()):
		  self.startStop["IMMED"]=[0b1,1,0,1]
		self.startStop["LUN"]=[str(self.ui.lunNum.text()),1,7,3]
		
		self.startStop["Reserved1"]=["reserved",1,4,4]
		self.startStop["Reserved2"]=["reserved",2,7,8]
		self.startStop["Reserved3"]=["reserved",3,7,8]
		self.startStop["Reserved4"]=["reserved",4,7,6]
		if(self.ui.loej0.isChecked()):
		  self.startStop["LOEJ"]=[0b0,4,1,1]
		if(self.ui.loej1.isChecked()):
		  self.startStop["LOEJ"]=[0b1,4,1,1]
		if(self.ui.start0.isChecked()):
		  self.startStop["start"]=[0b0,4,0,1]

		if(self.ui.start1.isChecked()):
		  self.startStop["start"]=[0b1,4,0,1]
		 
		self.startStop["Control"]=["control",5,7,8]
		self.close()

	def getCdb(self):
		return self.startStop;

		

