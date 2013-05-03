import time
def write_log(command_name,msg ):
	lfile = open("log.dat","a")
	lfile.write(command_name+"..."+msg+"..."+ time.ctime() + '\n')
	lfile.close()
