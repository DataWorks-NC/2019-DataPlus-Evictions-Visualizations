#reading pickles and plotting results
#import
import numpy as np
import pandas as pd
from bokeh.io import show
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.plotting import figure
from bokeh.palettes import brewer
#################################################################
# Load Pickles Dataframes
df = pd.read_pickle('./pickled_files/df_calendar.pkl')
years = np.load('./npy/years.npy')
months = np.load('./npy/months.npy')
#---------------------------------------------------------------#
# Palette Setup
palette = ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff']
palette = palette[::-1]
mapper = LinearColorMapper(palette=palette, low=df.normalize.min(), high=df.normalize.max())
color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="10pt",
                     ticker=BasicTicker(desired_num_ticks=len(palette)),
                     label_standoff=6, border_line_color=None, location=(0, 0))
#---------------------------------------------------------------#
# Figures
p = figure(title="Number of Evictions in Durham ({0} - {1})".format(years[0], years[-1]),
           x_range=years, y_range=list(reversed(months)),
           x_axis_location="above", plot_width=750, plot_height=500,
           tools=["hover,save,pan,box_zoom,reset,wheel_zoom"], toolbar_location='below',
           tooltips=[('date', '@Month @Year'), ('norm', '@normalize'), ('evictions', '@evictions')])
#---------------------------------------------------------------#
# Map Setup
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "20pt"
p.title.text_font_size = '20pt'
p.axis.major_label_standoff = 0
p.add_layout(color_bar, 'right')
#---------------------------------------------------------------#
# Glyphs
p.rect(x="Year", y="Month", width=1, height=1,
       source=df,
       fill_color={'field': 'normalize', 'transform': mapper},
       line_color=None)
#---------------------------------------------------------------#
# Create Layout
layout = p
