import sys, os, math
from PyQt4.QtNetwork import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
#from cdbV4 import Ui_Form

class CDB(QtGui.QDialog):
	def __init__(self, parent=None):
		# setting up gui
		QtGui.QWidget.__init__(self, parent)
		self.resize(800,700)

		self.frame = QtGui.QFrame(self)
		self.gridLayoutWidget = QtGui.QWidget(self.frame)
		self.horizontalLayout = QtGui.QHBoxLayout(self.gridLayoutWidget)
		self.scrollArea = QtGui.QScrollArea(self.frame)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setWidget(self.gridLayoutWidget)
		

	def show_cdb(self, rep_luns):
		

		self.frame.setGeometry(QtCore.QRect(50, 30, 600, 500))
		self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName("frame")
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		self.horizontalLayout.setGeometry(QtCore.QRect(0, 0, 600, 500))
		#self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 600, 500))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.scrollArea.setGeometry(QtCore.QRect(0, 0, 600, 500))
		if not hasattr(self, 'gridLayout'):
			self.gridLayout = QtGui.QGridLayout()
		else :
			for i in range(self.gridLayout.count()): self.gridLayout.itemAt(i).widget().close()
		#self.gridLayout.setMargin(1)
		self.horizontalLayout.addLayout(self.gridLayout)
		self.gridLayout.setObjectName("gridLayout")
		self.gridLayout.setSpacing(0)

		i = 0
		self.mylabel = []
		for x in range(9):
			self.mylabel.append(QtGui.QLabel(self.gridLayoutWidget))
			self.mylabel[i].setAlignment(QtCore.Qt.AlignCenter)
			self.mylabel[i].setObjectName("mylabel"+str(i))
			if x==0:
				self.mylabel[i].setText("Bytes/Bits")
			else :
				self.mylabel[i].setText(str(8-x))
			self.mylabel[i].setStyleSheet("font-weight:bold; border-style:dotted; border-width:1px;margin:0px;")
			self.gridLayout.addWidget(self.mylabel[i], 0, x,1, 1)
			i += 1
		max_rows = 1
		for key,value in rep_luns.items():
			if max_rows<value[1]:
				max_rows = value[1]
			if isinstance(value[0], str) :
				self.mylabel.append(QtGui.QLabel(self.gridLayoutWidget))
				self.mylabel[i].setAlignment(QtCore.Qt.AlignCenter)
				self.mylabel[i].setObjectName("mylabel"+str(i))
				self.mylabel[i].setText(str(value[0]))
				self.mylabel[i].setStyleSheet("border-style:dotted; border-width:1px;margin:0px")
				self.mylabel[i].setToolTip("<font color='blue' >" + key + "</font>")
				if value[3]<8:
					self.gridLayout.addWidget(self.mylabel[i], value[1]+1, 8 - value[2],max(1,math.ceil(value[3]/8)), value[3])
				else :
					self.gridLayout.addWidget(self.mylabel[i], value[1]+1, 8 - value[2],max(1,math.ceil(value[3]/8)), 8)
				if max_rows<(value[1]+1+math.ceil(value[3]/8)):
					max_rows = value[1]+1+math.ceil(value[3]/8)
				i += 1
			else :
				j = 0
				r = 0
				c = 7 - value[2]
				#print(str(bin(value[0])[2:]))
				#temp = str(bin(value[0])[2:]).zfill(value[3])
				temp = "{0:#b}".format(value[0])[2:].zfill(value[3])
				for digit in temp:
					self.mylabel.append(QtGui.QLabel(self.gridLayoutWidget))
					self.mylabel[i].setAlignment(QtCore.Qt.AlignCenter)
					self.mylabel[i].setObjectName("mylabel"+str(i))
					self.mylabel[i].setText(digit)
					self.mylabel[i].setStyleSheet("border-style:dotted; border-width:1px;margin:0px")
					self.mylabel[i].setToolTip("<font color='blue' >" + key + "</font>")
					self.gridLayout.addWidget(self.mylabel[i], value[1]+1 + r, 1 + c + (j%8) ,1, 1)
					i += 1
					j += 1
					if ((7 - value[2]+j)%8) == 0 :
						r += 1
						c = 0
						if max_rows<value[1] + r+ 1 :
							max_rows = value[1] + r+ 1
		for x in range(int(max_rows-1)):
			self.mylabel.append(QtGui.QLabel(self.gridLayoutWidget))
			self.mylabel[i].setAlignment(QtCore.Qt.AlignCenter)
			self.mylabel[i].setObjectName("label_" + str(x))
			self.mylabel[i].setText(str(x))
			self.mylabel[i].setStyleSheet("font-weight:bold; border-style:dotted; border-width:1px;margin:0px")
			self.gridLayout.addWidget(self.mylabel[i], x+1, 0, 1, 1)
			i += 1


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())