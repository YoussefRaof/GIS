import arcpy
import os
from PIL import Image, ExifTags
import re

arcpy.env.workspace = r"D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Data"
arcpy.env.overwriteOutput = True

points = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Data\ne_10m_populated_places.shp'
disputed_areas = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Data\ne_10m_admin_0_disputed_areas.shp'
countries = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Data\ne_10m_admin_0_countries.shp'
# airports = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Data\ne_10m_airports.shp'
urban_areas = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Data\ne_10m_urban_areas.shp'

# Requirment-1 list features
# Feature_List = arcpy.ListFeatureClasses()
# print(Feature_List)


#Requirment-2 Cities and disputed areas in Palestine

# output2 = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out2'
# arcpy.env.overwriteOutput = True
# arcpy.MakeFeatureLayer_management(points,'points_layer')
# arcpy.MakeFeatureLayer_management(disputed_areas,'disputed_areas_layer')
# #NAME = Palestine
# arcpy.MakeFeatureLayer_management(countries,'countries_layer',""" "NAME"='Palestine' """)


#for cities
# cities_cursor=arcpy.SearchCursor(points,['NAME','ADM0NAME'])
# for city in cities_cursor:
#     if city.getValue('ADM0NAME') == 'Palestine':
#         city_name = city.getValue('NAME')
#         print(city_name)
#         # Create a feature layer for the current city
#         arcpy.MakeFeatureLayer_management(points, '{}_layer'.format(city_name), """ "NAME" = '{}' """.format(city_name))
#         # Select cities within the palestine
#         arcpy.SelectLayerByLocation_management('{}_layer'.format(city_name), 'WITHIN', 'countries_layer')
#         # create shape file for each
#         arcpy.FeatureClassToFeatureClass_conversion('{}_layer'.format(city_name),output2,'{}_in_Palestine'.format(city_name))

# #for disputed_areas
# disputed_areas_cursor=arcpy.SearchCursor(disputed_areas,['NAME_SORT','ADMIN'])
# for area in disputed_areas_cursor:
#     if area.getValue('ADMIN') == 'Palestine':
#         area_name = area.getValue('NAME')
#         print(area_name)
#         # Create a feature layer for the current area
#         arcpy.MakeFeatureLayer_management(disputed_areas, '{}_layer'.format(area_name), """ "NAME" = '{}' """.format(area_name))
#         # Select areas within palestine
#         arcpy.SelectLayerByLocation_management('{}_layer'.format(area_name), 'WITHIN', 'countries_layer')
#         # create shape file for each
#         arcpy.FeatureClassToFeatureClass_conversion('{}_layer'.format(area_name),output2,'{}_in_Palestine'.format(area_name))




# Requirment-3
#update "Sovereignt"field in the disputed plcaes of palestine to'palestine'

# with arcpy.da.UpdateCursor(disputed_areas,['NAME_SORT','SOVEREIGNT','ADMIN']) as areaCursor:
#
#     for area in areaCursor:
#         if area[2] == 'Palestine':
#             print (area[0],area[1])
#             area[1] = 'Palestine'
#             areaCursor.updateRow(area)
#             print (area[0],area[1])

#update "SOV0NAME "field in the cities of palestine to'palestine'

    # with arcpy.da.UpdateCursor(points,['NAME','SOV0NAME','ADM0NAME']) as pointsCursor:
    #
    # for city in pointsCursor:
    #     if city[2] == 'Palestine':
    #         print (city[0],city[1])
    #         city[1] = 'Palestine'
    #         pointsCursor.updateRow(city)
    #         print (city[0],city[1])


#Requirment-4
# output4 = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out4'
#
# arcpy.MakeFeatureLayer_management(airports,'airports_layer',""" "type" LIKE  '%military%' """)
#
# countries_cursor = arcpy.SearchCursor(countries , ['NAME'])
# for x in countries_cursor:
#     arcpy.MakeFeatureLayer_management(countries ,'countries_layer')
#     arcpy.SelectLayerByLocation_management('airports_layer', 'WITHIN','countries_layer')
#     name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('name'))
#     print(name)
#     arcpy.FeatureClassToFeatureClass_conversion('countries_layer',output4,'country_{0}with_military_airport'.format(name))



# Requirment-5

# output5 = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out5'
# arcpy.env.overwriteOutput = True
# arcpy.MakeFeatureLayer_management(urban_areas,'urban_areas_layer')
#
# countries_cursor=arcpy.SearchCursor(countries,['SOVEREIGNT','CONTINENT'])
#
# for x in countries_cursor:
#     if x.getValue('CONTINENT') in ['Asia','Europe', 'North America']:
#         arcpy.MakeFeatureLayer_management(countries ,'countries_layer')
#         arcpy.SelectLayerByLocation_management('urban_areas_layer','WITHIN','countries_layer')
#         name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('SOVEREIGNT'))
#         print(name)
#         arcpy.FeatureClassToFeatureClass_conversion('urban_areas_layer',output5,'country_{0}_in_{1}_Continent_has_urban_area'.format(name,x.getValue('CONTINENT')))





# Requirment 6

# output6 =r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out6'
# arcpy.env.overwriteOutput = True
#
# disputed_areas_cursor = arcpy.SearchCursor(disputed_areas, ['NAME','INCOME_GRP'])
# for x in disputed_areas_cursor:
#     if x.getValue('INCOME_GRP') in ['1. High income: OECD', '2. High income: nonOECD', '3. Upper middle income']:
#         name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('NAME'))
#         print(name)
#         arcpy.MakeFeatureLayer_management(disputed_areas , 'disputed_areas_layer')
#         arcpy.FeatureClassToFeatureClass_conversion('disputed_areas_layer',output6 ,'disputed_area_{0}_with_{1}_IncomeGRP'.format(name,x.getValue('INCOME_GRP')))




# Requirment 7

# output7=r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out7'
# arcpy.env.overwriteOutput = True
#
# airports_cursor = arcpy.SearchCursor(airports , ['name','location','wikipedia'])
# for x in airports_cursor:
#     name = re.sub(r'[^a-zA-Z0-9\s]', '', x.getValue('name'))
#     wiki = re.sub(r'[^a-zA-Z0-9\s]','',x.getValue('wikipedia'))
#     if x.getValue('location') == 'ramp':
#         print(name)
#         print(wiki)
#         print(x.getValue('location'))
#         print('\n')


# Requirment 8
#sha3ban
# output8 = r'C:\Users\youssef\Desktop\GIS\Output\out8'
# arcpy.env.overwriteOutput = True

# # Extract the list of countries in the Middle East & North Africa region
# arcpy.MakeFeatureLayer_management(countries, 'countries_layer')
# sql_query = """ "region_wb" = 'Middle East & North Africa' AND "CONTINENT" <> 'Europe' AND "NAME" <> 'Israel' """
# arcpy.MakeFeatureLayer_management('countries_layer', 'MENACountries', sql_query)

# country_list = []
# with arcpy.da.SearchCursor('MENACountries', ['NAME']) as cursor:
#     for row in cursor:
#         country_name = row[0]
#         country_list.append(country_name)
# # Print the list of countries
# for country_name in country_list:
#     print(country_name)


# # Create shapefiles for each city in the selected countries
# for Arabcountry in country_list:
#     cities_cursor=arcpy.SearchCursor(points,['NAME','ADM0NAME'])

#     for city in cities_cursor:
#         if city.getValue('ADM0NAME') == Arabcountry:
#             city_name = city.getValue('NAME')
#             print(city_name)
#             city_name=str(city_name).replace('(','').replace(')','').replace(" ' ",'').replace('','_')
#             # Create a feature layer for the current city
#             arcpy.MakeFeatureLayer_management(points, '{}_layer'.format(city_name), """ "NAME" = '{}' """.format(city_name))
#             # Select cities within the MENA
#             arcpy.SelectLayerByLocation_management('{}_layer'.format(city_name), 'WITHIN', 'MENACountries')
#             # create shape file for each
#             arcpy.FeatureClassToFeatureClass_conversion('{}_layer'.format(city_name),output8,'{0}_in_{1}'.format(city_name,Arabcountry))


# Requirment 9
# output9=r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out9'
# arcpy.env.overwriteOutput = True
#
# Sql_Query = """ area_sqkm > 50.0 """
# arcpy.MakeFeatureLayer_management(urban_areas , 'urban_areas_layer', Sql_Query)
#
# country_cursor = arcpy.SearchCursor(countries , ['REGION_UN','FID','SOVEREIGNT'])
#
# for x in country_cursor:
#     if x.getValue('REGION_UN') == 'Africa':
#         name = re.sub(r'[^a-zA-Z0-9\s]','',x.getValue('SOVEREIGNT'))
#         print(x.getValue('FID'))
#         print(name)
#         print(x.getValue('REGION_UN'))
#         print('\n')
#         arcpy.MakeFeatureLayer_management(countries,'countries_layer')
#         arcpy.SelectLayerByLocation_management('urban_areas_layer','WITHIN','countries_layer')
#
#         arcpy.FeatureClassToFeatureClass_conversion('urban_areas_layer',output9,'UrbanAreas_in_{0}_{1}'.format(name,x.getValue('FID')))











# Requirment 10

# output10=r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out10'
# arcpy.env.overwriteOutput = True
#
#
# urban_areas = arcpy.GetParameterAsText(0)
#
# countries = arcpy.GetParameterAsText(1)
# area_sqkm_input = float(arcpy.GetParameterAsText(2))
# region    = arcpy.GetParameterAsText(3)
#
# Sql_Query = """ area_sqkm > {} """.format(area_sqkm_input)
# arcpy.MakeFeatureLayer_management(urban_areas , 'urban_areas_layer', Sql_Query)
#
# country_cursor = arcpy.SearchCursor(countries , ['REGION_UN','FID','SOVEREIGNT'])
#
# for x in country_cursor:
#     if x.getValue('REGION_UN') == region:
#         name = re.sub(r'[^a-zA-Z0-9\s]','',x.getValue('SOVEREIGNT'))
#         print(x.getValue('FID'))
#         print(name)
#         print(x.getValue('REGION_UN'))
#         print('\n')
#         arcpy.MakeFeatureLayer_management(countries,'countries_layer')
#         arcpy.SelectLayerByLocation_management('urban_areas_layer','WITHIN','countries_layer')
#
#         arcpy.FeatureClassToFeatureClass_conversion('urban_areas_layer',output10,'UrbanAreas_in_{0}_{1}'.format(name,x.getValue('FID')))
#         arcpy.AddMessage("Success")




# Requirment 11

# Using Update Cursor for multiple fields, update empty fields that are of string
# datatype in airports with the english name of the airport


# Requirment 11,12
# list all field in air port table

# airports = arcpy.GetParameterAsText(0)
# Column_name = arcpy.GetParameterAsText(1)
# all_fields=arcpy.ListFields(airports)
# #create list of string  fildes within air port table
# text_fileds= []
# for f in all_fields:
#     # print (f.name + " " + f.type )
#     if f.type == 'String':
#         text_fileds.append(f.name)
#         print("\n")
#
# print(len(text_fileds),len(all_fields))
# print("\n")
#
# for field in text_fileds:
#     with arcpy.da.UpdateCursor(airports, [field,Column_name]) as Airport_cursor:
#         for row in Airport_cursor:
#                 if row[0] == ' ':
#                     row[0] = row[-1]
#                     Airport_cursor.updateRow(row)
#                     arcpy.AddMessage("done")




# Requirment 13

# disputed_areas = arcpy.GetParameterAsText(0)
# Year=arcpy.GetParameterAsText(1)
# Updated_Economy=arcpy.GetParameterAsText(2)
#
# # output13=r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Work\Output\Out13'
# arcpy.env.overwriteOutput = True
# totalcount = 0
# Updated_Count = 0
# with arcpy.da.UpdateCursor(disputed_areas,['NAME_SORT','ECONOMY','POP_YEAR']) as disputed_areas_cursor:
#     for x in disputed_areas_cursor:
#         totalcount = totalcount +1
#         if x[2] < float(Year):
#             Updated_Count = Updated_Count+1
#             x[1] = Updated_Economy
#             print(x[0])
#             print(x[1])
#             print(x[2])
#             print("\n")
#             disputed_areas_cursor.updateRow(x)
#             arcpy.AddMessage("Success & Updated")
#
#
# print(Updated_Count, totalcount)

# Requirment 14

# Image1_Folder = r'D:\Colleage\Fourth Year\Second Semester\GIS\Project\Image'
# Image1_Contents=os.listdir(Image1_Folder)
#
# for image in Image1_Contents:
#     print(image)
#     full_path1=os.path.join(Image1_Folder,image)
#     print(full_path1)
#     print("\n")
#     #Requirment 15
#     Pillow_Image=Image.open(full_path1)
#     exif = {ExifTags.TAGS[k]: v for k, v in Pillow_Image._getexif().items() if k in ExifTags.TAGS}
#     print(exif)
#     print("\n")
#     gps_all ={}
#     try:
#         # Requirment 16
#         for k in exif['GPSInfo'].keys():
#             print ("\n")
#             print(" Coded Value {}".format(k))
#             decoded=ExifTags.GPSTAGS.get(k)
#             print "Associated Label {}".format(decoded)
#             gps_all[decoded] = exif['GPSInfo'][k]
#
#         #Requirment 17
#
#         Long_Ref = gps_all.get('GPSLongitudeRef')
#         Long = gps_all.get('GPSLongitude')
#         Lat_Ref = gps_all.get('GPSLatitudeRef')
#         Lat = gps_all.get('GPSLatitude')
#
#         print Long_Ref, "   ",Long
#         print Lat_Ref,  "    ",Lat
#         print("\n")
#     except:
#         print "No Gps Info In This Image".format(full_path1)
#         pass
#








