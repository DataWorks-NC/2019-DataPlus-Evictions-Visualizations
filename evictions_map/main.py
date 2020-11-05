from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, FixedTicker, LogColorMapper, ColorBar, HoverTool, \
    WheelZoomTool
from bokeh.models.widgets import Slider, Paragraph, Button
from bokeh.plotting import figure
from bokeh.palettes import YlGnBu5
from bokeh.tile_providers import get_provider, CARTODBPOSITRON_RETINA

# Reverse the color palette so it runs from lighter to darker.
palette = YlGnBu5[::-1]


# Filters the evictions dataframe by year and month.
def filter_evictions(evictions_dataset, year, month):
    return evictions_dataset[(evictions_dataset['year'] == year) & (evictions_dataset['month'] == month)]

# setup time range
months_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November',
          'December']
num_unique_months = 24

# Import data from server_context
server_context = curdoc().session_context.server_context
evictions_count = server_context.evictions_count

# Find unique dates from dataset
dates = evictions_count.groupby(['year', 'month'])
dates = dates['year'].unique().keys()
update = dates[(-1*num_unique_months-1):-1] # (year, month) pairs for most recent 18 months in dataset, but cut most recent month because server tends to report empty data there.
update = [{'year': d[0], 'month': d[1], 'name': f'{months_names[d[1] - 1]} {d[0]}'} for d in update]
cur_date = update[-1]

# Pull latest data for initial display
initial_filtered_evictions = filter_evictions(evictions_count, cur_date['year'], cur_date['month'])

source = ColumnDataSource(
        data=dict(
            xs=list(initial_filtered_evictions['xs']),
            ys=list(initial_filtered_evictions['ys']),
            evics=list(initial_filtered_evictions['evictions_per_rental_unit']),
            evics_raw=list(initial_filtered_evictions['evictions']),
            fips=list(initial_filtered_evictions.fips),
            tract=list(initial_filtered_evictions.tract),
            blockgroup=list(initial_filtered_evictions.blockgroup))
)

# ---------------------------------------------------------------#
# Palette Setup / ColorBar
color_bar_height = 650 + 11
color_bar_width = 120
color_mapper = LogColorMapper(palette=palette, low=0.00001, high=evictions_count['evictions_per_rental_unit'].max())
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, ticker=FixedTicker(ticks=[0, 2, 5, 10, 50]),
                     major_tick_line_color='#000000', major_tick_out=5,
                     height=500, location=(0, 0))
color_bar_plot = figure(title="Evictions per 100 Rental Units", title_location="right",
                        height=color_bar_height, width=color_bar_width,
                        toolbar_location=None, min_border=0,
                        outline_line_color=None)

color_bar_plot.add_layout(color_bar, 'right')
color_bar_plot.title.align = "center"
color_bar_plot.title.text_font_size = '12pt'

# ---------------------------------------------------------------#
# Figures
hover = HoverTool(tooltips=[('Tract', '@tract'), ('Block Group', '@blockgroup'), ('Evictions per 100 rental units', '@evics'), ('Total evictions', '@evics_raw')])
wheel_zoom = WheelZoomTool()

evictions_data = ColumnDataSource(dict(
    xs=list(initial_filtered_evictions['xs']),
    ys=list(initial_filtered_evictions['ys']),
    evics=list(initial_filtered_evictions['evictions_per_rental_unit']),
    evics_raw=list(initial_filtered_evictions['evictions']),
    fips=list(initial_filtered_evictions.fips),
    tract=list(initial_filtered_evictions.tract),
    blockgroup=list(initial_filtered_evictions.blockgroup))
)

evictions_map = figure(plot_height=650, plot_width=500, title='Evictions per 100 Rental Units per Block group, Durham',
                       tools=[hover, wheel_zoom, 'pan', 'save', 'reset'],
                       toolbar_location='above', x_range=(-8785000, -8775000), y_range=(4280000, 4335000),
                       x_axis_type='mercator', y_axis_type='mercator')

# ---------------------------------------------------------------#
# Map Setup
evictions_map.axis.visible = False
evictions_map.grid.grid_line_color = None
evictions_map.add_tile(get_provider(CARTODBPOSITRON_RETINA))
evictions_map.grid.grid_line_color = None
evictions_map.toolbar.active_scroll = wheel_zoom

# ---------------------------------------------------------------#
# Glyphs
choropleth_layer = evictions_map.patches('xs', 'ys',
                                         source=evictions_data,
                                         fill_color={'field': 'evics', 'transform': color_mapper},
                                         line_width=0.3,
                                         line_color='black',
                                         fill_alpha=0.9)

# ---------------------------------------------------------------#
# Widgets Setup

year = Slider(title='', value=num_unique_months - 1, start=0, end=num_unique_months - 1, step=1)

year.show_value = False
sliderLabel = Paragraph(text='Select a month to view using the slider')
paragraph = Paragraph(text=cur_date['name'], width=200, height=8) # TODO: This initial value also needs to update dynamically
paragraph.default_size = 500
opacity = Button(label='Show Streets')


# ---------------------------------------------------------------#
# Set Up Callbacks
def update_data(attrname, old, new):
    # Transition Sliders
    index = year.value

    # Pull just evictions data for this month/year.

    filtered_evictions = filter_evictions(evictions_count, update[index]['year'], update[index]['month'])

    # Inject new dataset
    evictions_data.data = dict(
        xs=list(filtered_evictions['xs']),
        ys=list(filtered_evictions['ys']),
        evics=list(filtered_evictions['evictions_per_rental_unit']),
        evics_raw=list(filtered_evictions['evictions']),
        fips=list(filtered_evictions.fips),
        tract=list(filtered_evictions.tract),
        blockgroup=list(filtered_evictions.blockgroup)
    )
    paragraph.text = update[index]['name']


year.on_change('value_throttled', update_data)
paragraph.on_change('text', update_data)


def update_opacity():
    if opacity.label == 'Show Streets':
        opacity.label = 'Hide Streets'
        choropleth_layer.glyph.fill_alpha = 0.5
    else:
        opacity.label = 'Show Streets'
        choropleth_layer.glyph.fill_alpha = 1


opacity.on_click(update_opacity)

# ---------------------------------------------------------------#
# Create Layout
layout = column(row(evictions_map, color_bar_plot), sliderLabel, paragraph, year, opacity, width=800)

curdoc().add_root(layout)
