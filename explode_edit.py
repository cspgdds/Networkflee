# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:02:04 2018

@author: Joanna Leng from the University of Leeds, email is menjle@leeds.ac.uk
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.io.shapereader as shpreader
import matplotlib.patches as mpatches
import csv, sys


def LineMidPoint(lon1,lat1,lon2,lat2):
    
    lon_mid=0
    lat_mid=0
    
    if lon1 > lon2:
        lon_mid = lon1 - ((lon1 - lon2)/2)
    else:
        lon_mid = lon2 - ((lon2 - lon1)/2)
    
    if lat1 > lat2:
        lat_mid = lat1 - ((lat1 - lat2)/2)
    else:
        lat_mid = lat2 - ((lat2 - lat1)/2)
        
    return(lon_mid,lat_mid)




# Set up for the legeng
red_patch = mpatches.Patch(color='red', label='Conflict Zone')
green_patch = mpatches.Patch(color='green', label='Camp')
yellow_patch = mpatches.Patch(color='yellow', label='Town')
lightgreen_patch = mpatches.Patch(color='lawngreen', label='Forwarding Camp')


# Read in info and calculate some values from it eg lat min and max and 
# lon min and max which are needed to set the extents
local_info = []

filename = 'local_info.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            #print row
            local_info.append(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        
        
        
        
lon_min=0
lon_max=0
lat_min=0
lat_max=0

# draw markers
n=0
for r in local_info[1:]:
     
    lat=float(r[3])
    lon=float(r[4])
    
    if n==0:
        lon_min=lon
        lon_max=lon
        lat_min=lat
        lat_max=lat
        n=1
        
    if lon < lon_min:
        lon_min=lon
    if lon > lon_max:
        lon_max=lon
    if lat < lat_min:
        lat_min=lat
    if lat > lat_max:
        lat_max=lat
        


connect = []

for r in local_info[1:]:
    
    for s in local_info[1:]:
        if r[5] == "conflict_zone" and s[5] == "camp":
            index1=local_info.index(r)
            index2=local_info.index(s)
            item = [index1,index2]
            connect.append(item)
            






# Set up for the image we are creating
kw = dict(resolution='10m', category='cultural', name='admin_1_states_provinces')
states_shp = shpreader.natural_earth(**kw)
shp = shpreader.Reader(states_shp)



# Create a large figure:
fig = plt.figure(figsize=(10, 10))

#The information below was taken from stack over flow:
# https://stackoverflow.com/questions/6999621/how-to-use-extent-in-matplotlib-pyplot-imshow
# Assuming you have longitude along the horizontal ax1is, then you'll take 
# extent=[longitude_top_left,longitude_top_right,latitude_bottom_left,latitude_top_left]. 
# longitude_top_left and longitude_bottom_left should be the same, latitude_top_left 
# and latitude_top_right should be the same, and the values within these pairs 
# are interchangeable.

lon_top_left=12.5
lon_top_right=28
lat_bottom_left=13
lat_top_left=1




# Add axes and draw coastlines:

ax1 = plt.axes([0.01, 0.49, 0.8, 0.5], projection=ccrs.PlateCarree())

ax1.set_extent([lon_top_left, lon_top_right, lat_bottom_left, lat_top_left], crs=ccrs.PlateCarree())

ax1.coastlines()

ax1.legend(handles=[red_patch,green_patch,yellow_patch,lightgreen_patch])




# draw lines to connect nodes
for r in connect:
    
    #print("r:",r)
    
    index_start=r[0]
    index_end=r[1]
    #print("start:",local_info[index_start])
    #print("end:",local_info[index_end])
    start_lat=float(local_info[index_start][3])
    start_lon=float(local_info[index_start][4])
    end_lat=float(local_info[index_end][3])
    end_lon=float(local_info[index_end][4])   
    
    print("start lat:", start_lat)
    print("end lat:", end_lat) 
    print("start lon:", start_lon)
    print("end lon:", end_lon) 
    
    plt.plot([start_lon, end_lon], [start_lat, end_lat],
         color='blue', linewidth=2,
         transform=ccrs.PlateCarree(),
         )

    #print(LineMidPoint(CZ1_lon,CZ1_lat,camp1_lon,camp1_lat))

    [lon_mid,lat_mid]=LineMidPoint(start_lon,start_lat,end_lon,end_lat)



    plt.text(lon_mid, lat_mid, '56km', color="blue",
         horizontalalignment='left', weight="bold",
         transform=ccrs.Geodetic())



# draw markers
for r in local_info[1:]:
    if r[5]=="town":
        print r
        c='yellow'
    elif r[5]=="conflict_zone":
        c='red'
    elif r[5]=="camp":
        c='green'
    elif r[5]=="forwardong_camp":
        c="lawngreen"
    else:
        c='error'
        print(r,":  This is not a valid location type.")
        
    if c is not 'e':
        
        lat=float(r[3])
        lon=float(r[4])
        
        plt.plot([lon, lon], [lat, lat],
                 color=c, marker='o',
                 transform=ccrs.PlateCarree(),
                 )
    
        location=r[0]
    
        plt.text(lon, lat, location,
                 horizontalalignment='right',
                 transform=ccrs.PlateCarree()
                 )

    



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

    else:

        facecolor = 'greenyellow'

    ax1.add_geometries([state], ccrs.PlateCarree(), facecolor=facecolor, edgecolor='black')

ax1.add_feature(ccrs.cartopy.feature.OCEAN)
ax1.add_feature(ccrs.cartopy.feature.RIVERS)
ax1.add_feature(ccrs.cartopy.feature.LAKES)




'''
# I was deceloping this section to explode out and zoom some parts of the map.
# This did not work easily and I susspect I should have used subfigures rather
# than adding axes to the figure. This was based on a code snippet taken from here:
# https://stackoverflow.com/questions/22543847/drawing-lines-between-cartopy-axes

print("lat min:",lat_min)
print("lat max:",lat_max)




# Draw the rectangular extent of the second plot on the first:
plt.plot([lon_max+0.5, lon_max+0.5], [lat_min-0.5, lat_max+0.5],
    color='black', linewidth=1,
    transform=ccrs.PlateCarree(),
    )
plt.plot([lon_min-0.5, lon_min-0.5], [lat_min-0.5, lat_max+0.5],
    color='black', linewidth=1,
    transform=ccrs.PlateCarree(),
    )
plt.plot([lon_min-0.5, lon_max+0.5], [lat_min-0.5, lat_min-0.5],
    color='black', linewidth=1,
    transform=ccrs.PlateCarree(),
    )
plt.plot([lon_min-0.5, lon_max+0.5], [lat_max+0.5, lat_max+0.5],
    color='black', linewidth=1,
    transform=ccrs.PlateCarree(),
    )

plt.plot([lon_min-0.5, 0.45], [lat_min-0.5, 0.35],
    color='black', linewidth=1,
    transform=ccrs.PlateCarree(),
    )



# Add a second axes set (overlaps first) and draw coastlines:
ax2 = plt.axes([0.45, 0.35, 0.4, 0.3], projection=ccrs.PlateCarree())
#ax2.set_extent([13, 20, 10, 6], crs=ccrs.PlateCarree())
ax2.set_extent([lon_min-0.5, lon_max+0.5, lat_max+0.5, lat_min-0.5], crs=ccrs.PlateCarree())
ax2.coastlines()


ax2.add_feature(ccrs.cartopy.feature.OCEAN)
ax2.add_feature(ccrs.cartopy.feature.RIVERS)
ax2.add_feature(ccrs.cartopy.feature.LAKES)
ax2.add_feature(ccrs.cartopy.feature.BORDERS)


lon_top_left=12.5
lon_top_right=28
lat_bottom_left=13
lat_top_left=1




transFigure = fig.transFigure.inverted()
coord1 = transFigure.transform(ax2.transAxes.transform([0, 0]))
print(coord1)
coord2 = transFigure.transform(ax1.transData.transform([lon_min-0.5, lat_min-0.5]))
print(coord2)
#line = plt.Line2D((coord1[0], coord2[0]), (coord1[1], coord2[1]), transform=fig.transFigure)
#fig.lines.append(line)

plt.plot([lon_min-0.5, coord1[0]], [lat_min-0.5, 0.35],
    color='black', linewidth=1,
    transform=ccrs.PlateCarree(),
    )
'''

plt.show()


