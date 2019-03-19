# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:42:55 2019

@author: YK Huang
"""

import arcpy
import numpy
F_toaream2 = "{0}".format("!SHAPE.area@SQUAREMETERS!")
 
#replace zonexx
#100
featurelist = [r"FS_buffer\FS_buffer_100m",r"chicago_zones\chicago_zone12"]
outzone = r' C:\Users\yhuan25\Documents\ArcGIS\Default.gdb\fs_zone12_100_wpython'
arcpy.Intersect_analysis (in_features=featurelist, out_feature_class= outzone)
arcpy.AddField_management(outzone,"t2","Double")
arcpy.CalculateField_management(outzone, "t2",F_toaream2, "PYTHON", )
outdf = arcpy.da.FeatureClassToNumPyArray(outzone, ['OBJECTID','Name','t2'])  
numpy.savetxt('fs_zone12_100_wpython.csv', outdf, delimiter=",", header="oid,Name,t2", fmt="%s")  
#200
featurelist = [r"FS_buffer\FS_buffer_200m",r"chicago_zones\chicago_zone12"]
outzone = r' C:\Users\yhuan25\Documents\ArcGIS\Default.gdb\fs_zone12_200_wpython'
arcpy.Intersect_analysis (in_features=featurelist, out_feature_class= outzone)
arcpy.AddField_management(outzone,"t2","Double")
arcpy.CalculateField_management(outzone, "t2",F_toaream2, "PYTHON", )
outdf = arcpy.da.FeatureClassToNumPyArray(outzone, ['OBJECTID','Name','t2'])  
numpy.savetxt('fs_zone12_200_wpython.csv', outdf, delimiter=",", header="oid,Name,t2", fmt="%s")  
#300
featurelist = [r"FS_buffer\FS_buffer_300m",r"chicago_zones\chicago_zone12"]
outzone = r' C:\Users\yhuan25\Documents\ArcGIS\Default.gdb\fs_zone12_300_wpython'
arcpy.Intersect_analysis (in_features=featurelist, out_feature_class= outzone)
arcpy.AddField_management(outzone,"t2","Double")
arcpy.CalculateField_management(outzone, "t2",F_toaream2, "PYTHON", )
outdf = arcpy.da.FeatureClassToNumPyArray(outzone, ['OBJECTID','Name','t2'])  
numpy.savetxt('fs_zone12_300_wpython.csv', outdf, delimiter=",", header="oid,Name,t2", fmt="%s")  
#500
featurelist = [r"FS_buffer\FS_buffer_500m",r"chicago_zones\chicago_zone12"]
outzone = r' C:\Users\yhuan25\Documents\ArcGIS\Default.gdb\fs_zone12_500_wpython'
arcpy.Intersect_analysis (in_features=featurelist, out_feature_class= outzone)
arcpy.AddField_management(outzone,"t2","Double")
arcpy.CalculateField_management(outzone, "t2",F_toaream2, "PYTHON", )
outdf = arcpy.da.FeatureClassToNumPyArray(outzone, ['OBJECTID','Name','t2'])  
numpy.savetxt('fs_zone12_500_wpython.csv', outdf, delimiter=",", header="oid,Name,t2", fmt="%s")  
#1000
featurelist = [r"FS_buffer\FS_buffer_1000m",r"chicago_zones\chicago_zone12"]
outzone = r' C:\Users\yhuan25\Documents\ArcGIS\Default.gdb\fs_zone12_1000_wpython'
arcpy.Intersect_analysis (in_features=featurelist, out_feature_class= outzone)
arcpy.AddField_management(outzone,"t2","Double")
arcpy.CalculateField_management(outzone, "t2",F_toaream2, "PYTHON", )
outdf = arcpy.da.FeatureClassToNumPyArray(outzone, ['OBJECTID','Name','t2'])  
numpy.savetxt('fs_zone12_1000_wpython.csv', outdf, delimiter=",", header="oid,Name,t2", fmt="%s")  
#3000
featurelist = [r"FS_buffer\FS_buffer_3000m",r"chicago_zones\chicago_zone12"]
outzone = r' C:\Users\yhuan25\Documents\ArcGIS\Default.gdb\fs_zone12_3000_wpython'
arcpy.Intersect_analysis (in_features=featurelist, out_feature_class= outzone)
arcpy.AddField_management(outzone,"t2","Double")
arcpy.CalculateField_management(outzone, "t2",F_toaream2, "PYTHON", )
outdf = arcpy.da.FeatureClassToNumPyArray(outzone, ['OBJECTID','Name','t2'])  
numpy.savetxt('fs_zone12_3000_wpython.csv', outdf, delimiter=",", header="oid,Name,t2", fmt="%s")  

