# script used to extract features attachments , like photos from a survey

import arcpy
from arcpy import da
import os

inTable = arcpy.GetParameterAsText(0)
fileLocation = arcpy.GetParameterAsText(1)

with da.SearchCursor(inTable, ['DATA', 'ATT_NAME', 'ATTACHMENTID']) as cursor:
    for item in cursor:
        attachment = item[0]
        filename = str(item[1]) 
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filename
        del attachment