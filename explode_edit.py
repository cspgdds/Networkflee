# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:02:04 2018

@author: menjle
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import matplotlib.patches as mpatches


red_patch = mpatches.Patch(color='red', label='Conflict Zone')
green_patch = mpatches.Patch(color='green', label='Camp')
yellow_patch = mpatches.Patch(color='yellow', label='Town')
lightgreen_patch = mpatches.Patch(color='lawngreen', label='Forwarding Camp')

#plt.legend(handles=[red_patch,green_patch])


shpfilename = shpreader.natural_earth(resolution='110m',
                                      category='cultural',
                                      name='admin_0_countries')
states_shp = shpreader.natural_earth(**kw)
shp = shpreader.Reader(states_shp)



# Create a large figure:
fig = plt.figure(figsize=(15, 15))

# Assuming you have longitude along the horizontal axis, then you'll take 
# extent=[longitude_top_left,longitude_top_right,latitude_bottom_left,latitude_top_left]. 
# longitude_top_left and longitude_bottom_left should be the same, latitude_top_left 
# and latitude_top_right should be the same, and the values within these pairs 
# are interchangeable.

lon_min=1
lon_max=28
lat_min=1
lat_max=28

# Add a second axes set (overlaps first) and draw coastlines:
ax2 = plt.axes([0.4, 0.35, 0.4, 0.3], projection=ccrs.PlateCarree())
ax2.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
ax2.coastlines()

ax2.legend(handles=[red_patch,green_patch,yellow_patch,lightgreen_patch])

#Bangui,Bangui,CAR,4.36122,18.55496,conflict_zone
#Dosseye,La_Nya_Pende_Province,Chad,8.1591666,16.4888888,camp

CZ1_lat = 4.36122
CZ1_lon = 18.55496

camp1_lat = 8.1591666
camp1_lon = 16.4888888

# draw a line
plt.plot([CZ1_lon, camp1_lon], [CZ1_lat, camp1_lat],
         color='blue', linewidth=2, marker='o',
         transform=ccrs.PlateCarree(),
         )

# draw a marker
plt.plot([CZ1_lon, CZ1_lon], [CZ1_lat, CZ1_lat],
         color='red', marker='o',
         transform=ccrs.PlateCarree(),
         )

plt.plot([camp1_lon, camp1_lon], [camp1_lat, camp1_lat],
         color='green', marker='o',
         transform=ccrs.PlateCarree(),
         )

plt.text(camp1_lon -1, camp1_lat, 'Dosseye',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(CZ1_lon, CZ1_lat, 'Bangui',
         horizontalalignment='left',
         transform=ccrs.Geodetic())



#colors = list(cnames.keys())

#len_colors = len(colors)

 

k = 0


for record, state in zip(shp.records(), shp.geometries()):

    if record.attributes['admin'] == 'Central African Republic':

        #if k+1 == len_colors:

            #k = 0

        #else:

            #k += 1

        facecolor = 'LightGray'

    #else:

        #facecolor = 'LightGray'

    ax2.add_geometries([state], ccrs.PlateCarree(), facecolor=facecolor, edgecolor='black')


plt.show()