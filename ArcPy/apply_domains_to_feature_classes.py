# Code to apply domains to feature classes
# Jason Balkenbush 28 December 2017
# GDB, Feature Classes, Domains must all exist

# excel format: Table|Field|Domain
# uses first excel sheet in the input excel document

# build list of indexes for each table
# use the indexes to read the cell values for field and domain
# once the values are obtained, use them to apply the domains

import arcpy
import xlrd
import time
import os

# input excel file
fname = r"C:\temp\test\domain_specs.xls"
# gdb containing the feature classes that will have the domains applied
ogdb = r"C:\temp\test\test.gdb"

start = time.strftime("%Y%m%d %X")

# set up log to record processed feature classes
lname = "RCWPDD_Processed_FCs.txt"
logfilename = os.path.join(r'\\pipelinetrust\apps\GIS\Projects\Wallumbilla_Reedy_Creek\Data_Dictionary\Processing',lname)
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
    
# message log 
def log(message):
    """log message"""
    now = time.strftime("%Y%m%d %X")
    try:
        print message
        logfile.write(str(message) + '\n')
        logfile.flush()
    except IOError:
        print "Error: Log file IOError"


# open workbook, assign sheet 1
wb = xlrd.open_workbook(fname)
sh1 = wb.sheet_by_index(0)

# list of table names (all instances)
vlist = []
for i in range(sh1.nrows):
	vlist.append(sh1.cell_value(i,0))

# set of unique table names
vset = set(vlist)

# dictionary of table names and their row indices
tdict = {}
for v in vset:
	tdict[v] = [i for i, x in enumerate(vlist) if x == v]
tdict.pop('Table')
vset.remove('Table')

# dictionary of {tablename1 : [[field1,domain1],[field2,domain2],...], tablename2 : [[field1,domain1],...],...}
vdict = {}
for t in tdict:
	for i in tdict[t]:
		vdict[t]=[[sh1.cell_value(i,1),sh1.cell_value(i,2)] if i in tdict[t] else i for i in tdict[t]]

# assign the domains
def assdoms(vdict):
	for v in vdict:
		for i in vdict[v]:
			tab = os.path.join(ogdb,v)
			field = i[0]
			domain = i[1]
			#print "{} Assigning {} domain to {} in {} feature class".format(time.strftime("%Y%m%d %X"),domain,field,tab)
			arcpy.AddMessage("Script start time {}".format(start))
			arcpy.AddMessage("{} Assigning {} domain to {} in {} feature class".format(time.strftime("%Y%m%d %X"),domain,field,tab))
			arcpy.AssignDomainToField_management (tab, field, domain)
			log(','.join([tab,field]))

if __name__ == '__main__':
	arcpy.AddMessage("{} Start".format(time.strftime("%Y%m%d %X")))
	assdoms(vdict)
	arcpy.AddMessage("{} End".format(time.strftime("%Y%m%d %X")))