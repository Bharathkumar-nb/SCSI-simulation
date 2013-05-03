import sys
from PyQt4.QtNetwork import *
from PyQt4 import QtCore, QtGui
from ui_client import Ui_Form  
from read_client import *
from readcap_client import *
from inquiry_client import *
from sendDiag_client import *
from reqsense_client import *
from report_luns_client import *
from mode_select_client import *
from logsense_client import *
from startStop_client import *
import write_command
from TUR_client import *
from formatunit_client import *
from cdb import *
from mode_sense_client import *

class MyForm(QtGui.QMainWindow):
	

	def __init__(self, parent=None):
		# setting up gui
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.setWindowTitle("SCSI_client")
		self.ui.lineEdit_2.setText("0.0.0.0")       
		self.ui.lineEdit_3.setText("5131")  
		
		# creates a new socket
		self.s = QTcpSocket()
		#self.w = MyPopup();
		#self.w.setGeometry(100,200,400,400);
		self.cmds={}
		self.cmds["tur"] = 0		
		self.cmds["send_diag"] = 0
		self.cmds["start_stop"] = 0
		self.cmds["report_luns"] = 0
		self.cmds["mode_sel"] = 0
		self.cmds["req_sense"] = 0
		self.cmds["read_cap"] = 0
		self.cmds["log_sense"] = 0
		self.cmds["write"] = 0
		self.cmds["format_unit"] = 0
		self.cmds["inquiry"] = 0
		self.cmds["read"] = 0
		self.cmds["mode_sense"] = 0


		# signals and events
		self.ui.pushButton_3.setEnabled(False)
		self.ui.pushButton_4.setEnabled(False)
		self.ui.pushButton_5.setEnabled(False)
		self.ui.pushButton_7.setEnabled(False)
		self.ui.pushButton_8.setEnabled(False)
		self.ui.pushButton_9.setEnabled(False)
		self.ui.pushButton_10.setEnabled(False)
		self.ui.pushButton_11.setEnabled(False)
		self.ui.pushButton_12.setEnabled(False)
		self.ui.pushButton_13.setEnabled(False)
		self.ui.pushButton_14.setEnabled(False)
		self.ui.pushButton_15.setEnabled(False)
		self.ui.pushButton_16.setEnabled(False)
		       
		self.ui.pushButton_2.clicked.connect(self.connectToServer)
		self.ui.pushButton_3.clicked.connect(self.checkDep(3))
		self.ui.pushButton_16.clicked.connect(self.checkDep(16))  # change
		self.ui.pushButton_11.clicked.connect(self.checkDep(11))
		self.ui.pushButton_15.clicked.connect(self.checkDep(15))
		self.ui.pushButton_4.clicked.connect(self.checkDep(4))
		self.ui.pushButton_9.clicked.connect(self.checkDep(9))
		self.ui.pushButton_7.clicked.connect(self.checkDep(7))
		self.ui.pushButton_8.clicked.connect(self.checkDep(8))
		self.ui.pushButton_12.clicked.connect(self.checkDep(12))
		self.ui.pushButton_5.clicked.connect(self.checkDep(5))
		self.ui.pushButton_13.clicked.connect(self.checkDep(13))
		self.ui.pushButton_14.clicked.connect(self.checkDep(14))
		self.ui.pushButton_10.clicked.connect(self.checkDep(10))
	
		
		#change
		self.ui.pushButton_99.clicked.connect(self.clrScr)
		self.s.readyRead.connect(self.readFromServer)
		self.s.stateChanged.connect(self.validate)
		self.s.error.connect(self.checkError)
		self.s.disconnected.connect(self.serverHasStopped)
		
		#self.cmds = {}
		
	def clrScr(self):
		self.ui.textBrowser.clear()

	def validate(self):
		if self.s.state() == 1 :
			self.ui.textBrowser.append("Hostlookup state")
		elif self.s.state() == 2 :
			self.ui.textBrowser.append("Connecting state")
		elif self.s.state() == 3 :
			self.ui.textBrowser.append("Connected state")


	def checkError(self):
		self.ui.textBrowser.append("Error : " + str(self.s.error()))
		self.s.close()
		self.ui.pushButton_2.setEnabled(True)
		self.ui.pushButton_3.setEnabled(False)
		self.ui.pushButton_4.setEnabled(False)
		self.ui.pushButton_5.setEnabled(False)
		self.ui.pushButton_7.setEnabled(False)
		self.ui.pushButton_8.setEnabled(False)
		self.ui.pushButton_9.setEnabled(False)
		self.ui.pushButton_10.setEnabled(False)
		self.ui.pushButton_11.setEnabled(False)
		self.ui.pushButton_12.setEnabled(False)
		self.ui.pushButton_13.setEnabled(False)
		self.ui.pushButton_14.setEnabled(False)
		self.ui.pushButton_15.setEnabled(False)
		self.ui.pushButton_16.setEnabled(False)


	def connectToServer(self):
		# Validate Host Address and Port
		if self.is_number(self.ui.lineEdit_3.text()) :
			self.s.connectToHost(str(self.ui.lineEdit_2.text()), int(self.ui.lineEdit_3.text()))
			self.ui.pushButton_2.setEnabled(False)
			self.ui.pushButton_3.setEnabled(True)
			self.ui.pushButton_4.setEnabled(True)
			self.ui.pushButton_5.setEnabled(True)
			self.ui.pushButton_7.setEnabled(True)
			self.ui.pushButton_8.setEnabled(True)
			self.ui.pushButton_9.setEnabled(True)
			self.ui.pushButton_10.setEnabled(True)
			self.ui.pushButton_11.setEnabled(True)
			self.ui.pushButton_12.setEnabled(True)
			self.ui.pushButton_13.setEnabled(True)
			self.ui.pushButton_14.setEnabled(True)
			self.ui.pushButton_15.setEnabled(True)
			self.ui.pushButton_16.setEnabled(True)
			# to check state
			self.ui.textBrowser.append("state : " + str(self.s.state()))

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False
		
	def check(self,dep_list):
		not_exec = []
		for i in dep_list:
			if self.cmds[i] == 0:
				not_exec.append(i)
		return not_exec
	
	def checkDep(self,a):
		
		if a==3 :

			def checkedCdb():
				
				dep_list = ["format_unit","report_luns"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(3)
					sendCdb()
		elif a==4 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns","start_stop"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(4)
					sendCdb()
		
		elif a==5 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(5)
					sendCdb()
		
		elif a==7 :
			def checkedCdb():
				dep_list = ["format_unit"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(7)
					sendCdb()
		
		elif a==8 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns","start_stop","mode_sense"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(8)
					sendCdb()
		elif a==9 :
			def checkedCdb():
				dep_list = []
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(9)
					sendCdb()
		
		elif a==10 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns","start_stop"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(10)
					sendCdb()
		
		elif a==11 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns","start_stop","inquiry"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(11)
					sendCdb()
		
		elif a==12 :
			def checkedCdb():
				dep_list = []
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(12)
					sendCdb()
		
		elif a==13 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns","start_stop","read_cap","tur"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(13)
					sendCdb()
		
		elif a==14 :
			def checkedCdb():
				dep_list = []
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(14)
					sendCdb()
			
		elif a==15 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(15)
					sendCdb()
		elif a==16 :
			def checkedCdb():
				dep_list = ["format_unit","report_luns","start_stop","read_cap","tur"]
				res = self.check(dep_list)
				if(len(res) != 0):
					QtGui.QMessageBox.warning(self,"Command Status","These commands should be executed "+str(res))	
				else:
					sendCdb=self.createCdb(16)
					sendCdb()
		
			
		return checkedCdb				
			

	def createCdb(self,a):
	#change
		if(a==16):
			def sendCdb():
				self.cmds["read"] = 1;
				w = ReadPopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write( (str(cdb)))
		elif(a==11):
			def sendCdb():
				self.cmds["read_cap"] = 1;
				w = ReadCapPopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write( (str(cdb)))
		elif(a==15):
			def sendCdb():
				self.cmds["inquiry"] = 1;
				w = InquiryPopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				
				self.s.write( (str(cdb)))
			
		elif(a==4):
			def sendCdb():
				self.cmds["send_diag"] = 1;
				w = SendDiagPopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				
				self.s.write( (str(cdb)))

		elif(a==9):
			def sendCdb():
				self.cmds["req_sense"] = 1;
				w = reqSensePopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				
				self.s.write( (str(cdb)))

		elif(a==7):
			def sendCdb():
				self.cmds["report_luns"] = 1;
				w = ReportLunsPopup()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write( (str(cdb)))
		
		elif(a==8):
			def sendCdb():
				self.cmds["mode_sel"] = 1;				
				w = ModeSelPopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write( (str(cdb)))
		
		elif(a==5):
			def sendCdb():
				self.cmds["start_stop"] = 1;
				w = startStopPopUp()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write( (str(cdb)))

		elif(a==12):
			
			def sendCdb():
				self.cmds["log_sense"] = 1;
				w = LogsensePopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				
				self.s.write( (str(cdb)))
		
		elif(a==13):
			def sendCdb():
				self.cmds["write"] = 1;
				w = write_command.writePopUp()
				w.exec_()
				cdb = w.getCdb()
				self.s.write(str(cdb))
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()

		elif(a==3):
			def sendCdb():
				self.cmds["tur"] = 1;
				w = TurPopup()
				w.exec_()
				cdb=w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write( (str(cdb)))		
		elif(a==14):
			def sendCdb():
				self.cmds["format_unit"] = 1;
				cdb =format_unit_cdb_init()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write(str(cdb))
		
		elif(a==10):
			def sendCdb():
				self.cmds["mode_sense"] = 1;
				w = ModeSensePopup()
				w.exec_()
				cdb = w.getCdb()
				disp = CDB()
				disp.show_cdb(cdb)
				disp.exec_()
				self.s.write(str(cdb))

		return sendCdb
	

	def readFromServer(self):
		rply = self.s.readLine(10000)
		if(rply == None):
			pass
		elif rply[0] == '{':
			reply=eval(rply)
			if( "read" in reply.keys()):  #for read command
				self.ui.textBrowser.append(reply["read"])

			elif ("pageCodeValidity" in reply.keys()) and (reply["pageCodeValidity"]==1):
				if reply["saveLogs"]=="0":
					#just display reply["logData"] on the gui
					self.ui.textBrowser.append(str(reply["logData"]))
				elif reply["saveLogs"]=="1":
					#open a file and 
					wfile = open("mylog.dat","w")
					logs = reply["logData"]
					wfile.write(logs)
					self.ui.textBrowser.append("\nLog file (mylog.dat) has been updated")
				else:
					fs = open("sense.dat","w")
					fs.write("LOG_SENSE FAIL 5") 
					fs.close()
					self.ui.textBrowser.append("\nINVALID SP BIT")
			
			elif reply.has_key("cmd"):
				if reply["cmd"] == "write" and reply["status"] == "received":
					buf = "response for write command received.\n"
					buf += "beginning file transfer."
					self.ui.textBrowser.append(buf)
					write_cdb = eval(reply["cdb"])
					f_handler = write_command.clientFileHandler(reply)
					write_cdb["content"] = str(f_handler.buffer)
					self.s.write(str(write_cdb))
			else:
				disp = CDB()
				disp.show_cdb(reply)
				disp.exec_()
				#self.ui.textBrowser.append(str(rply))	#disply cdb
		else:
			QtGui.QMessageBox.information(self,"Command Status",str(rply))

	def serverHasStopped(self):
		self.s.close()
		self.ui.pushButton_2.setEnabled(True)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
