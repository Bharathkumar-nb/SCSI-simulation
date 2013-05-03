from write_log import *
#what should be done at the server.
def logsense_response(logsense_cdb): 
	write_log("LOGSENSE","STARTED")
	savelogs = logsense_cdb["sp"][0]
	pcode = logsense_cdb["pageCode"][0]
	valid = 1
	data = ""
	resp = {}
	if pcode!=0x31:
		valid = 0
		resp["pageCodeValidity"] = valid
		
	else:	
		lfile = open("log.dat","r")
		data = lfile.read()
		resp["saveLogs"] = savelogs
		resp["logData"] = data
		resp["pageCodeValidity"] = valid
		
	write_log("LOGSENSE","SUCCESSFUL")
	return str(resp)

