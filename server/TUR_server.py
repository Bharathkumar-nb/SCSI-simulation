from write_log import *
import random

#server
def TurServer(cdb):
	write_log("TEST_UNIT_READY","STARTED")
	if(cdb["LUN"][0]>5):
		fs = open("sense.dat","w")
		fs.write("TEST_UNIT_READY FAIL 5") 
		fs.close()
		write_log("TEST_UNIT_READY","FAILED")
		return "Check Unit. LUN does not exist" 
	no=(random.randrange(1,10000))
	if (no%2!=0):
		write_log("TEST_UNIT_READY","SUCCESSFUL")
		return "SUCCESSFUL : UNIT IS RUNNING"
	else:
		fs = open("sense.dat","w")
		fs.write("TEST_UNIT_READY FAIL 5") 
		fs.close()
		write_log("TEST_UNIT_READY","FAILED")
		return "Check Unit. LUN is not functional"

