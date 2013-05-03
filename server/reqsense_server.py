from write_log import *

def receive_request_sense(s):
	write_log("REQUEST SENSE","STARTED")
	f=open("sense.dat","r")
	line = f.readline()
	line = line.strip()
	line = line.split()
	if(len(line) == 0):
		return "ALL_CMDS_SUCCESSFUL"

	command_name=line[0]
	status=line[1]
	sense_key=line[2]
	desc=s["desc"][0]
	if(desc=='0'):	
		send1={}
		send1["valid"]=[1,0,7,1]
		res_code=0x71   #current error , fixed format
		send1["response_code"]=[res_code,0,6,7]
		send1["reserved_1"]=["reserved",1,7,8] #segment number (obsolete)
		send1["reserved_2"]=["reserved",2,7,2]
#ILI - incorrect length indicator - 1 = requested logical block length did not match the logical block length of the data on the medium
		ili=0
		send1["ili"]=[ili,2,5,1]
		send1["reserved_3"]=["reserved",2,4,1]
          # 2 5 11
		asc=00	
		ascq=00
		if(sense_key=='2'):
                        emsg = 'ERROR MESSAGE: NOT READY'
			asc=04  #cause not reportable
			ascq=00
		elif(sense_key=='5'):
			emsg =  'ERROR MESSAGE: ILLEGAL REQUEST'
                      	asc=20 #invalid/unsupported command
			ascq=00
		elif(sense_key=='11'):
			emsg = 'ERROR MESSAGE: ABORTED COMMAND'
                      
			asc=00   #no additional sense code
			ascq=00
        	send1["sensekey"]=[sense_key,2,3,4]
		send1["information"]=[status,3,7,32]
		#additional sense length
		send1["additional_sense_length"]=[0,7,7,8]
		send1["command_sp_info"]=[command_name,8,7,32]
		send1["asc"]=[asc,12,7,8]
		send1["ascq"]=[ascq,13,7,8]
		send1["field replaceable unit code"]=["unit_code",14,7,8] #optional
		#    0 - sense key specific data are not SCSI compliant
		#   1 - sense key specific data are SCSI compliant
		send1["sksv"]=[1,15,7,1]
		send1["sense key specific 1"]=[emsg,15,6,7]
		send1["sense key specific 2"]=[emsg,16,7,16]
		#additional sense bytes
		send1["asb"]=["vendor specific",18,7,8]
		write_log("REQUEST SENSE","SUCCESSFUL")
		return str(send1)

	elif(desc=='1'):
		send2={}
		send2["reserved"]=["reserved",0,7,1]
		res_code=0x73 #current error , descriptor format
		send2["response_code"]=[res_code,0,6,7]
		send2["reserved1"]=["reserved",1,7,4]
		asc=00	
		ascq=00
		if(sense_key=='2'):
                        emsg = 'ERROR MESSAGE: NOT READY'
			asc=04  #cause not reportable
			ascq=00
		elif(sense_key=='5'):
			emsg =  'ERROR MESSAGE: ILLEGAL REQUEST'
                       
			asc=20 #invalid/unsupported command
			ascq=00
		elif(sense_key=='11'):
			emsg = 'ERROR MESSAGE: ABORTED COMMAND'
                        
			asc=00   #no additional sense code
			ascq=00
		send2["sensekey"]=[sense_key,1,3,4]
		send2["asc"]=[asc,2,7,8]
		send2["ascq"]=[ascq,3,7,8]
		send2["reserved2"]=["reserved",4,7,24]
		send2["additional_sense_length"]=[0,7,7,8] 
		send2["sense_data_descriptor"]=[emsg,8,7,8]#not sure
		write_log("REQUEST SENSE","SUCCESSFUL")
		return str(send2)

#what should be done at the server.

