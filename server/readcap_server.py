from write_log import *
#what should be done at the server.
def target_response(cdb):
	
	fs = open("sense.dat","w")
	if int(cdb["pmi"][0]) > 1: 
		fs.write("READ_CAPACITY FAIL 11") 
		fs.close()
		write_log("READ_CAPACITY","FAILED")
		return "INVALID PMI"
	
	elif int(cdb["pmi"][0]) == 0 and int(cdb["LBA"][0]) == 0: 
		read_cap_res={}
		read_cap_res["returnedLBA"]=["400",0,7,32]
		read_cap_res["block_length"]=["100",4,7,32]
		write_log("READ CAPACITY","SUCCESSFUL")
		return read_cap_res;
		
	elif int(cdb["pmi"][0]) == 0 and int(cdb["LBA"][0]) != 0: 
		fs.write("READ_CAPACITY FAIL 5") 
		fs.close()
		write_log("READ_CAPACITY","FAILED")
		return "INVALID LBA"
	
	
	elif int(cdb["pmi"][0]) == 1:
		read_cap_res={}
		read_cap_res["returnedLBA"]=["400",0,7,32]
		read_cap_res["block_length"]=["100",4,7,32]
		write_log("READ CAPACITY","SUCCESSFUL")
		return read_cap_res;
		
