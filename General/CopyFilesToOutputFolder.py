####################################################################################################################


##COPY MP3s (or other file types) TO OUTPUT FOLDER
##Copies all .mp3 (or other file type) files within the folder 'SourceFolder' and all of its 
## subfolders to the folder 'OutputFolder'
#
#
##If the files already exist in the output folder, they will be copied over (replaced)
#
#
##Requires Python 2.7 Installation
##For Python 3.4, the print statements must be changed to print("message")
#
#
##To run, edit the values below for source folder, output folder, and file type(s), save the file and run with cmd
#
#
##This can take between seconds and several hours to run depending on the amount and size of the
## files in the source folder
#
#
##Created by Jason Balkenbush 31 March 2016
##Last Updated 27 December 2017
##Updates:  Cleaned up formatting; added functionality to search for a list of file types;


#=====================================================================================================================
#=====================================================================================================================

##Change this to the path of your source folder (the 'r' specifies raw text.  Include this or escape your slashes)
SourceFolder = r"C:\temp" # or "C:\\temp"

##Change this to the path of your output folder
OutputFolder = r"C:\temp\test"

##Change this to match the file type or types that you want to copy
##Edit this list to include or remove file types (i.e. FileTypes = [".mp4",".wav",".xlsx",".txt",".docx",".jpg"])
FileTypes = [".mp3"]

#=====================================================================================================================
#=====================================================================================================================


def copyFiles(source, output, types):
	print "Source: {}; Output: {}; Types: {}".format(source,output,",".join(types))
	import shutil
	import os
	FileList = []
	for root, folders, files in os.walk(source):
		for file in files:
			if os.path.splitext(file)[1] in types: 
				FileList.append(os.path.join(root,file))
	for file in FileList:
		print  "{} copied to {}".format(file, output)
		shutil.copy2(file,output)
	if len(FileList) > 0: 
		print "All {} files copied!".format(",".join(types))
	else:
		print "No {} files found!".format(",".join(types))

if __name__ == "__main__":
	copyFiles(SourceFolder,OutputFolder,FileTypes)
#
#
####################################################################################################################