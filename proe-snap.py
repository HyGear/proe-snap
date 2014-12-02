'''
This script was written to aid in the creation of snapshots for Pro/E. When
Pro/E saves a file, it saves a copy of the file and increments the extension
number. For example, the 3rd save of somepart.prt would be somepart.prt.3.

To use the script, enter the working directory and execute. A snapshot with
the highest revision of each part will be saved to a folder with the current
timestamp.
'''
#Setup modules
import os.path
import shutil
from os import listdir
from os.path import isfile, join, basename
from datetime import datetime

#Setup variables
start_dir = os.getcwd().replace("\\","\\\\") + "\\\\"
ext_list = [".asm",".drw",".prt"]
purge_list = {}
new_list = []
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
snap_dir = start_dir+timestamp

# Helper functions
def copyFile(src,dest):
	try:
		shutil.copy(src, dest)
    # eg. src and dest are the same file
	except shutil.Error as e:
		print('Error: %s' % e)
    # eg. source or destination doesn't exist
	except IOError as e:
		print('Error: %s' % e.strerror)

def makeList():
	global start_dir,ext_list,purge_list,new_list,snap_dir
	#Generate a list of files by listing the directory and checking if it is a file.
	files = [ f for f in listdir(start_dir) if isfile(join(start_dir,f))]
	#Read files from start_dir and place in a dictionary with filename and empty list pair.
	for f in files:
		temp = os.path.splitext(os.path.basename(f)) 	# Get the filename from the file path and split it into a filename + extension
		#if key in array
		#Check if the file is a valid extension.
		if temp[0][-4:] in ext_list:
			if temp[0] in purge_list:
				if temp[1][1:] > purge_list[temp[0]]:
					purge_list[temp[0]] = temp[1][1:]
			else:
				purge_list[temp[0]] = temp[1][1:]

   
    #Generate a new list from the key
	for x in purge_list:
		new_list.append(x+"."+purge_list[x])

    #Sort the purge list into a new sorted list.
	new_list = sorted(new_list)


def ChkSnapDir(snap_dir):
    #Check to see if a directory should be made.
    if not os.path.isdir(snap_dir):
        print "We need to create a directory"
        os.makedirs(snap_dir)
    else:
        print "Directory exists"

def Main():
	global new_list,start_dir,snap_dir
	ChkSnapDir(snap_dir)
	makeList()
	for z in new_list:
		basename = os.path.splitext(z)[0]
		src = start_dir+basename+".1"
		copyFile(src,snap_dir)
	
if __name__ == "__main__":
    Main()
