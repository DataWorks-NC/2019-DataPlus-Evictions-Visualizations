import numpy as np
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2

from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import ColumnDataSource, LinearColorMapper, LogColorMapper, LogTicker, ColorBar, HoverTool, \
    WheelZoomTool
from bokeh.models.widgets import Slider, Paragraph, CheckboxGroup, Select, Button
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors, CARTODBPOSITRON

import queries as q
import settings

#################################################################
# Functions
def makePoly(row):
    import shapely.wkt
    return shapely.wkt.loads(row)


def getPolyCoords(row, coord_type, geom="geom"):
    exterior = row[geom].exterior
    if coord_type == "x":
        return list(exterior.coords.xy[0])
    if coord_type == "y":
        return list(exterior.coords.xy[1])


def conv_poly_ys(row):
    import math
    r = 6378137.0
    return [math.log(math.tan(math.pi / 4 + math.radians(x) / 2)) * r for x in row]


def conv_poly_xs(row):
    import math
    r = 6378137.0
    return [math.radians(x) * r for x in row]


# ---------------------------------------------------------------#
# Set up a connection to the postgres server.
if settings.PGHOST == "" or settings.PGUSER == "":
    print('No connection information found')
    exit(1)

conn_string = 'host=' + settings.PGHOST + ' port=' + '5432' + ' dbname=' + settings.PGDATABASE + ' user=' + settings.PGUSER + ' password=' + settings.PGPASSWORD
conn = psycopg2.connect(conn_string)
print('Connected to Server')
# create a cursor object
cursor = conn.cursor()
# ---------------------------------------------------------------#
# Load Data using SQL Queries
ebm_2018_2019 = q.ebm_2018oct_2019oct
rental_units = """select CAST(geoid10 as NUMERIC) as fips, acs16_rent as rental_units, acs16_tota as total_units FROM staging.evictions_per_bg"""
blockgroup = """select fips, st_astext((ST_Dump(geom)).geom) AS geom, area__sqmi FROM geom.blockgroup"""
# read queries using database
df_blockg_m = sqlio.read_sql_query(ebm_2018_2019, conn)
df_rental = sqlio.read_sql_query(rental_units, conn)
gdf_bg = sqlio.read_sql_query(blockgroup, conn)
# setup time range
years = ['2018', '2019']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
lower_case = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
combine = [j + " " + i for i in years for j in months][9:-2]
update = [lower_case[months.index(j)] + "_" + i for i in years for j in months][9:-2]
num_unique_months = len(combine)
# close connection
conn = None
# ---------------------------------------------------------------#
# Manipulate Data for Plotting
df_rental['rental_units'] = df_rental['rental_units'].replace([0, 0, 0, 0], [33.0, None, None, None])
# Convert FIPS column into INT
df_blockg_m['fips'] = df_blockg_m['fips'].astype(np.int64)
gdf_bg['fips'] = pd.to_numeric(gdf_bg.fips)
# ---------------------------------------------------------------#
# Grab and Convert Coords from Shapefile
gdf_bg['geom'] = gdf_bg.geom.apply(makePoly)  # convert string into Polygon object
gdf_bg['poly_x'] = gdf_bg.apply(getPolyCoords, coord_type='x', axis=1)  # grab x coords
gdf_bg['poly_y'] = gdf_bg.apply(getPolyCoords, coord_type='y', axis=1)  # grab y coords
gdf_bg['xs'] = gdf_bg.poly_x.map(conv_poly_xs)  # convert x coords to be usable by Bokeh
gdf_bg['ys'] = gdf_bg.poly_y.map(conv_poly_ys)  # convert y coords to be usable by Bokeh

# ---------------------------------------------------------------#
# Merge Evictions Dataset with Shapefile
mdf3 = gdf_bg.merge(df_blockg_m, right_on='fips', left_on='fips', how='outer')
mdf3 = df_rental.merge(mdf3, right_on='fips', left_on='fips', how='outer')

# ---------------------------------------------------------------#
# ColumnDataSource Setup
source = ColumnDataSource(
    data=dict(xs=list(mdf3['xs']), ys=list(mdf3['ys']), evics=list((mdf3.oct_2018 * 100) / mdf3.rental_units),
              fips=list(mdf3.fips), tract=list(mdf3.tract), blockgroup=list(mdf3.blockgroup)))

# ---------------------------------------------------------------#
# Palette Setup / ColorBar
color_bar_height = 650 + 11
color_bar_width = 120
palette = brewer['YlGnBu'][8]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette=palette, low=0, high=25)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20,
                     height=500, border_line_color=None, location=(0, 75), orientation='vertical')
color_bar_plot = figure(title="Evictions per 100 Rental Units", title_location="right",
                        height=color_bar_height, width=color_bar_width,
                        toolbar_location=None, min_border=0,
                        outline_line_color=None)

color_bar_plot.add_layout(color_bar, 'right')
color_bar_plot.title.align = "center"
color_bar_plot.title.text_font_size = '12pt'

# ---------------------------------------------------------------#
# Figures
hover = HoverTool(tooltips=[('Tract', '@tract'), ('BlockGroup', '@blockgroup'), ('# of evictions', '@evics')])
wheel_zoom = WheelZoomTool()
p = figure(plot_height=650, plot_width=700, title='BlockGroup Evictions, Durham',
           tools=[hover, wheel_zoom, 'pan', 'save', 'reset'],
           toolbar_location='above', x_range=(-8800000, -8775000), y_range=(4250000, 4350000),
           x_axis_type='mercator', y_axis_type='mercator')

# ---------------------------------------------------------------#
# Map Setup
p.axis.visible = False
p.grid.grid_line_color = None
p.add_tile(CARTODBPOSITRON)
p.grid.grid_line_color = None
p.axis.visible = True
p.toolbar.active_scroll = wheel_zoom

# ---------------------------------------------------------------#
# Glyphs
r = p.patches('xs', 'ys', source=source, fill_color={'field': 'evics', 'transform': color_mapper},
              line_width=0.3, line_color='black', fill_alpha=1)

# ---------------------------------------------------------------#
# Widgets Setup
year = Slider(title='', value=0, start=0, end=num_unique_months - 1, step=1, callback_policy='throttle',
              callback_throttle=500)
year.show_value = False
paragraph = Paragraph(text='October 2018', width=200, height=8)
paragraph.default_size = 500
opacity = Button(label='Full Opacity')


# ---------------------------------------------------------------#
# Set Up Callbacks
def update_data(attrname, old, new):
    # Transition Sliders
    index = year.value
    title = '''{input}'''
    input = title.format(input=combine[index])
    # Generate the new dataset
    update_evics = list((mdf3[update[index]] * 100) / mdf3["rental_units"])
    # Inject new dataset
    source.data = dict(xs=list(mdf3['xs']), ys=list(mdf3['ys']), evics=update_evics, fips=list(mdf3.fips),
                       tract=list(mdf3.tract), blockgroup=list(mdf3.blockgroup))
    paragraph.text = input


year.on_change('value_throttled', update_data)
paragraph.on_change('text', update_data)


def update_opacity():
    if (opacity.label == 'Full Opacity'):
        opacity.label = 'Half Opacity'
        r.glyph.fill_alpha = 0.5
    else:
        opacity.label = 'Full Opacity'
        r.glyph.fill_alpha = 1


opacity.on_click(update_opacity)

# ---------------------------------------------------------------#
# Create Layout
layout = column(row(p, color_bar_plot), paragraph, widgetbox(year), widgetbox(opacity), width=800)

curdoc().add_root(layout)
