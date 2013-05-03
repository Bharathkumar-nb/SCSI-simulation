from modeSensePopup import Ui_Dialog
from PyQt4 import QtCore, QtGui

class ModeSensePopup(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.mode_sense = {}
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.create_mode_sensecdb)
		
	def create_mode_sensecdb(self):
		self.mode_sense["operationCode"]=[0x1A,0,7,8]
		DBD=str(self.ui.lineEdit.text())
		if(DBD=="Y" or DBD=="y"):
			self.mode_sense["DBD"]=[1,1,3,1]
		else:
			self.mode_sense["DBD"]=[0,1,3,1]

		PC=str(self.ui.lineEdit_2.text())
		self.mode_sense["PC"]=[PC,2,7,2]
		LUN=str(self.ui.lineEdit_3.text())
		self.mode_sense["LUN"]=[int(LUN),1,7,4]

		AL=str(self.ui.lineEdit_6.text())
		self.mode_sense["AL"]=[int(AL),4,7,8]

		pageCode=str(self.ui.lineEdit_4.text())
		subPage=str(self.ui.lineEdit_5.text())
		self.mode_sense["subPage"]=[subPage,3,7,8]
		self.mode_sense["pageCode"]=[pageCode,2,5,6]
                self.mode_sense["Reserved_1"]=["Reserved",1,7,4]
                self.mode_sense["Reserved_2"]=["Reserved",1,2,3]
                self.mode_sense["Control"]=["Control",5,7,8]
		self.close()
		
	def getCdb(self):
	    return self.mode_sense
		
			
def mode_sense_server(mode_sense):
	PC=mode_sense["PC"][0]
	if not(PC=="00b"or PC=="01b" or PC=="10b" or PC=="11b"):
		return "invalid Page Control"

	LUN=mode_sense["LUN"][0]
	if not(int(LUN)>=1 and int(LUN)<6):
	    return "LUN not present"

	
	AL=mode_sense["AL"][0]
	pageCode=mode_sense['pageCode'][0]
	if not(pageCode=="00h" or pageCode=="0Ah"):
		return "PAGES NOT IMPLEMENTED"
	
	
	cdb={}
	if(mode_sense["pageCode"][0]=='00h'):
		print "Vendor Specific Page"
		create_header(cdb,False)
		if(mode_sense["DBD"][0]==0):
			create_discript(cdb)
		
	else:
		print "Control Mode Page"
		create_header(cdb,True)
		create_page(cdb)
		if(mode_sense["DBD"][0]==0):
			create_discript(cdb)
	if(int(AL)>int(cdb["MODE DATA LENGTH"][0], 16)):
		return str(cdb)
	else:
		return "SIZE OF BUFFER INSUFFICIENT"
		
def create_header(cdb,chk):
	if(chk):
		cdb["MODE DATA LENGTH"]=["16",0,7,8]
	else:
		cdb["MODE DATA LENGTH"]=["C",0,7,8]

	cdb["MEDIUM TYPE"]=["MEDTYPE",1,7,8]
	cdb["DEVICE-SPECIFIC PARAMETER"]=["DeviceSpecificParam",2,7,8]
	cdb["BLOCK DESCRIPTOR LENGTH"]=[8,3,7,8]
		
def create_discript(cdb):
	cdb["DENSITY CODE"]=["DENSITY CODE",4,7,8]
	cdb["NUMBER OF BLOCKS"]=["NUMBER OF BLOCKS",5,7,24]
	cdb["Reserved_1"]=["Reserved",8,7,8]
	cdb["BLOCK LENGTH"]=["BLOCK LENGTH",9,7,24]
		
def create_page(cdb):
	f = open('controlModePage.dat', 'r')
	for line in f:
		line=line.strip()
		field=line.split(' ')
		if(field[1]=='PS'):
			cdb['PS']=[field[0],12,7,1]

		elif(field[1]=='SPF'):
			print("spf --- " + str(field[0]))
			cdb['SPF']=['SPF',12,6,1]

		elif(field[1]=='PAGE-CODE'):
			cdb['PAGE CODE']=[field[0],12,5,6]

		elif(field[1]=='PAGE-LENGTH'):
			cdb['PAGE LENGTH']=[field[0],13,7,8]

		elif(field[1]=='TST'):
			cdb['TST']=[field[0],14,7,3]

		elif(field[1]=='TMF_ONLY'):
			cdb['TMF_ONLY']=[field[0],14,4,1]

		elif(field[1]=='DPICZ'):
			cdb['DPICZ']=[field[0],14,3,1]

		elif(field[1]=='D_SENSE'):
			cdb['D_SENSE']=[field[0],14,2,1]

		elif(field[1]=='GLTSD'):
			cdb['GLTSD']=[field[0],14,1,1]

		elif(field[1]=='RLEC'):
			cdb['RLEC']=[field[0],14,0,1]

		elif(field[1]=='QUEUE-ALGORITHM-MODIFIER'):
			cdb['QUEUE ALGORITHM MODIFIER']=[field[0],15,7,4]

		elif(field[1]=='NUAR'):
			cdb['NUAR']=[field[0],15,3,1]

		elif(field[1]=='QERR'):
			cdb['QERR']=[field[0],15,2,2]

		elif(field[1]=='Obsolete_1'):
			cdb['Obsolete_1']=[field[0],15,0,1]

		elif(field[1]=='VS'):
			cdb['VS']=[field[0],16,7,1]

		elif(field[1]=='RAC'):
			cdb['RAC']=[field[0],16,6,1]

		elif(field[1]=='UA_INTLCK_CTRL'):
			cdb['UA_INTLCK_CTRL']=[field[0],16,5,2]

		elif(field[1]=='Obsolete_2'):
			cdb['Obsolete_2']=[field[0],16,2,3]

		elif(field[1]=='SWP'):
			cdb['SWP']=[field[0],16,3,1]

		elif(field[1]=='ATO'):
			cdb['ATO']=[field[0],17,7,1]

		elif(field[1]=='TAS'):
			cdb['TAS']=[field[0],17,6,1]

		elif(field[1]=='ATMPE'):
			cdb['ATMPE']=[field[0],17,5,1]

		elif(field[1]=='RWWP'):
			cdb['RWWP']=[field[0],17,4,1]

		elif(field[1]=='Reserved'):
			cdb['Reserved_2']=[field[0],17,3,1]

		elif(field[1]=='AUTOLOAD-MODE'):
			cdb['SPF']=[field[0],17,2,3]

		elif(field[1]=='Obsolete_3'):
			cdb['Obsolete_3']=[field[0],18,7,16]

		elif(field[1]=='BUSY-TIMEOUT-PERIOD'):
			cdb['BUSY TIMEOUT PERIOD']=[field[0],20,7,16]

		elif(field[1]=='EXTENDED-SELF-TEST-COMPLETION-TIME'):
			cdb['EXTENDED SELF-TEST COMPLETION TIME']=[field[0],22,7,16]

