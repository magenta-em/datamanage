import os
import arrow

def main():
	findShootday("/Users/download/Desktop/ARECA_88TB/SONIC3/")

def findShootday(base):
	today = arrow.now().format('YYYYMMDD')
	today_dirs = []
	yday_dirs = []
	today_sd = ""
	
	while today_sd == "":
 		for dir in os.listdir(base):
 			if dir[:8] == today:
 				today_dirs.append(dir)
 				print(dir)
 		if len(today_dirs) > 1:
 			print("Multiple Shootdays made today")
 			#while today_sd == "":
 			#work out how to find the most up to date shootday for today
 		if len(today_dirs) == 1:
 			today_sd = today_dirs[0]
 		if len(today_dirs) < 1:
 			print("No shootdays made today, assuming nightwork")
 			yesterday = arrow.now().shift(days=-1).format('YYYYMMDD')
 			if dir[:8] == yesterday:
 				yday_dirs.append(dir)
 			if len(yday_dirs) > 1:
 				print("Multiple shootdays yesterday, unclear selection")
 			if len(yday_dirs) < 1:
 				print("No shootdays today or yesterday, unclear process.\nExiting")
 				exit()
 			if len(yday_dirs) == 1:
 				today_sd = yday_dirs[0]
				
	print("Your shootday is: " + today_sd)
	return today_sd
		

if __name__ == "__main__":
	main()
