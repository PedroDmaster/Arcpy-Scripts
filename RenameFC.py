import arcpy
arcpy.env.workspace = 'LOCATION OF THE GDB'
fcs = arcpy.ListFeatureClasses("*cnty*","")

for fc in fcs:
    arcpy.Rename_management(fc, f'{fc[0:1]}{fc[-2]}')