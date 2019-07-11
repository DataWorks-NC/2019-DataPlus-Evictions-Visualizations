#reading pickles and plotting results
#import
import numpy as np
import pandas as pd
from scipy import stats
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox, LayoutDOM
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar, HoverTool, WheelZoomTool
from bokeh.models.widgets import Slider, TextInput, Paragraph, CheckboxGroup
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors, CARTODBPOSITRON
from functions import get_base_dir
#################################################################
# Load Pickles Dataframesdf = pd.read_pickle(f'{get_base_dir()}/pickled_files/df.pkl')
# df_max_min = pd.read_pickle(f'{get_base_dir()}/pickled_files/maxmin.pkl')
# df_dates = pd.read_pickle(f'{get_base_dir()}/pickled_files/sorted.pkl')
# sorted_unique_dates = df_dates.sorted_unique_dates.tolist()
# initial = pd.read_pickle(f'{get_base_dir()}/pickled_files/initial.pkl')

# normframe=[]
# for i in range(0,len(sorted_unique_dates)):
#   df = pd.read_pickle(f'{get_base_dir()}/pickled_files/jar/KDE_' + str(i) + '.pkl')
#   normframe.append(df['KDE'].tolist()[0])
df=pd.read_pickle(f'{get_base_dir()}/pickled_files/df.pkl')
df_max_min=pd.read_pickle(f'{get_base_dir()}/pickled_files/maxmin.pkl')

dates=df['date'].tolist()
unique_dates=list(set(dates))
sorted_unique_dates=sorted(unique_dates)

normframe=[]
for i in range(0,len(sorted_unique_dates)):
    t = pd.read_pickle(f'{get_base_dir()}/pickled_files/jar/KDE_' + str(i) + '.pkl')
    normframe.append(t['KDE'].tolist()[0])
#---------------------------------------------------------------#
# ColumnDataSource Setup
source = ColumnDataSource(data=dict(image=[normframe[0]], x=df_max_min.xmin, y=df_max_min.ymin))
pointsource = ColumnDataSource(data=dict(xs=list(initial['XX']), ys=list(initial['YY'])))
#---------------------------------------------------------------#
# Palette Setup
palette = brewer['OrRd'][8]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette=palette, low=0, high=1)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20,
                     height=500, border_line_color=None, location=(0,75), orientation='vertical')
#---------------------------------------------------------------#
# Figures
wheel_zoom = WheelZoomTool()
p = figure(plot_height=650, plot_width=700, title="Durham Evictions",
           tools=[wheel_zoom, 'pan', 'save', 'reset'], tooltips=[("value", "@image")], toolbar_location='above',
           x_range=(-8800000, -8775000), y_range=(4250000, 4350000),
           x_axis_type="mercator", y_axis_type="mercator")
#---------------------------------------------------------------#
# Map Setup
p.axis.visible = False
p.grid.grid_line_color = None
p.add_tile(CARTODBPOSITRON)
p.grid.grid_line_color = None
p.axis.visible = True
p.add_layout(color_bar, 'right')
p.toolbar.active_scroll = wheel_zoom
#---------------------------------------------------------------#
# Glyphs
r = p.image(image='image', source=source, x='x', y='y',
        	dw=df_max_min.xmax[0] - df_max_min.xmin[0],
        	dh=df_max_min.ymax[0] - df_max_min.ymin[0],
        	palette=palette, global_alpha=0.6)
r.glyph.color_mapper.nan_color = (0, 0, 0, 0)
s = p.circle(x='xs', y='ys', source=pointsource, size=1, fill_color='black', line_color='black', fill_alpha=0)
s.visible = False
#---------------------------------------------------------------#
# Widgets Setup
year = Slider(title="", value=0, start=0, end=len(sorted_unique_dates)-1, step=1, callback_policy ='throttle', callback_throttle=500)
year.show_value = False
paragraph = Paragraph(text='January 2012', width=200, height=8)
paragraph.default_size = 500
opacity = Slider(title='Opacity', value=0.6, start=0, end=1.0, step=0.1)
checkbox = CheckboxGroup(labels=["Eviction Points"], active=[])
#---------------------------------------------------------------#
# Set Up Callbacks
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
combine = []

for i in range(len(years)):
    for j in range(len(months)):
        combine.append(months[j] + ' ' + years[i])

def update_data(attrname, old, new):
    yr = year.value
    source.data = dict(image=[normframe[yr]], x=df_max_min.xmin, y=df_max_min.ymin)

    new_data=df[df['date']==sorted_unique_dates[yr]]
    pointsource.data=dict(xs=list(new_data['XX']),ys=list(new_data['YY']))

    title = """{input}"""
    input = title.format(input=combine[yr])
    paragraph.text = input
year.on_change('value_throttled', update_data)     
paragraph.on_change('text', update_data)

def update_opacity(attrname, old, new):
    
    r.glyph.global_alpha=opacity.value
opacity.on_change('value', update_opacity)

def update_checkbox(attrname, old, new):
    if checkbox.active.__contains__(0):
        s.visible = True
    if not(checkbox.active.__contains__(0)):
        s.visible = False
checkbox.on_change('active', update_checkbox)
#---------------------------------------------------------------#
# Create the Layout
layout = row(column(paragraph, widgetbox(year), opacity, checkbox), p, width=800)


