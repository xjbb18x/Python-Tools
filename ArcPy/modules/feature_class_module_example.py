#--------------------------------------------------------------------------- 
# Name:        feature_class_module_example.py
#
# Purpose:     Defines 'boundary' feature class creation
#              which is a component of the RCWP Data Dictionary
#
#              
# Version:     See 'ver' line 32 in code
# Author:      Jason Balkenbush
# Created:     05/10/2017
#
#
# Pre:
#		output geodatabase must already exist or be created before running boundary()
#
# Params:   
#		outgdb - output geodatabase
#		sr - spatial reference
#
# Run instructions: 
#					import feature_class_module_example
#					example_fc(outgdb,sr)
#
#
#
# 
#--------------------------------------------------------------------------- 

import arcpy

def example_fc(outgdb,sr):
	ver = '1.0'
	name = 'example_fc'
	aname = name + '_v' + ver
	type = 'POLYGON'	
	# field structure (name, type, precision, scale, length, domain)
	fexample = [('supplier_id', 'TEXT', '', '', 15, '')
	,('steward', 'TEXT', '', '', 100, '')
	,('data_supplier', 'TEXT', '', '', 50, '')
	,('survey_company', 'TEXT', '', '', 100, '')
	,('surveyor', 'TEXT', '', '', 50, '')
	,('survey_date', 'DATE', '', '', '', '')
	,('survey_revision', 'TEXT', '', '', 5, '')
	,('physical_lifecycle_status', 'TEXT', '', '', 30, '')
	,('revision', 'TEXT', '', '', 5, '')
	,('revision_date', 'DATE', '', '', '', '')
	,('feature_status', 'TEXT', '', '', 15, '')
	,('feature_retired_date', 'DATE', '', '', '', '')
	,('source_data', 'TEXT', '', '', 250, '')
	,('capture_method', 'TEXT', '', '', 15, '')
	,('spatial_accuracy_m', 'DOUBLE', 6, 2, '', '')
	,('boundary_type', 'TEXT', '', '', 50, '')
	,('note', 'TEXT', '', '', 250, '')
	,('feature_name', 'TEXT', '', '', 100, '')
	,('lot_plan', 'TEXT', '', '', 25, '')
	,('tenure', 'TEXT', '', '', 100, '')
	,('landholder', 'TEXT', '', '', 250, '')
	,('acquired_date', 'DATE', '', '', '', '')
	,('expiry_date', 'DATE', '', '', '', '')
	,('tenement_status', 'TEXT', '', '', 25, '')
	,('release_id', 'TEXT', '', '', 50, '')
	,('checked_date', 'DATE', '', '', '', '')]
	# create the feature class
	example = arcpy.CreateFeatureclass_management(outgdb, name, type,'',"ENABLED", "ENABLED", sr)
	# set alias name with current version
	arcpy.AlterAliasName(example, aname)
	# add fields
	for field in fexample:
		arcpy.AddField_management(example,field[0],field[1],field[2],field[3],field[4],'','','',field[5])
	return example