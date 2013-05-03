def format_unit_cdb_init():
	cdb = {}
	cdb['operationCode'] = [0x04,0,7,8]
	cdb['fmtp_info'] = [0x00,1,7,2]
	cdb['long_list'] = [0x00,1,5,1]
	cdb['fmtdata'] = [0x00,1,4,1]
	cdb['cmplist'] = [0x00,1,3,1]
	cdb['defect_list_format'] = [0x00,1,2,3]
	cdb['vendor_specific'] = ['vendor_specific',2,7,8]
	cdb['obsolete'] = ['obsolete',3,7,16]
	cdb['control'] = ['control',5,7,8]

	return cdb


