## Jason Balkenbush 28 December 2017
## For xls files: code to group rows based on duplicate values in the first column
## groups are converted to new sheets in the output xls file
## rows containing "Domain" in the first cell are excluded from the output
## xlwt does not work with xlsx files, only xls
##

import xlrd
import xlwt

# input excel file
fname = r"C:\temp\test\domain_specs.xls"
# ouput excel file
foname = r"C:\temp\test\domain_specs_modified.xls"
wb = xlrd.open_workbook(fname)
sheets = [sheet.name for sheet in wb.sheets()]


for sheet in sheets:
	sh = wb.sheet_by_name(sheet)
	nrows = sh.nrows
	ncols = sh.ncols
	print "{} has {} rows, {} cols".format(sheet,nrows,ncols)

sh1 = wb.sheet_by_name(sheets[1])


vallist = []
#rowlist = []
for i in range(sh1.nrows):
	vallist.append(sh1.cell_value(i,0))
#	rowlist.append(sh1.row(i))

vset = set(vallist)

vdict = {}
for val in vset:
	vdict[val] = [i for i, x in enumerate(vallist) if x == val]
vdict.pop('Domain')
vset.remove('Domain')

# sdict contains key:[[cell1,cell2],[cell1,cell2],...] the key values are cell 2 and cell 3 from each row where the key occurs
sdict = {}
for k in vdict:
	for i in vdict[k]:
		sdict[k]=[[sh1.cell_value(i,1),sh1.cell_value(i,2)] if i in vdict[k] else i for i in vdict[k]]

# create sheet list
slist = []
for s in sdict:
	slist.append(s)

# Create the new sheets
wtwb = xlwt.Workbook(foname)
for s in slist:
	wtwb.add_sheet(s,'cell_overwrite_ok=True')

# Write new cells
for s in slist:
	wtsh = wtwb.get_sheet(slist.index(s))
	for i in range(len(sdict[s])):
		v1 = sdict[s][i][0]
		v2 = sdict[s][i][1]
		wtsh.write(0,0,u"code")
		wtsh.write(0,1,u"description")
		wtsh.write(i+1,0,v1)
		wtsh.write(i+1,1,v2)

wtwb.save(foname)

