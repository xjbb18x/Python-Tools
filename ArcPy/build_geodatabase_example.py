#--------------------------------------------------------------------------- 
# Name:        build_geodatabase_example.py
#
# Purpose:     Creates an example geodatabase and feature class using modules
#              
#
#              
# Version:     1.0
# Author:      Jason Balkenbush
# Created:     05/10/2017
#
#
# Pre:
#
#				The output geodatabse must not exist or the program will fail.
#				This script works with modules that must be imported.  These modules must reside within the parent source code folder or a subfolder within.  If the modules reside within a subfolder,
#				a blank .py file with the filename __init__.py must exist within the subfolder or the modules will not import.
#				Modules are currently residing in the subfolder 'modules' and must be called as follows:  from modules import <module name>
#
# Params:   
#				gdbfold - output folder
#				gdbnam - output gdb name
#				gdbver - version of the output gdb - appended to the output name (i.e. gdbnam = "test" and gdbver = "1.1" yeilds "test_v1_1.gdb")
#				arcver - ArcGIS version settings for the output gdb (10.3, 9.3, etc.)
#				sr - spatial reference for output feature classes
#
# Run instructions: 	
#
#				all parameters are required, no special instructions for running			
#
# Issues?
#
#				speed of adding fields = slow
#
#
#--------------------------------------------------------------------------- 

import arcpy
import os
import sys
import time

# params
gdbfold = sys.argv[1]
gdbnam = sys.argv[2]
gdbver = sys.argv[3]
arcver = sys.argv[4]
sr = arcpy.SpatialReference(int(sys.argv[5]))

print "Params=", gdbfold, gdbnam, gdbver, arcver, sr

#-----------------------------------------
# setup and check log file
#-----------------------------------------
lname = "RCWP_Data_Dictionary_Q-03-101-DAT-L-0159_v" + gdbver.replace('.','_').replace(' ','_') + "_Log.log"
logfilename = os.path.join(gdbfold,  lname)
print 'logging to ' + logfilename + "\n"

try:
    if os.path.exists(logfilename):
        os.remove(logfilename)
    logfile = open(logfilename, 'w')
except WindowsError:
    print 'Windows Error - logfile or folder read-only?'
    sys.exit('logging not possible.  program abort.')
except IOError:
    print "Error: IOError"
    sys.exit('logging not possible.  program abort.')
    


#-----------------------------------------
# message log 
#-----------------------------------------
def log(message):
    """log message"""
    now = time.strftime("%Y%m%d %X")
    try:
        print message
        logfile.write('\n' + now + ' ' + str(message))
        logfile.flush()
    except IOError:
        print "Error: Log file IOError"


log("Begin main program")
		
#-----------------------------------------
# main		
#-----------------------------------------
# create gdb
#-----------------------------------------
from modules import geodatabase_module_example
outgdb = geodatabase_module_example.gdb(gdbfold,gdbnam,gdbver,arcver)
message = str(outgdb) + " created sucessfully"
arcpy.AddMessage(message)
log(message)


#-----------------------------------------
# Create example feature class
#-----------------------------------------
from modules import feature_class_module_example
example = feature_class_module_example.example_fc(outgdb,sr)
message = "example feature class added sucessfully"
arcpy.AddMessage(message)
log(message)
