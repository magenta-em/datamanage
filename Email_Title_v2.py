import os
import arrow
import pyperclip as pc

def main():
	
	root = "/Volumes/ARECA_88TB/SONIC3/"
	today = arrow.now().format('YYYYMMDD')
	today_sd = ""
	
	for sd in os.listdir(root):
		if sd[:8] == today:
			today_sd = sd
			print(today_sd," is your shootday")
	
	if sd == "":
		print("No Shootday found")			
	
	title = "SONIC 3 | " + today_sd + " Data Reports"
	pc.copy(title)
	print(title)
	

if __name__ == "__main__":
	main()