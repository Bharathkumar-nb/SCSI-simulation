from write_log import *

def create_inq_res_cdb():
	inq_res_cdb = {}
	inq_res_cdb["peripheral_qualifier"] = ["DEVICE_QUALIFIER_ACTIVE",0,7,3]  #The operating system supports the device, and the device is present.
	inq_res_cdb["peripheral_device_type"] = [0x00,0,4,5] #direct access device
	inq_res_cdb["RMB"] = [0,1,7,1]  #A removable medium (RMB) bit of zero indicates that the medium is not removable. A RMB bit of one 							indicates that the medium is removable.

	inq_res_cdb["device_type_modifier"] = [0,1,6,7]  #The device might or might not comply to an ANSI-approved standard. 
	inq_res_cdb["ISO_version"] = ["ISO",2,7,2] 
	inq_res_cdb["ECMA_version"] = ["ECMA",2,5,3]
	inq_res_cdb["ANSI_version"] = ["ANSI",2,2,3]  
	inq_res_cdb["AENC"] = [0,3,7,1]  #asynchronous event notification capability  --applicable to processor device type
	inq_res_cdb["trmIOP"] = [0,3,6,1] #supports Terminate I/O Process messages
	inq_res_cdb["reserved1"] = ["RESERVED",3,5,2]
	inq_res_cdb["response_data_format"] = ["000",3,3,4] #000=SCSI compliant
	inq_res_cdb["additional_length"] = [0,4,7,8]
	inq_res_cdb["reserved2"] = ["RESERVED",5,7,8]
	inq_res_cdb["reserved3"] = ["RESERVED",6,7,8]
	inq_res_cdb["RelAdr"] = [0,7,7,1] #this LUN supports Relative Addressing Mode 
	inq_res_cdb["WBus32"] = [1,7,6,1]  
	inq_res_cdb["WBUS16"] = [1,7,5,1]  #8, 16 or 32 bit
	inq_res_cdb["Sync"] = [0,7,4,1]  #SYNCHRONOUS is "sort of" Req/Ack
	inq_res_cdb["Linked"] = [0,7,3,1] #when multiple commands are issued to satisfy a single client request,the commands may be linked together as a scsi task 
	inq_res_cdb["reserved4"] = ["RESERVED",7,2,1]
	inq_res_cdb["CmdQue"] = [0,7,1,1] #SCSI command tag queuing refers to queuing multiple commands to a SCSI device.
	inq_res_cdb["SftRe"] = [0,7,0,1] #The reset condition is used to immediately clear all SCSI devices from the bus..Attempt to complete any I/O processes which have not completed and that were fully identified
	inq_res_cdb["vendor_id"] = ["YAMAHA",8,7,64]
	inq_res_cdb["prod_id"] = ["CRW-F1E",16,7,128]
	inq_res_cdb["prod_rev_level"] = ["1.0",32,7,32]
	inq_res_cdb["vendor_specific"] = ["vendor specific",36,7,160]  
	inq_res_cdb["reserved5"] = ["RESERVED",56,7,320]
	inq_res_cdb["vendor_specific_param"] = ["vendor specific",96,7,8] 
	
	return inq_res_cdb

def inquiry_target(cdb):
	write_log("INQUIRY","STARTED")
	fileNo = int(cdb["LUN"][0])
	fp = open("sense.dat","w")
	resp=None
	write_log("INQUIRY","WORKING ON LUN "+ str(fileNo))
	if(fileNo > 5): # 5- no of files(LU) on target
		fp.write("INQUIRY FAIL 11")
		
		resp = "INVALID LUN"
	else:	
		evpd = int(cdb["EVPD"][0])
		pageCode = int(cdb["pageCode"][0])
		if(evpd == 1):
			fp.write("INQUIRY FAIL 5")
			write_log("INQUIRY","FAILED")
		
			resp = "EVPD=1 NOT SUPPORTED"

		elif(evpd == 0 and  pageCode != 0): 
			fp.write("INQUIRY FAIL 5")
			write_log("INQUIRY","FAILED")
		
			resp = "INVALID PAGE CODE"
		else:
			resp = create_inq_res_cdb()
			write_log("INQUIRY","SUCCESSFUL")

	fp.close()
	return resp

