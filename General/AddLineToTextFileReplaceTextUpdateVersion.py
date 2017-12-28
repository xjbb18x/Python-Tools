## Jason Balkenbush 24/10/2017
## Program to copy and replace text in multiple files and insert text based on the index of unique line of text in the file
## Useful for editing multiple .py modules (add a line after a certain line, replace a certain line with another, etc.)
## I used this to modify 35 modules used to create feature classes.  I removed and added fields to all modules as necessary.

import os
import shutil

# Source Folder
sfold = r"C:\temp"
# Archive Folder
afold = r"C:\temp\archive"
# File Type (Only works for text files)
ftype = ".py"
# Current Version of the Files
pver = "1.0"
# New Version of the Files
ver = "1.1"
# Text to find to use as an index
index = "def randoFunction():\n"
# Position to insert the new text (before or after the index text:  1 = 1 after, -1 = 1 before, 3 = 3 after, etc.)
pos = 1
# New line of text to insert based on index and pos
ins = "  print 'random function in progress'\n"
# Line of text to find to be replaced 1
find1 = "  print 'tomato'\n"
# Line of text that will replace find 1
repl1 = "  print 'carrot'\n"
# Line of text to find to be replaced 2
find2 = "  print 'spud'\n"
# Line of text that will replace find 2
repl2 = "  print 'potato'\n"


##USING THE EXAMPLE TEXT ABOVE ASSUMING THE .PY FILE LOOKS LIKE THIS:
#def randoFunction():
#  print "tomato"
#  print "spud"
##RESULTING FILE LOOKS LIKE:
#def randoFunction():
#  print 'random function in progress'
#  print 'carrot'
#  print 'potato
##

def __main__():
	# List files in source folder
	flist = []
	for root, dir, files in os.walk(sfold):
		for x in files:
			if os.path.splitext(x)[1] == ftype:
				flist.append(x)

	# Remove non-.py files from file list
	for f in flist:
		if f in ["blah.py","foo.py"]:  # edit this list to include specific files that you do not want to process
			flist[:] = [x for x in flist if x != f]
	print flist

	# Main program - copy current file to archive folder, suffix filename with pver then update current file with new field and new version
	for file in flist:
		# New file path for archive
		nf = os.path.splitext(file)[0] + "_{}_{}{}".format(pver.split(".")[0],pver.split(".")[1],ftype)
		# Copy files to archive using new path
		shutil.copy2(os.path.join(sfold,file),os.path.join(afold,nf))
		# Open current file and read contents to list
		f = open(os.path.join(sfold,file),'r')
		lines = f.readlines()
		f.close()
		# Find and replace with dictionary
		dict = {find1:repl1, find2:repl2}
		lines = [dict[n] if n in dict else n for n in lines]
		# Find index text
		if index in lines:
			i = lines.index(index)
		# Insert new text if not already existing
			if ins not in lines:
				lines.insert(i+pos,ins)
		else:
			print "Index line not found in {}".format(file)
		# Write new contents to file
		a = open(os.path.join(sfold,file),'w')
		a.writelines(lines)
		a.flush()
		a.close()


if __name__ == '__main__':
	__main__()
	
	

