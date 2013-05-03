activeLun=[]
from write_log import *

def startStop(startStop):
	write_log("START/STOP","STARTED")
	lunNumber=int(startStop["LUN"][0])
	write_log("START/STOP","WORKING ON LUN "+ str(lunNumber))
	start=int(startStop["start"][0])
	loej=int(startStop["LOEJ"][0])
	immed=int(startStop["IMMED"][0])
	fp = open("sense.dat","w")
	if lunNumber > 5 or lunNumber < 1:
		fp.write("START/STOP FAIL 11")
		fp.close()
		write_log("START/STOP","FAILED")
		return "LUN does not exist"
	try:
		i=activeLun.index(lunNumber)
	except ValueError:
		i=-1
	if (activeLun==[] or i == -1) and start !=1:
		fp.write("START/STOP FAIL 2")
		fp.close()
		write_log("START/STOP","FAILED")
		return "Lun not started" #lun not started error
	if start == 0 and loej==0:
		activeLun.remove(lunNumber)
		write_log("START/STOP","stoping LUN")
	if start == 1 and loej==0:
		activeLun.append(lunNumber)
		write_log("START/STOP","staring LUN")
	if start == 0 and loej==1:
		write_log("START/STOP","ejecting media")
	if start == 1 and loej==1:
		write_log("START/STOP","loading media")
	if(immed==1):
		write_log("START/STOP","Before operation")
		return "StartStopUnit Successful before operation" #success status
	if(immed==0):
		write_log("START/STOP","After operation")
		return "StartStopUnit Successful After operation" #success status
	
