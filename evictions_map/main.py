from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import ColumnDataSource, LinearColorMapper, LogColorMapper, LogTicker, ColorBar, HoverTool, \
    WheelZoomTool
from bokeh.models.widgets import Slider, DateSlider, Paragraph, CheckboxGroup, Select, Button
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors

# setup time range
# TODO: PUll this from the range returned by DB query so it auto-updates.
years = ['2018', '2019']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November',
          'December']
lower_case = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
combine = [j + " " + i for i in years for j in months][9:-2]
update = [{'year': int(i), 'month': j + 1} for i in years for j in range(len(months))][9:-2]
num_unique_months = len(combine)

# Import data from server_context
server_context = curdoc().session_context.server_context
mdf3 = server_context.mdf3

initial_filtered_evictions = mdf3[(mdf3['year'] == update[-1]['year']) & (mdf3['month'] == update[-1]['month'])]

source = ColumnDataSource(
        data=dict(xs=list(initial_filtered_evictions['xs']), ys=list(initial_filtered_evictions['ys']), evics=list((initial_filtered_evictions['evictions'] * 100) / initial_filtered_evictions['rental_units']),
                  fips=list(initial_filtered_evictions.fips), tract=list(initial_filtered_evictions.tract), blockgroup=list(initial_filtered_evictions.blockgroup)))

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
hover = HoverTool(tooltips=[('Tract', '@tract'), ('Block Group', '@blockgroup'), ('Evictions per 100 renters', '@evics')])
wheel_zoom = WheelZoomTool()
p = figure(plot_height=650, plot_width=700, title='Evictions per 100 Rental Units per Block group, Durham',
           tools=[hover, wheel_zoom, 'pan', 'save', 'reset'],
           toolbar_location='above', x_range=(-8800000, -8775000), y_range=(4250000, 4350000),
           x_axis_type='mercator', y_axis_type='mercator')

# ---------------------------------------------------------------#
# Map Setup
p.axis.visible = False
p.grid.grid_line_color = None
p.add_tile(get_provider(Vendors.CARTODBPOSITRON))
p.grid.grid_line_color = None
p.axis.visible = True
p.toolbar.active_scroll = wheel_zoom

# ---------------------------------------------------------------#
# Glyphs
r = p.patches('xs', 'ys', source=source, fill_color={'field': 'evics', 'transform': color_mapper},
              line_width=0.3, line_color='black', fill_alpha=1)

# ---------------------------------------------------------------#
# Widgets Setup

year = Slider(title='', value=num_unique_months - 1, start=0, end=num_unique_months - 1, step=1, callback_policy='throttle',
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

    # Pull just evictions data for this month/year.
    filtered_evictions = mdf3[(mdf3['year'] == update[index]['year']) & (mdf3['month'] == update[index]['month'])]
    # Generate the new dataset
    update_evics = list((filtered_evictions['evictions'] * 100) / filtered_evictions["rental_units"])
    # Inject new dataset
    source.data = dict(xs=list(filtered_evictions['xs']), ys=list(filtered_evictions['ys']), evics=update_evics, fips=list(filtered_evictions.fips),
                       tract=list(filtered_evictions.tract), blockgroup=list(filtered_evictions.blockgroup))
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