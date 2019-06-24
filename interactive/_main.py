import chloropleth
import heatmap
import grid
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs, Panel

tab1 = Panel(child=chloropleth.layout, title='Chloropleth')
tab2 = Panel(child=heatmap.layout, title='HeatMap')
tab3 = Panel(child=grid.layout, title='Calendar')
tabs = Tabs(tabs=[tab1, tab2, tab3])

curdoc().add_root(tabs)