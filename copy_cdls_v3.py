import os
import re
import shutil
import arrow

def main():
	#Define Variables
	cdls = "CDL1", "CDL2", "CDL3", "CDL4", "CDL5", "CDL6", 
	today = arrow.now().format('YYYYMMDD')
	sd = []
	areca = "/Volumes/ARECA_88TB/SONIC3/"
	usb = "No USB mounted"
	
	#Find USB
	for cdl in cdls:
		if os.path.ismount(os.path.join("/Volumes/",cdl)):
			usb = os.path.join("/Volumes/",cdl)
	print(usb)
	
	#Find Shootday
	for dir in os.listdir(areca):
		if dir[:8] == today:
			sd.append(dir)
			print(dir)
	if len(sd) > 1:
		print("Multiple shootdays created today - please copy manually\nOr update your script")
		#!!!WORKING AREA!!!
		
		exit()
	
	#Define base dest for CDLs
	copy_dest = os.path.join(areca,sd[0],"CDL")
	
	#Work out if Split folders exist or not for copy dest
	split_dest = os.path.join(copy_dest, "SPLIT")
	if os.path.isdir(split_dest):
		if len(os.listdir(split_dest)) == 0:
			#No files in the split folder, so we should use the split folder as our copy location
			copy_dest = split_dest
		if len(os.listdir(split_dest)) != 0:
			copy_dest = os.path.join(areca,sd[0],"CDL/EOD")
	
	
	#Execute copy files from USB
	for root, dirs, files in os.walk(usb):
		print("Copying CDLs and stills to " + copy_dest)
		for file in files:
			if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".cdl"):
				shutil.copy(os.path.join(root,file), copy_dest)
				print("Copied to ARECA: ", file)

if __name__ == "__main__":
	main()
