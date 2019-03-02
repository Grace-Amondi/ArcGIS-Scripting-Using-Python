# import sitepackages
import arcpy, os
try:
    workspace = arcpy.GetParameterAsText(0)
    txtfile= arcpy.GetParameterAsText(1)
    fc =arcpy.GetParameterAsText(2)
#     define workspace
    arcpy.env.workspace = workspace
#     open text file
    f = open(txtfile,'r')
#     read line by line
    lstSchls = f.readlines()
#     open cursor for read write access
    cursor = arcpy.InsertCursor(fc)
    
#     loop through school txt file and insert latitude and longitude to school feature class
    for school in lstSchls:
        if 'latitude' in school:
            continue
#         split by tabs
        vals = school.split("	")    
        latitude= float(vals[2])
        longitude= float(vals[1])
        confid = int(vals[0])
        
#         create points in arcpy
        pnt = arcpy.Point(longitude,latitude)
        feat= cursor.newRow()
        feat.shape =pnt
        feat.setValue("CONFIDENCEVALUE",confid)
        cursor.insertRow(feat)
        
except:
#     return error
    print arcpy.GetMessages()
finally:
#     release lock
    del cursor
    f.close()
