#! usr/bin/python 2.7
# filename : write_c.py

from PyQt4 import QtGui,QtCore
import sys
import os
def main():
	app = QtGui.QApplication(sys.argv)
	w = writePopUp()
	w.exec_()
class writePopUp(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.cdb = dict()	
		self.ui = writeUI()
		self.ui.setupUI(self)
		self.show()
		self.ui.ok_button.clicked.connect(self.createWriteCdb)
	def createWriteCdb(self):
		try:
			if self.ui.lun_edit.text() == '' or self.ui.lba_edit.text() == '' or self.ui.tl_edit.text() == '':
				self.warning("one of the fields were left empty")
			if int(self.ui.lun_edit.text()) <= 0:
				self.warning("Logical Unit Number cannot be less than zero. (1-5)")
			elif int(self.ui.lun_edit.text()) > 5:
				self.warning("Logical Unit Number cannot be greater than 5. (1-5)")
			elif int(self.ui.lba_edit.text()) <= 0:
				self.warning("Logical Block Number cannot be less than zero. (1-5)")
			elif int(self.ui.lba_edit.text()) > 5:
				self.warning("Logical Block Number cannot be greater than 5. (1-5)")
			elif int(self.ui.tl_edit.text()) < 0:
				self.warning("Transfer length cannot be less than zero")
			self.validate_transferlength()
			self.cdb['operationCode'] = [0x0A,0,7,8]
			self.cdb['reserved'] = ['reserved',1,7,3]
			self.cdb['msb'] = ['msb',1,4,5]
			self.cdb['LUN'] = [int(self.ui.lun_edit.text()),2,7,8]
			self.cdb['LBA'] = [int(self.ui.lba_edit.text()),3,7,16]
			self.cdb['transferLength'] = [int(self.ui.tl_edit.text()),5,7,8]
			self.cdb['control'] = ['control',6,7,8]
			self.close()
		except TypeError, e:
			QtGui.QMessageBox.warning(self,"Error","Invalid arguments.. the arguments must be integers")
		except ValueError, e:
			pass
	def warning(self,warning_message):
		QtGui.QMessageBox.warning(self,"Error",warning_message)
		self.ui.lun_edit.setText('')
		self.ui.lba_edit.setText('')
		self.ui.tl_edit.setText('')
	def getCdb(self):
		return self.cdb
	def validate_transferlength(self):
		tl_related_to_luns = dict([(1,25),(2,20),(3,15),(4,10),(5,5)])
		max_possible_tl = tl_related_to_luns[int(self.ui.lun_edit.text())] - int(self.ui.lba_edit.text()) + 1
		if max_possible_tl < int(self.ui.tl_edit.text()):
			self.warning("transfer length exceeds maximum limit. maximum value is " + str(max_possible_tl))
class writeUI(object):
	"""class for defining the ui for write"""
	def __init__(self):
		super(writeUI, self).__init__()
	def setupUI(self,dialog):
		self.lun_edit = QtGui.QLineEdit(dialog)
		self.lba_edit = QtGui.QLineEdit(dialog)
		self.tl_edit = QtGui.QLineEdit(dialog)
		self.ok_button = QtGui.QPushButton('&Submit',dialog)
		dialog.setLayout(self.buildLayout())
		dialog.setWindowTitle("Enter the form fields")
		dialog.resize(400,130)
		dialog.move(300,300)
	def buildLayout(self):
		form_layout = QtGui.QFormLayout()
		form_layout.addRow("Logical Unit Number",self.lun_edit)	
		form_layout.addRow("Logical Block Address",self.lba_edit)
		form_layout.addRow("Transfer Length",self.tl_edit)	
		form_layout.addRow("Submit",self.ok_button)
		return form_layout
class clientFileHandler(object):
	"""docstring for clientFileHandler"""
	def __init__(self,d):
		super(clientFileHandler, self).__init__()
		self.desc = d
		self.file_name = self.choose_file()
		self.buffer = self.get_content()
	def choose_file(self):
		if os.path.exists("C:\\"):
			file_name = QtGui.QFileDialog.getOpenFileName(caption="Select a file",directory="C:\\")
		elif os.path.exists("/home"):
			file_name = QtGui.QFileDialog.getOpenFileName(caption="Select a file",directory="/home")
		write_cdb = eval(self.desc["cdb"])
		stat_struct = os.stat(file_name)
		if write_cdb["transferLength"][0] * 100 > int(stat_struct.st_size):
			msg = "transfer length exceeds the file size."
			msg += "\ntransfer length choosen was " + str(write_cdb["transferLength"][0] * 100) + " (transferlength * 100) and file size was " + str(int(stat_struct.st_size))
			msg += "\nselected file size must be greater than the transfer length"
			QtGui.QMessageBox.warning(QtGui.QDialog(),"Error",msg)
			self.choose_file()
		return file_name
	def get_content(self):
		fobj = open(self.file_name,"r")
		n_bytes = eval(self.desc["cdb"])["transferLength"][0] * 100
		return fobj.read(n_bytes)
class serverFileHandler(object):
	"""docstring for serverFileHandler"""
	def __init__(self,cdb):
		super(serverFileHandler, self).__init__()
		self.cdb = cdb 
	def write_content(self):
		present_lun = self.cdb["LUN"][0]
		present_lba = self.cdb["LBA"][0]
		no_lba_remaining = 5 - present_lba + 1
		count = 0
		flag = 0
		while count < int(self.cdb["transferLength"][0]) and present_lun <= 5:
			if no_lba_remaining > 0:
				fobj = open("file" + str(present_lun) + ".txt","a")
				if not flag:
					fobj = open("file" + str(present_lun) + ".txt","w")
					fobj.seek((present_lba - 1) * 100)
					flag = 1
				else:
					fobj.seek(0,1)
				fobj.write(self.cdb["content"][count * 100:(count + 1) * 100])
				no_lba_remaining -= 1	
				present_lba += 1
				fobj.close()
			else:
				flag = 0
				no_lba_remaining = 5
				present_lun += 1
				present_lba = 1
				count -= 1
			count += 1
		print "file transfer complete"
if __name__ == '__main__':
	main()
