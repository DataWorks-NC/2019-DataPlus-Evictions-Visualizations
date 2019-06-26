#reading pickles and plotting results
#import
import _functions as fn
import pandas as pd
import geopandas as gpd
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.models.widgets import Slider, Paragraph, CheckboxGroup, Select
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors, CARTODBPOSITRON
#################################################################
# Load Pickles Dataframes
mdf1 = pd.read_pickle('./pickled_files/mdf1.pkl')
mdf2 = pd.read_pickle('./pickled_files/mdf2.pkl')
mdf3 = pd.read_pickle('./pickled_files/mdf3.pkl')
mdf4 = pd.read_pickle('./pickled_files/mdf4.pkl')
initial = pd.read_pickle('./pickled_files/initial2.pkl')
df_date = pd.read_pickle('./pickled_files/df_date.pkl')
df_sorted = pd.read_pickle('./pickled_files/sorted2.pkl')
sorted_unique_dates = df_sorted.sorted_unique_dates.tolist()
#---------------------------------------------------------------#
# ColumnDataSource Setup
source = ColumnDataSource(data=dict(xs=list(mdf1['xs']), ys=list(mdf1['ys']), evics=list(mdf1.jan_2012), fips=list(mdf1.fips), tract=list(mdf1.tract), blockgroup=list(mdf1.tract)))
pointsource = ColumnDataSource(data=dict(xs=list(initial['XX']), ys=list(initial['YY'])))
#---------------------------------------------------------------#
# Palette Setup
palette = brewer['YlGnBu'][8]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette=palette, low=0, high=100)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20,
                     height=500, border_line_color=None, location=(0,75), orientation='vertical')
#---------------------------------------------------------------#
# Figures
hover = HoverTool(tooltips=[('Tract', '@tract'), ('# of evictions', '@evics')])
p = figure(plot_height=650, plot_width=700, title="Tract Evictions, Durham",
           tools=[hover,'wheel_zoom', 'pan', 'save', 'reset'], 
           toolbar_location='above', x_range=(-8800000, -8775000), y_range=(4250000, 4350000),
           x_axis_type="mercator", y_axis_type="mercator")
#---------------------------------------------------------------#
# Map Setup
p.axis.visible = False
p.grid.grid_line_color = None
p.add_tile(CARTODBPOSITRON)
p.grid.grid_line_color = None
p.axis.visible = True
p.add_layout(color_bar, 'right')
#---------------------------------------------------------------#
# Glyphs
r = p.patches('xs', 'ys', source=source, fill_color={'field': 'evics', 'transform': color_mapper},
              line_width=0.3, line_color='black', fill_alpha=0.6)
s = p.circle(x='xs', y='ys', source=pointsource, size=1, fill_color='black', line_color='black', fill_alpha=0)
s.visible = False
#---------------------------------------------------------------#
# Widgets Setup
year = Slider(title="", value=0, start=0, end=len(sorted_unique_dates)-1, step=1)
year.show_value = False
year2 = Slider(title="", value=2012, start=2012, end=2018, step=1)
year2.visible = False
paragraph = Paragraph(text='January 2012', width=200, height=8)
paragraph.default_size = 500
opacity = Slider(title='Opacity', value=0.6, start=0, end=1.0, step=0.1)
checkbox = CheckboxGroup(labels=["Eviction Points"], active=[])
select_census = Select(title="Census Display:", value="Census Tracts", options=["Census Tracts", "Census BlockGroups"])
select_time = Select(title="Timeframe:", value="Months", options=["Months", "Years"])
#---------------------------------------------------------------#
# Set Up Callbacks
lower_case = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
combine = []
year_slider = []

for i in range(len(years)):
    for j in range(len(months)):
        combine.append(months[j] + ' ' + years[i])
        year_slider.append(lower_case[j] + '_' + years[i])

def update_data(attrname, old, new):
    # Get the current slider values
    if select_census.value == 'Census Tracts' and select_time.value == 'Months':
        p.title.text = 'Tract Evictions, Durham'
        color_mapper = LinearColorMapper(palette=palette, low=0, high=100)
        r.glyph.fill_color = {'field': 'evics', 'transform': color_mapper}
        color_bar.color_mapper = color_mapper
        paragraph.visible = True
        year2.visible = False
        year.visible = True
        index = year.value
        title = """{input}"""
        input = title.format(input=combine[index])
        # Generate the new dataset
        new_data = df_date[df_date['date'] == sorted_unique_dates[index]]
        update_evics = list(mdf1[year_slider[index]])
        # Inject new dataset
        pointsource.data = dict(xs=list(new_data['XX']), ys=list(new_data['YY']))
        source.data = dict(xs=list(mdf1['xs']), ys=list(mdf1['ys']), evics=update_evics, fips=mdf1.fips, tract=list(mdf1.tract), blockgroup=list(mdf1.tract))
        paragraph.text = input
        hover.tooltips = [('Tract', '@tract'), ('# of evictions', '@evics')]

    if select_census.value == 'Census Tracts' and select_time.value == 'Years':
        #Set Map Properties
        p.title.text = 'Tract Evictions, Durham'
        color_mapper = LinearColorMapper(palette=palette, low=0, high=650)
        r.glyph.fill_color = {'field': 'evics', 'transform': color_mapper}
        color_bar.color_mapper = color_mapper
        #Transition Sliders
        paragraph.visible = False
        year.visible = False
        year2.visible = True
        index = year2.value
        input = 'y_' + str(index)
        # Generate the new dataset
        new_data = df_date.query('data_year == @index')
        update_evics = list(mdf2[input])
        # Inject new dataset
        pointsource.data = dict(xs=list(new_data['XX']), ys=list(new_data['YY']))
        source.data = dict(xs=list(mdf2['xs']), ys=list(mdf2['ys']), evics=update_evics, fips=mdf2.fips, tract=list(mdf2.tract), blockgroup=list(mdf2.tract))
        hover.tooltips = [('Tract', '@tract'), ('# of evictions', '@evics')]

    if select_census.value == 'Census BlockGroups' and select_time.value == 'Months':
        #Set Map Properties
        p.title.text = 'BlockGroup Evictions, Durham'
        color_mapper = LinearColorMapper(palette=palette, low=0, high=100)
        color_bar.color_mapper = color_mapper
        r.glyph.fill_color = {'field': 'evics', 'transform': color_mapper}
        #Transition Sliders
        paragraph.visible = True
        year2.visible = False
        year.visible = True
        index = year.value
        title = """{input}"""
        input = title.format(input=combine[index])
        # Generate the new dataset
        new_data = df_date[df_date['date'] == sorted_unique_dates[index]]
        update_evics = list(mdf3[year_slider[index]])
        # Inject new dataset
        pointsource.data = dict(xs=list(new_data['XX']), ys=list(new_data['YY']))
        source.data = dict(xs=list(mdf3['xs']), ys=list(mdf3['ys']), evics=update_evics, fips=list(mdf3.fips), tract=list(mdf3.tract), blockgroup=list(mdf3.blockgroup))
        paragraph.text = input
        hover.tooltips = [('Tract', '@tract'), ('BlockGroup', '@blockgroup'), ('# of evictions', '@evics')]

    if select_census.value == 'Census BlockGroups' and select_time.value == 'Years':
        p.title.text = 'BlockGroup Evictions, Durham'
        color_mapper = LinearColorMapper(palette=palette, low=0, high=500)
        color_bar.color_mapper = color_mapper
        r.glyph.fill_color = {'field': 'evics', 'transform': color_mapper}
        #Transition Sliders
        paragraph.visible = False
        year.visible = False
        year2.visible = True
        index = year2.value
        input = 'y_' + str(index)
        # Generate the new dataset
        new_data = df_date.query('data_year == @index')
        update_evics = list(mdf4[input])
        # Inject new dataset
        pointsource.data = dict(xs=list(new_data['XX']), ys=list(new_data['YY']))
        source.data = dict(xs=list(mdf4['xs']), ys=list(mdf4['ys']), evics=update_evics, fips=list(mdf4.fips), tract=list(mdf4.tract), blockgroup=list(mdf4.blockgroup))
        hover.tooltips = [('Tract', '@tract'), ('BlockGroup', '@blockgroup'), ('# of evictions', '@evics')]


year.on_change('value', update_data)
year2.on_change('value', update_data)
paragraph.on_change('text', update_data)

def update_opacity(attrname, old, new):

  r.glyph.fill_alpha = opacity.value
opacity.on_change('value', update_opacity)

def update_checkbox(attrname, old, new):
    if checkbox.active.__contains__(0):
        s.visible = True
    if not(checkbox.active.__contains__(0)):
        s.visible = False
checkbox.on_change('active', update_checkbox)

# def update_select_census(attrname, old, new):

select_census.on_change('value', update_data)

# def update_select_time(attrname, old, new):

select_time.on_change('value', update_data)
#---------------------------------------------------------------#
# Create Layout
layout = row(column(select_census, select_time, paragraph, widgetbox(year), widgetbox(year2), widgetbox(opacity), checkbox), p, width=800)

