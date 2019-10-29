#reading pickles and plotting results
#import
import numpy as np
import pandas as pd
from math import pi
from bokeh.io import show
from bokeh.models import CustomJS, LinearColorMapper, BasicTicker, ColorBar
from bokeh.models.widgets import Select
from bokeh.plotting import figure, output_file
from bokeh.palettes import brewer
from bokeh.layouts import column

output_file("grid.html")
#################################################################
# Load Pickles Dataframes
df = pd.read_pickle('../interactive/pickled_files/df_calendar.pkl')
years = np.load('../interactive/npy/years.npy')
months = np.load('../interactive/npy/months.npy')
#---------------------------------------------------------------#
# Palette Setup
palette = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b']
mapper = LinearColorMapper(palette=palette, low=df.normalize.min(), high=df.normalize.max())
color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="10pt",
                     ticker=BasicTicker(desired_num_ticks=len(palette)),
                     label_standoff=6, border_line_color=None, location=(0, 0))
#---------------------------------------------------------------#
# Widgets
select = Select(title='Display Type:', value='Normalized Ejectments', options=['Normalized Ejectments', 'Standard Ejectments'])
#---------------------------------------------------------------#
# Figures
p = figure(title="Number of Evictions in Durham ({0} - {1})".format(years[0], years[-1]),
           x_range=years, y_range=list(reversed(months)),
           x_axis_location="above", plot_width=1250, plot_height=500,
           tools=["hover,save,pan,box_zoom,reset,wheel_zoom"], toolbar_location='below',
           tooltips=[('date', '@Month @Year'), ('norm', '@normalize'), ('evictions', '@evictions')])
#---------------------------------------------------------------#
# Map Setup
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "18pt"
p.xaxis.major_label_orientation = pi/6
p.title.text_font_size = '20pt'
p.axis.major_label_standoff = 0
p.add_layout(color_bar, 'right')

n_min = df.normalize.min()
n_max = df.normalize.max()
e_min = df.evictions.min()
e_max = df.evictions.max()
#---------------------------------------------------------------#
# Glyphs
r = p.rect(x="Year", y="Month", width=1, height=1,
       source=df,
       fill_color={'field': 'normalize', 'transform': mapper},
       line_color=None)
#---------------------------------------------------------------#
# Set Up Callbacks
callback = CustomJS(args=dict(n_min=n_min, n_max=n_max, e_min=e_min, e_max=e_max, mapper=mapper, r=r), code="""
    if (cb_obj.value == 'Normalized Ejectments') {
        mapper.low = n_min;
        mapper.high = n_max;
        r.glyph.fill_color = {'field': 'normalize', 'transform': mapper}
    }
    if (cb_obj.value == 'Standard Ejectments') {
        mapper.low = e_min;
        mapper.high = e_max;
        r.glyph.fill_color = {'field': 'evictions', 'transform': mapper}
    }
    """)
select.js_on_change('value', callback)
#---------------------------------------------------------------#
# Create Layout
layout = column(p, select)

show(layout)




