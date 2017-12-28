## Tables to Domains
## Jason Balkenbush 28 December 2017
# create domains in a geodatabase using tables from a geodatabase
# works through the python window in arcmap or as a standalone script

import arcpy
import os
import time

#geodatabase to receive the domains
wksp = r"C:\temp\test.gdb"
#geodatabase containing tables defining the domains
dgdb = r"C:\temp\domains.gdb"
# code field
cf = "code"
# description field
df = "description"

# start data and time
start = time.strftime("%Y%m%d %X")

# create list of domains (dlist) and list of tables with numeric description field (fixlist)
dlist = []
fixlist = []
for dirpath, dirnames, filenames in arcpy.da.Walk(dgdb, datatype="Table"):
	for filename in filenames:
		dlist.append(filename)
		if "_mm" in filename:
			fixlist.append(filename)
# dictionary of domain table name : domain table path
ddict = {x:os.path.join(dgdb,x) for x in dlist}

# fix numeric domains - description field must be a text field.  This function converts the description field to text.
def tabfix(fixlist,ddict):
	arcpy.AddMessage("{} Converting numeric description fields to text fields".format(time.strftime("%Y%m%d %X")))
	for fix in fixlist:
		tab = ddict[fix]
		arcpy.AddMessage("{} Processing {}".format(time.strftime("%Y%m%d %X"),tab))
		arcpy.AddField_management(tab, 't', 'TEXT')
		arcpy.CalculateField_management(tab,'t','!description!','PYTHON')
		arcpy.DeleteField_management(tab, 'description')
		arcpy.AddField_management(tab, 'description', 'TEXT')
		arcpy.CalculateField_management(tab,'description','!t!','PYTHON')
		arcpy.DeleteField_management(tab, 't')
	arcpy.AddMessage("{} Conversion of numeric description fields to text fields complete".format(time.strftime("%Y%m%d %X")))

# fill any null description fields with the values from the code field
def fillnulldesc(ddict):
	arcpy.AddMessage("{} Replacing null description fields with code values".format(time.strftime("%Y%m%d %X")))
	expression = 'replacenull(!description!, !code!)'
	codeblock = 'def replacenull(rev,oldrev):\n    if not rev:\n        return oldrev\n    else:\n        return rev'
	for d in ddict:
		arcpy.AddMessage("{} Processing {}".format(time.strftime("%Y%m%d %X"),d))
		arcpy.CalculateField_management(ddict[d],'description',expression,'PYTHON',codeblock)
	arcpy.AddMessage("{} Replacing null description fields with code values complete".format(time.strftime("%Y%m%d %X")))

# convert the tables to domains
def tabtodom(ddict):
	arcpy.AddMessage("{} Adding domains to {}".format(time.strftime("%Y%m%d %X"),wksp))
	for d in ddict:
		dtab = ddict[d]
		arcpy.AddMessage("Script start time {}".format(start))
		arcpy.AddMessage("{} Assigning {} domain".format(time.strftime("%Y%m%d %X"),d))
		arcpy.TableToDomain_management(dtab,cf,df,wksp,d,d,"REPLACE")
	arcpy.AddMessage("{} Domains successfully added to {}".format(time.strftime("%Y%m%d %X"),wksp))

if __name__ == '__main__':
	tabfix(fixlist,ddict)
	fillnulldesc(ddict)
	tabtodom(ddict)