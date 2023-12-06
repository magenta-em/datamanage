import os
import pyperclip as pc

def main ():
	#Define Variables
	sd_num = input("Which shootday? ")
	root = "/Volumes/ARECA_88TB/SONIC3/"
	sd_pot_dirs = []
	rolls_clean = []

	#Add number padding for SD's < 10
	while len(sd_num) < 2:
		sd_num = "0" + sd_num
		
	#Find directories with correct sd num
	for dname in os.listdir(root):
		path = os.path.join(root, dname)
		if os.path.isdir(path):
			if sd_num in dname[-4:]:
				sd_pot_dirs.append(dname)
	
	#User selection of correct shootday from list
	if len(sd_pot_dirs) > 1:
		print("Multiple Shootday Options\nPlease select from list:\n")
		counter = 1
		for sd in sd_pot_dirs:
			print(f"{counter}: {sd}")
			counter += 1
		sd_dir = sd_pot_dirs[int(input("Select your shootday:"))-1]
	#If there are no matching shootdays
	if len(sd_pot_dirs) < 1:
		print("Shootday folder doesn't exist")
		exit()
	#Only one possible shootday
	if len(sd_pot_dirs) == 1:
		sd_dir = sd_pot_dirs[0]
	
	print("Your shootday: ", sd_dir)
	rolls_path = os.path.join(root,sd_dir,"CAMERA")

	#Pulling roll info from directories
	for roll in os.listdir(rolls_path):
		if not "." in roll:
			rolls_clean.append(roll[:6])
	rolls_clean = sorted(rolls_clean)
	rolls_string = '\n'.join(str(a) for a in rolls_clean)
	
	print(*rolls_clean, sep="\n")
	#pc.copy(rolls_string)

	#WORKING AREA!!
	#Make email body
	bold = ""
	bold_stop = ""
	email_body = f"Hello,\n\nFootage from {bold}{sd_dir}{bold_stop} will arrive at Company3 on {bold}Shuttle 0 & Shuttle 0{bold_stop}.\n\n{bold}Rolls:{bold_stop}\n{rolls_string}\n\n{bold}Total Time: {bold_stop}00:00:00\n{bold}Total Data: {bold_stop} TB"
	pc.copy(email_body)

if __name__ == "__main__":
	main()
