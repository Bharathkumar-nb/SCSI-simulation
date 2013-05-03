import os,sys, re


class ReportLunsPopup:
	def __init__(self):
		self.rep_luns = {}
		self.report_lun_client();
		

	def report_lun_client(self):
		
		self.rep_luns["operationCode"] = [0xA0,0,7,8]
		self.rep_luns["reserved1"] = ["reserved",1,7,8]
		self.rep_luns["select_report"] = [0x00,2,7,8]
		self.rep_luns["reserved2"] = ["reserved",3,7,24]
		self.rep_luns["allocation_length"] = [32,6,7,32]
		self.rep_luns["reserved3"] = ["reserved",10,7,8]
		self.rep_luns["control"] = ["control",11,7,8]
	
	def getCdb(self):
		return self.rep_luns

