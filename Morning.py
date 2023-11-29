import os
import shutil
import arrow
import pyperclip as pc

def main():
	#make new folder structure
	today = arrow.now().format('YYYYMMDD')
	sd_num = input("What shootday is it? ")

	while len(sd_num) < 2:
		sd_num = "0" + sd_num
	
	shootday = today + "_MU_SD" + sd_num
	print(shootday)

	sd_path = os.path.join("/Volumes/ARECA_88TB/SONIC3/", shootday)
	
	#if not already a folder name
	if not os.path.isfile(sd_path):
		os.mkdir(sd_path)
		os.mkdir(os.path.join(sd_path, "CDL"))
		os.mkdir(os.path.join(sd_path, "CDL", "SPLIT"))
		os.mkdir(os.path.join(sd_path, "CDL", "EOD"))
		os.mkdir(os.path.join(sd_path, "REPORT"))
		
	pc.copy(shootday)

if __name__ == "__main__":
	main()