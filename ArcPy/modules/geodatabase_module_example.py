#--------------------------------------------------------------------------- 
# Name:        geodatabase_module_example.py
#
# Purpose:     Defines output geodatabase creation
#              
#
#              
# Version:     1.1
# Author:      Jason Balkenbush
# Created:     05/10/2017
#
#
# Params:   
#		gdbfold - output folder
#		gdbnam - output geodatabase name - spaces will be auto-removed
#		gdbver - output geodatabase version - spaces will be auto-removed
#		arcver - ArcGIS Version of GDB (10.3, 10.2, etc.)
#
# Run instructions: 
#					import geodatabase_module_example
#					gdb(gdbfold,gdbnam,gdbver,arcver)
#
# 
#
# 
#--------------------------------------------------------------------------- 

import arcpy

def gdb(gdbfold,gdbnam,gdbver,arcver):
	# fix gdb name and version to remove '.' and ' ' and replace with '_'
	name = gdbnam.replace('.','_').replace(' ','_') + "_v" + gdbver.replace('.','_').replace(' ','_')
	outgdb = arcpy.CreateFileGDB_management(gdbfold, name, arcver)
	return outgdb