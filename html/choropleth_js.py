#reading pickles and plotting results
#import
import numpy as np
import pandas as pd
import geopandas as gpd
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import CustomJS, ColumnDataSource, LinearColorMapper, ColorBar, HoverTool, WheelZoomTool
from bokeh.models.widgets import Slider, Paragraph, CheckboxGroup, Select
from bokeh.plotting import figure, output_file, save, show
from bokeh.palettes import brewer
from bokeh.tile_providers import get_provider, Vendors, CARTODBPOSITRON

output_file("choropleth.html")
#################################################################
# Load Pickles Dataframes
mdf1 = pd.read_pickle('../interactive/pickled_files/mdf1.pkl')
mdf2 = pd.read_pickle('../interactive/pickled_files/mdf2.pkl')
mdf3 = pd.read_pickle('../interactive/pickled_files/mdf3.pkl')
mdf4 = pd.read_pickle('../interactive/pickled_files/mdf4.pkl')

df_sorted = pd.read_pickle('../interactive/pickled_files/sorted.pkl')
sorted_unique_dates = df_sorted.sorted_unique_dates.tolist()

years = np.load('../interactive/npy/years.npy')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
lower_case = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
#---------------------------------------------------------------#
# ColumnDataSource Setup
source = ColumnDataSource(data=dict(xs=list(mdf1['xs']), ys=list(mdf1['ys']), evics=list(mdf1.jan_2000), fips=list(mdf1.fips), tract=list(mdf1.tract), blockgroup=list(mdf1.tract)))
src_mdf1 = ColumnDataSource(data=dict(fips=list(mdf1['fips']), xs=list(mdf1['xs']), ys=list(mdf1['ys']), jan_2012=list(mdf1.jan_2012), feb_2012=list(mdf1.feb_2012), mar_2012=list(mdf1.mar_2012), apr_2012=list(mdf1.apr_2012), may_2012=list(mdf1.may_2012), jun_2012=list(mdf1.jun_2012), jul_2012=list(mdf1.jul_2012), aug_2012=list(mdf1.aug_2012), sep_2012=list(mdf1.sep_2012), oct_2012=list(mdf1.oct_2012), nov_2012=list(mdf1.nov_2012), dec_2012=list(mdf1.dec_2012), jan_2013=list(mdf1.jan_2013), feb_2013=list(mdf1.feb_2013), mar_2013=list(mdf1.mar_2013), apr_2013=list(mdf1.apr_2013), may_2013=list(mdf1.may_2013), jun_2013=list(mdf1.jun_2013), jul_2013=list(mdf1.jul_2013), aug_2013=list(mdf1.aug_2013), sep_2013=list(mdf1.sep_2013), oct_2013=list(mdf1.oct_2013), nov_2013=list(mdf1.nov_2013), dec_2013=list(mdf1.dec_2013), jan_2014=list(mdf1.jan_2014), feb_2014=list(mdf1.feb_2014), mar_2014=list(mdf1.mar_2014), apr_2014=list(mdf1.apr_2014), may_2014=list(mdf1.may_2014), jun_2014=list(mdf1.jun_2014), jul_2014=list(mdf1.jul_2014), aug_2014=list(mdf1.aug_2014), sep_2014=list(mdf1.sep_2014), oct_2014=list(mdf1.oct_2014), nov_2014=list(mdf1.nov_2014), dec_2014=list(mdf1.dec_2014), jan_2015=list(mdf1.jan_2015), feb_2015=list(mdf1.feb_2015), mar_2015=list(mdf1.mar_2015), apr_2015=list(mdf1.apr_2015), may_2015=list(mdf1.may_2015), jun_2015=list(mdf1.jun_2015), jul_2015=list(mdf1.jul_2015), aug_2015=list(mdf1.aug_2015), sep_2015=list(mdf1.sep_2015), oct_2015=list(mdf1.oct_2015), nov_2015=list(mdf1.nov_2015), dec_2015=list(mdf1.dec_2015), jan_2016=list(mdf1.jan_2016), feb_2016=list(mdf1.feb_2016), mar_2016=list(mdf1.mar_2016), apr_2016=list(mdf1.apr_2016), may_2016=list(mdf1.may_2016), jun_2016=list(mdf1.jun_2016), jul_2016=list(mdf1.jul_2016), aug_2016=list(mdf1.aug_2016), sep_2016=list(mdf1.sep_2016), oct_2016=list(mdf1.oct_2016), nov_2016=list(mdf1.nov_2016), dec_2016=list(mdf1.dec_2016), jan_2017=list(mdf1.jan_2017), feb_2017=list(mdf1.feb_2017), mar_2017=list(mdf1.mar_2017), apr_2017=list(mdf1.apr_2017), may_2017=list(mdf1.may_2017), jun_2017=list(mdf1.jun_2017), jul_2017=list(mdf1.jul_2017), aug_2017=list(mdf1.aug_2017), sep_2017=list(mdf1.sep_2017), oct_2017=list(mdf1.oct_2017), nov_2017=list(mdf1.nov_2017), dec_2017=list(mdf1.dec_2017), jan_2018=list(mdf1.jan_2018), feb_2018=list(mdf1.feb_2018), mar_2018=list(mdf1.mar_2018), apr_2018=list(mdf1.apr_2018), may_2018=list(mdf1.may_2018), jun_2018=list(mdf1.jun_2018), jul_2018=list(mdf1.jul_2018), aug_2018=list(mdf1.aug_2018), sep_2018=list(mdf1.sep_2018), oct_2018=list(mdf1.oct_2018), nov_2018=list(mdf1.nov_2018), dec_2018=list(mdf1.dec_2018), jan_2019=list(mdf1.jan_2019), feb_2019=list(mdf1.feb_2019), mar_2019=list(mdf1.mar_2019), apr_2019=list(mdf1.apr_2019), may_2019=list(mdf1.may_2019), jun_2019=list(mdf1.jun_2019), jul_2019=list(mdf1.jul_2019), aug_2019=list(mdf1.aug_2019), sep_2019=list(mdf1.sep_2019), oct_2019=list(mdf1.oct_2019), nov_2019=list(mdf1.nov_2019), dec_2019=list(mdf1.dec_2019), jan_2000=list(mdf1.jan_2000), feb_2000=list(mdf1.feb_2000), mar_2000=list(mdf1.mar_2000), apr_2000=list(mdf1.apr_2000), may_2000=list(mdf1.may_2000), jun_2000=list(mdf1.jun_2000), jul_2000=list(mdf1.jul_2000), aug_2000=list(mdf1.aug_2000), sep_2000=list(mdf1.sep_2000), oct_2000=list(mdf1.oct_2000), nov_2000=list(mdf1.nov_2000), dec_2000=list(mdf1.dec_2000), jan_2001=list(mdf1.jan_2001), feb_2001=list(mdf1.feb_2001), mar_2001=list(mdf1.mar_2001), apr_2001=list(mdf1.apr_2001), may_2001=list(mdf1.may_2001), jun_2001=list(mdf1.jun_2001), jul_2001=list(mdf1.jul_2001), aug_2001=list(mdf1.aug_2001), sep_2001=list(mdf1.sep_2001), oct_2001=list(mdf1.oct_2001), nov_2001=list(mdf1.nov_2001), dec_2001=list(mdf1.dec_2001), jan_2002=list(mdf1.jan_2002), feb_2002=list(mdf1.feb_2002), mar_2002=list(mdf1.mar_2002), apr_2002=list(mdf1.apr_2002), may_2002=list(mdf1.may_2002), jun_2002=list(mdf1.jun_2002), jul_2002=list(mdf1.jul_2002), aug_2002=list(mdf1.aug_2002), sep_2002=list(mdf1.sep_2002), oct_2002=list(mdf1.oct_2002), nov_2002=list(mdf1.nov_2002), dec_2002=list(mdf1.dec_2002), jan_2003=list(mdf1.jan_2003), feb_2003=list(mdf1.feb_2003), mar_2003=list(mdf1.mar_2003), apr_2003=list(mdf1.apr_2003), may_2003=list(mdf1.may_2003), jun_2003=list(mdf1.jun_2003), jul_2003=list(mdf1.jul_2003), aug_2003=list(mdf1.aug_2003), sep_2003=list(mdf1.sep_2003), oct_2003=list(mdf1.oct_2003), nov_2003=list(mdf1.nov_2003), dec_2003=list(mdf1.dec_2003), jan_2004=list(mdf1.jan_2004), feb_2004=list(mdf1.feb_2004), mar_2004=list(mdf1.mar_2004), apr_2004=list(mdf1.apr_2004), may_2004=list(mdf1.may_2004), jun_2004=list(mdf1.jun_2004), jul_2004=list(mdf1.jul_2004), aug_2004=list(mdf1.aug_2004), sep_2004=list(mdf1.sep_2004), oct_2004=list(mdf1.oct_2004), nov_2004=list(mdf1.nov_2004), dec_2004=list(mdf1.dec_2004), jan_2005=list(mdf1.jan_2005), feb_2005=list(mdf1.feb_2005), mar_2005=list(mdf1.mar_2005), apr_2005=list(mdf1.apr_2005), may_2005=list(mdf1.may_2005), jun_2005=list(mdf1.jun_2005), jul_2005=list(mdf1.jul_2005), aug_2005=list(mdf1.aug_2005), sep_2005=list(mdf1.sep_2005), oct_2005=list(mdf1.oct_2005), nov_2005=list(mdf1.nov_2005), dec_2005=list(mdf1.dec_2005), jan_2006=list(mdf1.jan_2006), feb_2006=list(mdf1.feb_2006), mar_2006=list(mdf1.mar_2006), apr_2006=list(mdf1.apr_2006), may_2006=list(mdf1.may_2006), jun_2006=list(mdf1.jun_2006), jul_2006=list(mdf1.jul_2006), aug_2006=list(mdf1.aug_2006), sep_2006=list(mdf1.sep_2006), oct_2006=list(mdf1.oct_2006), nov_2006=list(mdf1.nov_2006), dec_2006=list(mdf1.dec_2006), jan_2007=list(mdf1.jan_2007), feb_2007=list(mdf1.feb_2007), mar_2007=list(mdf1.mar_2007), apr_2007=list(mdf1.apr_2007), may_2007=list(mdf1.may_2007), jun_2007=list(mdf1.jun_2007), jul_2007=list(mdf1.jul_2007), aug_2007=list(mdf1.aug_2007), sep_2007=list(mdf1.sep_2007), oct_2007=list(mdf1.oct_2007), nov_2007=list(mdf1.nov_2007), dec_2007=list(mdf1.dec_2007), jan_2008=list(mdf1.jan_2008), feb_2008=list(mdf1.feb_2008), mar_2008=list(mdf1.mar_2008), apr_2008=list(mdf1.apr_2008), may_2008=list(mdf1.may_2008), jun_2008=list(mdf1.jun_2008), jul_2008=list(mdf1.jul_2008), aug_2008=list(mdf1.aug_2008), sep_2008=list(mdf1.sep_2008), oct_2008=list(mdf1.oct_2008), nov_2008=list(mdf1.nov_2008), dec_2008=list(mdf1.dec_2008), jan_2009=list(mdf1.jan_2009), feb_2009=list(mdf1.feb_2009), mar_2009=list(mdf1.mar_2009), apr_2009=list(mdf1.apr_2009), may_2009=list(mdf1.may_2009), jun_2009=list(mdf1.jun_2009), jul_2009=list(mdf1.jul_2009), aug_2009=list(mdf1.aug_2009), sep_2009=list(mdf1.sep_2009), oct_2009=list(mdf1.oct_2009), nov_2009=list(mdf1.nov_2009), dec_2009=list(mdf1.dec_2009), jan_2010=list(mdf1.jan_2010), feb_2010=list(mdf1.feb_2010), mar_2010=list(mdf1.mar_2010), apr_2010=list(mdf1.apr_2010), may_2010=list(mdf1.may_2010), jun_2010=list(mdf1.jun_2010), jul_2010=list(mdf1.jul_2010), aug_2010=list(mdf1.aug_2010), sep_2010=list(mdf1.sep_2010), oct_2010=list(mdf1.oct_2010), nov_2010=list(mdf1.nov_2010), dec_2010=list(mdf1.dec_2010), jan_2011=list(mdf1.jan_2011), feb_2011=list(mdf1.feb_2011), mar_2011=list(mdf1.mar_2011), apr_2011=list(mdf1.apr_2011), may_2011=list(mdf1.may_2011), jun_2011=list(mdf1.jun_2011), jul_2011=list(mdf1.jul_2011), aug_2011=list(mdf1.aug_2011), sep_2011=list(mdf1.sep_2011), oct_2011=list(mdf1.oct_2011), nov_2011=list(mdf1.nov_2011), dec_2011=list(mdf1.dec_2011), tract=list(mdf1.tract)))
src_mdf2 = ColumnDataSource(data=dict(fips=list(mdf2['fips']), xs=list(mdf2['xs']), ys=list(mdf2['ys']), y_2000=list(mdf2.y_2000), y_2001=list(mdf2.y_2001), y_2002=list(mdf2.y_2002), y_2003=list(mdf2.y_2003), y_2004=list(mdf2.y_2004), y_2005=list(mdf2.y_2005), y_2006=list(mdf2.y_2006), y_2007=list(mdf2.y_2007), y_2008=list(mdf2.y_2008), y_2009=list(mdf2.y_2009), y_2010=list(mdf2.y_2010), y_2011=list(mdf2.y_2011), y_2012=list(mdf2.y_2012), y_2013=list(mdf2.y_2013), y_2014=list(mdf2.y_2014), y_2015=list(mdf2.y_2015), y_2016=list(mdf2.y_2016), y_2017=list(mdf2.y_2017), y_2018=list(mdf2.y_2018), tract=list(mdf2.tract)))
src_mdf3 = ColumnDataSource(data=dict(fips=list(mdf3['fips']), xs=list(mdf3['xs']), ys=list(mdf3['ys']), jan_2012=list(mdf3.jan_2012), feb_2012=list(mdf3.feb_2012), mar_2012=list(mdf3.mar_2012), apr_2012=list(mdf3.apr_2012), may_2012=list(mdf3.may_2012), jun_2012=list(mdf3.jun_2012), jul_2012=list(mdf3.jul_2012), aug_2012=list(mdf3.aug_2012), sep_2012=list(mdf3.sep_2012), oct_2012=list(mdf3.oct_2012), nov_2012=list(mdf3.nov_2012), dec_2012=list(mdf3.dec_2012), jan_2013=list(mdf3.jan_2013), feb_2013=list(mdf3.feb_2013), mar_2013=list(mdf3.mar_2013), apr_2013=list(mdf3.apr_2013), may_2013=list(mdf3.may_2013), jun_2013=list(mdf3.jun_2013), jul_2013=list(mdf3.jul_2013), aug_2013=list(mdf3.aug_2013), sep_2013=list(mdf3.sep_2013), oct_2013=list(mdf3.oct_2013), nov_2013=list(mdf3.nov_2013), dec_2013=list(mdf3.dec_2013), jan_2014=list(mdf3.jan_2014), feb_2014=list(mdf3.feb_2014), mar_2014=list(mdf3.mar_2014), apr_2014=list(mdf3.apr_2014), may_2014=list(mdf3.may_2014), jun_2014=list(mdf3.jun_2014), jul_2014=list(mdf3.jul_2014), aug_2014=list(mdf3.aug_2014), sep_2014=list(mdf3.sep_2014), oct_2014=list(mdf3.oct_2014), nov_2014=list(mdf3.nov_2014), dec_2014=list(mdf3.dec_2014), jan_2015=list(mdf3.jan_2015), feb_2015=list(mdf3.feb_2015), mar_2015=list(mdf3.mar_2015), apr_2015=list(mdf3.apr_2015), may_2015=list(mdf3.may_2015), jun_2015=list(mdf3.jun_2015), jul_2015=list(mdf3.jul_2015), aug_2015=list(mdf3.aug_2015), sep_2015=list(mdf3.sep_2015), oct_2015=list(mdf3.oct_2015), nov_2015=list(mdf3.nov_2015), dec_2015=list(mdf3.dec_2015), jan_2016=list(mdf3.jan_2016), feb_2016=list(mdf3.feb_2016), mar_2016=list(mdf3.mar_2016), apr_2016=list(mdf3.apr_2016), may_2016=list(mdf3.may_2016), jun_2016=list(mdf3.jun_2016), jul_2016=list(mdf3.jul_2016), aug_2016=list(mdf3.aug_2016), sep_2016=list(mdf3.sep_2016), oct_2016=list(mdf3.oct_2016), nov_2016=list(mdf3.nov_2016), dec_2016=list(mdf3.dec_2016), jan_2017=list(mdf3.jan_2017), feb_2017=list(mdf3.feb_2017), mar_2017=list(mdf3.mar_2017), apr_2017=list(mdf3.apr_2017), may_2017=list(mdf3.may_2017), jun_2017=list(mdf3.jun_2017), jul_2017=list(mdf3.jul_2017), aug_2017=list(mdf3.aug_2017), sep_2017=list(mdf3.sep_2017), oct_2017=list(mdf3.oct_2017), nov_2017=list(mdf3.nov_2017), dec_2017=list(mdf3.dec_2017), jan_2018=list(mdf3.jan_2018), feb_2018=list(mdf3.feb_2018), mar_2018=list(mdf3.mar_2018), apr_2018=list(mdf3.apr_2018), may_2018=list(mdf3.may_2018), jun_2018=list(mdf3.jun_2018), jul_2018=list(mdf3.jul_2018), aug_2018=list(mdf3.aug_2018), sep_2018=list(mdf3.sep_2018), oct_2018=list(mdf3.oct_2018), nov_2018=list(mdf3.nov_2018), dec_2018=list(mdf3.dec_2018), jan_2019=list(mdf3.jan_2019), feb_2019=list(mdf3.feb_2019), mar_2019=list(mdf3.mar_2019), apr_2019=list(mdf3.apr_2019), may_2019=list(mdf3.may_2019), jun_2019=list(mdf3.jun_2019), jul_2019=list(mdf3.jul_2019), aug_2019=list(mdf3.aug_2019), sep_2019=list(mdf3.sep_2019), oct_2019=list(mdf3.oct_2019), nov_2019=list(mdf3.nov_2019), dec_2019=list(mdf3.dec_2019), jan_2000=list(mdf3.jan_2000), feb_2000=list(mdf3.feb_2000), mar_2000=list(mdf3.mar_2000), apr_2000=list(mdf3.apr_2000), may_2000=list(mdf3.may_2000), jun_2000=list(mdf3.jun_2000), jul_2000=list(mdf3.jul_2000), aug_2000=list(mdf3.aug_2000), sep_2000=list(mdf3.sep_2000), oct_2000=list(mdf3.oct_2000), nov_2000=list(mdf3.nov_2000), dec_2000=list(mdf3.dec_2000), jan_2001=list(mdf3.jan_2001), feb_2001=list(mdf3.feb_2001), mar_2001=list(mdf3.mar_2001), apr_2001=list(mdf3.apr_2001), may_2001=list(mdf3.may_2001), jun_2001=list(mdf3.jun_2001), jul_2001=list(mdf3.jul_2001), aug_2001=list(mdf3.aug_2001), sep_2001=list(mdf3.sep_2001), oct_2001=list(mdf3.oct_2001), nov_2001=list(mdf3.nov_2001), dec_2001=list(mdf3.dec_2001), jan_2002=list(mdf3.jan_2002), feb_2002=list(mdf3.feb_2002), mar_2002=list(mdf3.mar_2002), apr_2002=list(mdf3.apr_2002), may_2002=list(mdf3.may_2002), jun_2002=list(mdf3.jun_2002), jul_2002=list(mdf3.jul_2002), aug_2002=list(mdf3.aug_2002), sep_2002=list(mdf3.sep_2002), oct_2002=list(mdf3.oct_2002), nov_2002=list(mdf3.nov_2002), dec_2002=list(mdf3.dec_2002), jan_2003=list(mdf3.jan_2003), feb_2003=list(mdf3.feb_2003), mar_2003=list(mdf3.mar_2003), apr_2003=list(mdf3.apr_2003), may_2003=list(mdf3.may_2003), jun_2003=list(mdf3.jun_2003), jul_2003=list(mdf3.jul_2003), aug_2003=list(mdf3.aug_2003), sep_2003=list(mdf3.sep_2003), oct_2003=list(mdf3.oct_2003), nov_2003=list(mdf3.nov_2003), dec_2003=list(mdf3.dec_2003), jan_2004=list(mdf3.jan_2004), feb_2004=list(mdf3.feb_2004), mar_2004=list(mdf3.mar_2004), apr_2004=list(mdf3.apr_2004), may_2004=list(mdf3.may_2004), jun_2004=list(mdf3.jun_2004), jul_2004=list(mdf3.jul_2004), aug_2004=list(mdf3.aug_2004), sep_2004=list(mdf3.sep_2004), oct_2004=list(mdf3.oct_2004), nov_2004=list(mdf3.nov_2004), dec_2004=list(mdf3.dec_2004), jan_2005=list(mdf3.jan_2005), feb_2005=list(mdf3.feb_2005), mar_2005=list(mdf3.mar_2005), apr_2005=list(mdf3.apr_2005), may_2005=list(mdf3.may_2005), jun_2005=list(mdf3.jun_2005), jul_2005=list(mdf3.jul_2005), aug_2005=list(mdf3.aug_2005), sep_2005=list(mdf3.sep_2005), oct_2005=list(mdf3.oct_2005), nov_2005=list(mdf3.nov_2005), dec_2005=list(mdf3.dec_2005), jan_2006=list(mdf3.jan_2006), feb_2006=list(mdf3.feb_2006), mar_2006=list(mdf3.mar_2006), apr_2006=list(mdf3.apr_2006), may_2006=list(mdf3.may_2006), jun_2006=list(mdf3.jun_2006), jul_2006=list(mdf3.jul_2006), aug_2006=list(mdf3.aug_2006), sep_2006=list(mdf3.sep_2006), oct_2006=list(mdf3.oct_2006), nov_2006=list(mdf3.nov_2006), dec_2006=list(mdf3.dec_2006), jan_2007=list(mdf3.jan_2007), feb_2007=list(mdf3.feb_2007), mar_2007=list(mdf3.mar_2007), apr_2007=list(mdf3.apr_2007), may_2007=list(mdf3.may_2007), jun_2007=list(mdf3.jun_2007), jul_2007=list(mdf3.jul_2007), aug_2007=list(mdf3.aug_2007), sep_2007=list(mdf3.sep_2007), oct_2007=list(mdf3.oct_2007), nov_2007=list(mdf3.nov_2007), dec_2007=list(mdf3.dec_2007), jan_2008=list(mdf3.jan_2008), feb_2008=list(mdf3.feb_2008), mar_2008=list(mdf3.mar_2008), apr_2008=list(mdf3.apr_2008), may_2008=list(mdf3.may_2008), jun_2008=list(mdf3.jun_2008), jul_2008=list(mdf3.jul_2008), aug_2008=list(mdf3.aug_2008), sep_2008=list(mdf3.sep_2008), oct_2008=list(mdf3.oct_2008), nov_2008=list(mdf3.nov_2008), dec_2008=list(mdf3.dec_2008), jan_2009=list(mdf3.jan_2009), feb_2009=list(mdf3.feb_2009), mar_2009=list(mdf3.mar_2009), apr_2009=list(mdf3.apr_2009), may_2009=list(mdf3.may_2009), jun_2009=list(mdf3.jun_2009), jul_2009=list(mdf3.jul_2009), aug_2009=list(mdf3.aug_2009), sep_2009=list(mdf3.sep_2009), oct_2009=list(mdf3.oct_2009), nov_2009=list(mdf3.nov_2009), dec_2009=list(mdf3.dec_2009), jan_2010=list(mdf3.jan_2010), feb_2010=list(mdf3.feb_2010), mar_2010=list(mdf3.mar_2010), apr_2010=list(mdf3.apr_2010), may_2010=list(mdf3.may_2010), jun_2010=list(mdf3.jun_2010), jul_2010=list(mdf3.jul_2010), aug_2010=list(mdf3.aug_2010), sep_2010=list(mdf3.sep_2010), oct_2010=list(mdf3.oct_2010), nov_2010=list(mdf3.nov_2010), dec_2010=list(mdf3.dec_2010), jan_2011=list(mdf3.jan_2011), feb_2011=list(mdf3.feb_2011), mar_2011=list(mdf3.mar_2011), apr_2011=list(mdf3.apr_2011), may_2011=list(mdf3.may_2011), jun_2011=list(mdf3.jun_2011), jul_2011=list(mdf3.jul_2011), aug_2011=list(mdf3.aug_2011), sep_2011=list(mdf3.sep_2011), oct_2011=list(mdf3.oct_2011), nov_2011=list(mdf3.nov_2011), dec_2011=list(mdf3.dec_2011), tract=list(mdf3.tract), blockgroup=list(mdf3.blockgroup)))
src_mdf4 = ColumnDataSource(data=dict(fips=list(mdf4['fips']), xs=list(mdf4['xs']), ys=list(mdf4['ys']), y_2000=list(mdf4.y_2000), y_2001=list(mdf4.y_2001), y_2002=list(mdf4.y_2002), y_2003=list(mdf4.y_2003), y_2004=list(mdf4.y_2004), y_2005=list(mdf4.y_2005), y_2006=list(mdf4.y_2006), y_2007=list(mdf4.y_2007), y_2008=list(mdf4.y_2008), y_2009=list(mdf4.y_2009), y_2010=list(mdf4.y_2010), y_2011=list(mdf4.y_2011), y_2012=list(mdf4.y_2012), y_2013=list(mdf4.y_2013), y_2014=list(mdf4.y_2014), y_2015=list(mdf4.y_2015), y_2016=list(mdf4.y_2016), y_2017=list(mdf4.y_2017), y_2018=list(mdf4.y_2018), tract=list(mdf4.tract), blockgroup=list(mdf4.blockgroup)))
src_m = ColumnDataSource(data=dict(months=months))
src_y = ColumnDataSource(data=dict(years=years))
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
hover1 = HoverTool(tooltips=[('Tract', '@tract'), ('# of evictions', '@evics')])
hover2 = HoverTool(tooltips=[('Tract', '@tract'), ('BlockGroup', '@blockgroup'), ('# of evictions', '@evics')])
wheel_zoom = WheelZoomTool()
p = figure(plot_height=650, plot_width=700, title='Tract Evictions, Durham',
           tools=[hover, wheel_zoom, 'pan', 'save', 'reset'], 
           toolbar_location='above', x_range=(-8800000, -8775000), y_range=(4250000, 4350000),
           x_axis_type='mercator', y_axis_type='mercator')
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
r = p.patches('xs', 'ys', source=source, fill_color={'field': 'evics', 'transform': color_mapper},
              line_width=0.3, line_color='black', fill_alpha=0.6)

fill_color1 = {'field': source.data['evics'], 'transform': LinearColorMapper(palette=palette, low=0, high=100)}
fill_color2 = {'field': source.data['evics'], 'transform': LinearColorMapper(palette=palette, low=0, high=650)}
fill_color3 = {'field': source.data['evics'], 'transform': LinearColorMapper(palette=palette, low=0, high=75)}
fill_color4 = {'field': source.data['evics'], 'transform': LinearColorMapper(palette=palette, low=0, high=500)}
#---------------------------------------------------------------#
# Widgets Setup
year = Slider(title='', value=0, start=0, end=len(sorted_unique_dates)-2, step=1, callback_policy ='throttle', callback_throttle=500)
year.show_value = False
year2 = Slider(title='', value=2000, start=2000, end=2018, step=1, callback_policy ='throttle', callback_throttle=500)
year2.visible = False
paragraph = Paragraph(text='January 2000', width=200, height=8)
paragraph.default_size = 500
opacity = Slider(title='Opacity', value=0.6, start=0, end=1.0, step=0.1)
select_census = Select(title='Census Display:', value='Census Tracts', options=['Census Tracts', 'Census BlockGroups'])
select_time = Select(title='Timeframe:', value='Months', options=['Months', 'Years'])
#---------------------------------------------------------------#
# Set Up Callbacks
callback = CustomJS(args=dict(source=source, src_mdf1=src_mdf1, src_mdf3=src_mdf3, src_m=src_m, src_y=src_y, select_census=select_census, select_time=select_time, paragraph=paragraph, color_mapper=color_mapper), code="""
    	var index = cb_obj.value;
    	var months = src_m.data['months'];
        var years = src_y.data['years'];
        var month = months[index % 12];
        var year = years[Math.floor(index / 12)];
        var column = `${month.substring(0, 3).toLowerCase()}_${year}`;

    	if (select_census.value == 'Census Tracts' && select_time.value == 'Months') {

    		color_mapper.high = 100;

	        source.data['xs'] = src_mdf1.data['xs'];
	        source.data['ys'] = src_mdf1.data['ys'];
			source.data['evics'] = src_mdf1.data[column];
			source.data['fips'] = src_mdf1.data['fips'];
			source.data['tract'] = src_mdf1.data['tract'];
			source.data['blockgroup'] = src_mdf1.data['tract'];

	        var title = `${month} ${year}`;
	        paragraph.text = title;
	        source.change.emit();
    	} 
    	if (select_census.value == 'Census BlockGroups' && select_time.value == 'Months') {
    		
			color_mapper.high = 75;

	        source.data['xs'] = src_mdf3.data['xs'];
	        source.data['ys'] = src_mdf3.data['ys'];
			source.data['evics'] = src_mdf3.data[column];
			source.data['fips'] = src_mdf3.data['fips'];
			source.data['tract'] = src_mdf3.data['tract'];
			source.data['blockgroup'] = src_mdf3.data['blockgroup'];

	        var title = `${month} ${year}`;
	        paragraph.text = title;
	        source.change.emit();
    	}     
    """)
year.js_on_change('value', callback)

callback2 = CustomJS(args=dict(source=source, src_mdf2=src_mdf2, src_mdf4=src_mdf4, src_m=src_m, src_y=src_y, select_census=select_census, select_time=select_time, color_mapper=color_mapper), code="""
    	var index = cb_obj.value;
    	var column = `y_${index}`;

    	if (select_census.value == 'Census Tracts' && select_time.value == 'Years') {

    		source.data['xs'] = src_mdf2.data['xs'];
	        source.data['ys'] = src_mdf2.data['ys'];
			source.data['evics'] = src_mdf2.data[column];
			source.data['fips'] = src_mdf2.data['fips'];
			source.data['tract'] = src_mdf2.data['tract'];
			source.data['blockgroup'] = src_mdf2.data['tract'];

			source.change.emit();
    	} 
    	if (select_census.value == 'Census BlockGroups' && select_time.value == 'Years') {

    		source.data['xs'] = src_mdf4.data['xs'];
	        source.data['ys'] = src_mdf4.data['ys'];
			source.data['evics'] = src_mdf4.data[column];
			source.data['fips'] = src_mdf4.data['fips'];
			source.data['tract'] = src_mdf4.data['tract'];
			source.data['blockgroup'] = src_mdf4.data['blockgroup'];

			source.change.emit();
    	} 
    """)
year2.js_on_change('value', callback2)

callback_census = CustomJS(args=dict(select_time=select_time, source=source, p=p, r=r, color_mapper=color_mapper, paragraph=paragraph, year=year, year2=year2, hover=hover, hover1=hover1, hover2=hover2), code="""
    	if (cb_obj.value == 'Census Tracts' && select_time.value == 'Months') {
    		p.title.text = 'Tract Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 100;
   			choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = true;
    		year2.visible = false;
        	year.visible = true;
        	hover.tooltips = hover1.tooltips;
        	year.value += 1
        	year.value -= 1 
    	} 
    	if (cb_obj.value == 'Census Tracts' && select_time.value == 'Years') {
    		p.title.text = 'Tract Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 650;
    		choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = false;
	        year.visible = false;
	        year2.visible = true;
	        hover.tooltips = hover1.tooltips;
	        year2.value += 1
        	year2.value -= 1 
    	}
    	if (cb_obj.value == 'Census BlockGroups' && select_time.value == 'Months') {
    		p.title.text = 'BlockGroup Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 75;
    		choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = true;
	        year2.visible = false;
	        year.visible = true;
	        hover.tooltips = hover2.tooltips;
	        year.value += 1
        	year.value -= 1 
    	} 
    	if (cb_obj.value == 'Census BlockGroups' && select_time.value == 'Years') {
    		p.title.text = 'BlockGroup Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 500;
    		choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = false;
	        year.visible = false;
	        year2.visible = true;
	        hover.tooltips = hover2.tooltips;
	        year2.value += 1
        	year2.value -= 1 
    	}    
    	source.change.emit();  
    """)
select_census.js_on_change('value', callback_census)

callback_time = CustomJS(args=dict(select_census=select_census, source=source, p=p, r=r, color_mapper=color_mapper, paragraph=paragraph, year=year, year2=year2, hover=hover, hover1=hover1, hover2=hover2), code="""
		if (select_census.value == 'Census Tracts' && cb_obj.value == 'Months') {
    		p.title.text = 'Tract Evictions, Durham';
    		color_mapper.high = 100;
    		paragraph.visible = true;
    		year2.visible = false;
        	year.visible = true;
        	hover.tooltips = hover1.tooltips;
        	year.value += 1
        	year.value -= 1 
    	} 
    	if (select_census.value == 'Census Tracts' && cb_obj.value == 'Years') {
    		p.title.text = 'Tract Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 650;
    		choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = false;
	        year.visible = false;
	        year2.visible = true;
	        hover.tooltips = hover1.tooltips;
	        year2.value += 1
        	year2.value -= 1 
    	}
    	if (select_census.value == 'Census BlockGroups' && cb_obj.value == 'Months') {
    		p.title.text = 'BlockGroup Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 75;
    		choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = true;
	        year2.visible = false;
	        year.visible = true;
	        hover.tooltips = hover2.tooltips;
	        year.value += 1
        	year.value -= 1 
    	} 
    	if (select_census.value == 'Census BlockGroups' && cb_obj.value == 'Years') {
    		p.title.text = 'BlockGroup Evictions, Durham';
    		color_mapper.low = 0;
    		color_mapper.high = 500;
    		choropleth_layer.glyph.fill_color = {'field': 'evics', 'transform': color_mapper};
    		paragraph.visible = false;
	        year.visible = false;
	        year2.visible = true;
	        hover.tooltips = hover2.tooltips;
	        year2.value += 1
        	year2.value -= 1 
    	}    
    	source.change.emit();  
    """)
select_time.js_on_change('value', callback_time)

callback_opacity = CustomJS(args=dict(r=r), code="""
        choropleth_layer.glyph.fill_alpha = cb_obj.value;
    """) 
opacity.js_on_change('value', callback_opacity)
#---------------------------------------------------------------#
# Create Layout
layout = row(column(select_census, select_time, paragraph, widgetbox(year), widgetbox(year2), widgetbox(opacity)), p, width=800)

show(layout)

