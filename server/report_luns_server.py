from write_log import *
import os
import re

def reportLunsServer(cdb):
	write_log("REPORT LUNS","STARTED")
	rep_luns = {}
	rep_luns["reserved"] = ["reserved", 4, 7,32]
	rep_luns["lun1"] = []
	i, count = 0, 0
	update_inventory()
	luns = read_inventory()
	for lun in luns:
			i += 1
			rep_luns["lun" + str(i)] = [int(lun), 8+count, 7, 16]
			count += 2
	if rep_luns["lun1"] == []:
		rep_luns["lun1"] = ["empty", 8, 7, 8]
	rep_luns["length"] = [i*8,0 ,7 ,32]
	write_log("REPORT LUNS","SUCCESSFUL")

	return rep_luns

def read_inventory():
	x = []
	f = open("logical_unit_inventory.txt","r")
	for line in f.readlines():
		words = line.split(" ")
		x.append(words[0])
	f.close()
	return x

def update_inventory():
	os.chdir(".")
	i, count = 0, 0
	f = open("logical_unit_inventory.txt","w")
	for files in os.listdir("."):
		if re.search('file([0-9]+)\.txt$', files):
			i += 1
			files = files.strip(".txt")
			files = files[4:]
			open("logical_unit_inventory.txt")
			
			f.write(files + "   000b\n")
			count += 2

