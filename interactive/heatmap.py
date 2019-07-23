#reading pickles and plotting results
#import
import glob
import functions as fn
import numpy as np
import pandas as pd
from scipy import stats
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox, LayoutDOM
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar, HoverTool, WheelZoomTool
from bokeh.models.widgets import Slider, TextInput, Paragraph
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors, CARTODBPOSITRON
#################################################################
# Load Pickles Dataframes
df_max_min = pd.read_pickle(f'{fn.get_base_dir()}/pickled_files/maxmin.pkl')
df_dates = pd.read_pickle(f'{fn.get_base_dir()}/pickled_files/sorted.pkl')
sorted_unique_dates = df_dates.sorted_unique_dates.tolist()

years = np.load(f'{fn.get_base_dir()}/npy/years.npy')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

missing = [2003.01, 2003.02, 2003.03, 2003.04, 2003.05, 2003.07]
sorted_unique_dates = sorted(sorted_unique_dates + missing)

normframe=[]
for i in range(0,len(glob.glob1(f'{fn.get_base_dir()}/pickled_files/jar', '*.pkl'))):
  df_new = pd.read_pickle(f'{fn.get_base_dir()}/pickled_files/jar/KDE_' + str(i) + '.pkl')
  normframe.append(df_new['KDE'].tolist()[0])
#---------------------------------------------------------------#
# ColumnDataSource Setup
source = ColumnDataSource(data=dict(image=[normframe[0]], x=df_max_min.xmin, y=df_max_min.ymin))
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
#---------------------------------------------------------------#
# Widgets Setup
year = Slider(title="", value=0, start=0, end=len(glob.glob1(f'{fn.get_base_dir()}/pickled_files/jar', '*.pkl'))-1, step=1, callback_policy ='throttle', callback_throttle=500)
year.show_value = False
paragraph = Paragraph(text='January 2000', width=200, height=8)
paragraph.default_size = 500
opacity = Slider(title='Opacity', value=0.6, start=0, end=1.0, step=0.1)
#---------------------------------------------------------------#
# Set Up Callbacks
def update_data(attrname, old, new):
    yr = year.value
    source.data = dict(image=[normframe[yr]], x=df_max_min.xmin, y=df_max_min.ymin)

    title = """{input}"""
    input = title.format(input=months[yr % 12] + " " + years[yr // 12])
    paragraph.text = input
year.on_change('value_throttled', update_data)     
paragraph.on_change('text', update_data)

def update_opacity(attrname, old, new):
    
    r.glyph.global_alpha=opacity.value
opacity.on_change('value', update_opacity)
#---------------------------------------------------------------#
# Create the Layout
layout = row(column(paragraph, widgetbox(year), opacity), p, width=800)
