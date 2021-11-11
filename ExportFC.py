# Scritp used to export a feature, from one feature class to another, in arcgis
# Created using ModelBuilder

# -*- coding: utf-8 -*-

import arcpy

def ExportFeature():  

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    imputFC = ""
    outputFC = ""
 

    # Process: Select (Select) (analysis)
    export_test = "C:\\WINDOWS\\TEMP\\ArcGISProTemp8864\\fd2867fa-18c4-4487-9481-bdff22304df6\\Default.gdb\\export_test"
    arcpy.analysis.Select(in_features=imputFC, out_feature_class=export_test, where_clause='')

    # Process: Append (Append) (management)
    cod_edif_CN = arcpy.management.Append(inputs=[export_test], target=outputFC, schema_type="TEST", field_mapping="", subtype="", expression="")[0]

    # Process: Delete (Delete) (management)
    if export_test:
        Delete_Succeeded = arcpy.management.Delete(in_data=[export_test], data_type="")[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\WINDOWS\TEMP\ArcGISProTemp8864\fd2867fa-18c4-4487-9481-bdff22304df6\Default.gdb", workspace=r"C:\WINDOWS\TEMP\ArcGISProTemp8864\fd2867fa-18c4-4487-9481-bdff22304df6\Default.gdb"):
        ExportFeature()
