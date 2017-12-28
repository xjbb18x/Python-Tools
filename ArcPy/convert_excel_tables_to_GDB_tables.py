## Convert domain tables from excel to gdb tables
## Jason Balkenbush, 26/10/2017
## Must be run as a stand-alone script.  Does not work through Python module in ArcGIS (I can't figure out why)
## Params:	xf = input excel table
##			ogdb = output gdb
##          ofold = output folder
##
## Pre:		
##			Sheet names must be valid ArcGIS table name (no special characters or spaces)
##			Each sheet in excel document represents a domain table

import xlrd
import os
import arcpy
import time

# input excel document
xf = r"C:\temp\test\domain_specs.xls"
# output folder
ofold = r"C:\temp\test"
# output geodatabase
ogdb = r"C:\temp\test\domains.gdb"
arcpy.env.workspace = ogdb
arcpy.env.overwriteOutput = True

# make output gdb function
def makeogdb(ofold):
	ogdb = arcpy.CreateFileGDB_management(ofold, 'domains', 'current')

# excel sheets to geodatabase tables function	
def exdomstogdb(in_ex, out_gdb):
	wb = xlrd.open_workbook(in_ex)
	sheets = [sheet.name for sheet in wb.sheets()]
	arcpy.AddMessage('{} sheets found: {}'.format(len(sheets),','.join(sheets)))
	#print '{} sheets found: {}'.format(len(sheets),','.join(sheets))
	for sheet in sheets:
		out_table = os.path.join(out_gdb,arcpy.ValidateTableName(sheet))
		arcpy.AddMessage('{} Converting {} to {}'.format(time.strftime("%Y%m%d %X"),sheet, out_table))
		#print 'Converting {} to {}'.format(sheet, out_table)
		arcpy.ExcelToTable_conversion(in_ex,out_table,sheet)

if __name__=='__main__':
	if not os.path.isdir(ogdb):
		makeogdb(ofold)
	exdomstogdb(xf,ogdb)
