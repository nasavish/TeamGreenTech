# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:12:46 2018

@author: jbode
"""

# =============================================================================
# 1. Import Dependencies
# =============================================================================
import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper,
    LinearColorMapper,
    ContinuousColorMapper
)
from bokeh.palettes import Blues8, PuBu8, OrRd8
from bokeh.plotting import figure
import shapefile    

# =============================================================================
# 2. Format Geo data
# =============================================================================
# Iterate through each station
# Iterate through each row and create polygon
 

geodata = shapefile.Reader("../Resources/zip_code_shapes/cb_2017_us_zcta510_500k.shp")
geos = geodata.shapes()
recs = geodata.records()

lats = []
longs = []

for shape in geos:
    xpoly = []
    ypoly = []
    for point in shape.points:
        lat = point[0]
        long = point[1]
        xpoly.append(lat)
        ypoly.append(long)
    
    lats.append(xpoly)
    longs.append(ypoly)    
    
zipcodes = []    
for rec in recs:
    zipcodes.append(rec[0])    

my_dict = {
        "zipcode": zipcodes
        }
import numpy as np
geodata = pd.DataFrame(my_dict, dtype = np.int64)
geodata['lats'] = lats
geodata['longs'] = longs

geodata.to_json("../Resources/Zip code shape files - Bokeh gmap style.json")

# =============================================================================
#  3. Read in zip level data and merge geometries
# =============================================================================

zipdata = pd.read_pickle("../Resources/Solar data summary by zip")
zipdata.reset_index(level = None, inplace = True)
zipdata.rename(columns = {"Zip Code": "zipcode"}, inplace = True)
zipdata = pd.merge(zipdata, geodata, on = 'zipcode', how = 'inner')
zipdata = zipdata[['zipcode', 'solar_per_000', 'population', 'Total_installedkW', 'lats', 'longs']]
zipdata['solar_rank'] = zipdata.solar_per_000.rank(pct = True)

# =============================================================================
# 4. Produce chart - Penetration per 1000 people
# =============================================================================

#A. Set color scale 
PuBu8.reverse()
color_mapper = LinearColorMapper(palette=PuBu8)

#B. Define source
source = ColumnDataSource(zipdata)

#C. Specify Figure
TOOLS = "pan,wheel_zoom,reset,hover,box_zoom,save"
p = figure(
    title="New York Solar Penetration by zip code", tools=TOOLS,
    x_axis_location=None, y_axis_location=None, 
    plot_width = 1200, plot_height = 800
)


#D. Add Polygons
p.patches('lats', 'longs', source=source,
          fill_color={'field': 'solar_rank', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)


#E. Specify Hover Options
hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Zip Code:", "@zipcode"),
    ("Solar (kW) per 1,000 people", "@solar_per_000{0,0.0}"),
    ("Total Solar Installed (kW)", "@Total_installedkW{0,0}"),
    ("Population", "@population{0,0}"), 
    ("(Long, Lat)", "($x, $y)"),
]


#F. Remove grid lines
p.grid.grid_line_color = None


#G. Add Scale

#H.Show and save figure
show(p)
output_file("../Resources/Zip Code Choropleth Map Bokeh.html")
  