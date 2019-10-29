import glob
import numpy as np
import pandas as pd
from scipy import stats
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox, LayoutDOM
from bokeh.models import CustomJS, ColumnDataSource, LinearColorMapper, ColorBar, HoverTool, WheelZoomTool
from bokeh.models.widgets import Slider, TextInput, Paragraph
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors, CARTODBPOSITRON

output_file("heatmap.html")
#################################################################
# Load Pickles Dataframes
df_max_min = pd.read_pickle('../interactive/pickled_files/maxmin.pkl')
df_dates = pd.read_pickle('../interactive/pickled_files/sorted.pkl')
sorted_unique_dates = df_dates.sorted_unique_dates.tolist()

years = np.load('../interactive/npy/years.npy')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

missing = [2003.01, 2003.02, 2003.03, 2003.04, 2003.05, 2003.07]
sorted_unique_dates = sorted(sorted_unique_dates + missing)

Normframe=[]
normframe=[]
for i in range(0,len(glob.glob1('../interactive/pickled_files/jar', '*.pkl'))):
  df_new = pd.read_pickle('../interactive/pickled_files/jar/KDE_' + str(i) + '.pkl')
  normframe.append(df_new['KDE'].tolist()[0])
  Normframe.append([normframe[i]])
#---------------------------------------------------------------#
# ColumnDataSource Setup
s1 = ColumnDataSource(data=dict(image=[normframe[0]], x=df_max_min.xmin, y=df_max_min.ymin))
s2 = ColumnDataSource(data=dict(image=Normframe))
s3 = ColumnDataSource(data=dict(months=months))
s4 = ColumnDataSource(data=dict(years=years))
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
r = p.image(image='image', source=s1, x='x', y='y',
            dw=df_max_min.xmax[0] - df_max_min.xmin[0],
            dh=df_max_min.ymax[0] - df_max_min.ymin[0],
            palette=palette, global_alpha=0.6)
r.glyph.color_mapper.nan_color = (0, 0, 0, 0)
#---------------------------------------------------------------#
# Widgets Setup
year = Slider(title="", value=0, start=0, end=len(glob.glob1('../interactive/pickled_files/jar', '*.pkl'))-1, step=1, callback_policy ='throttle', callback_throttle=500)
year.show_value = False
paragraph = Paragraph(text='January 2000', width=200, height=8)
paragraph.default_size = 500
opacity = Slider(title='Opacity', value=0.6, start=0, end=1.0, step=0.1)
#---------------------------------------------------------------#
# Set Up Callbacks
callback =  CustomJS(args=dict(s1=s1, s2=s2, s3=s3, s4=s4, paragraph=paragraph), code="""
        var inds = cb_obj.value;
        var d1 = s1.data;
        var d2 = s2.data;
        var index = d2['image'];
        d1['image'] = index[inds];

        var months = s3.data['months'];
        var years = s4.data['years'];
        var month = months[inds % 12];
        var year = years[Math.floor(inds / 12)]
        title = `${month} ${year}`
        paragraph.text = title

        s1.change.emit();
    """)
year.js_on_change('value',callback)

callback_opacity = CustomJS(args=dict(r=r), code="""
        r.glyph.global_alpha = cb_obj.value;
    """) 
opacity.js_on_change('value', callback_opacity)
#---------------------------------------------------------------#
# Create the Layout
layout = row(column(paragraph, widgetbox(year), opacity), p, width=800)

show(layout)