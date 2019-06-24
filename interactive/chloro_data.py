#setting up data for Chloropleth
#import
import _functions as fn
import pandas as pd
import geopandas as gpd
#################################################################
# Load Data
k = 'Summary Ejectment'
df = pd.read_csv('./data/evictions_months.csv')
gdf_full = gpd.read_file('./data/durham_tracts/durhamtract.shp')
df_date = df
#---------------------------------------------------------------#
# Manipulate Data for Plotting
df = df.query('process == @k')
df = df.drop(['docket_num', 'tract_name', 'year', 'month', 'process'], axis=1)
df = df.groupby('fips').sum()
df.reset_index(level=0, inplace=True)
gdf = gdf_full[['fips', 'feature_na', 'geometry']]

for i in range(len(gdf.feature_na)): 
    gdf.feature_na[i] = gdf.feature_na[i][13:] # substring feature_na

df.fips = df.fips.astype(object)
for i in range(60):
    gdf.fips[i] = int(gdf.fips[i]) # convert fips into integer
#---------------------------------------------------------------#
# Grab and Convert Coords from Shapefile
gdf['poly_x'] = gdf.apply(fn.getPolyCoords, coord_type='x', axis=1)
gdf['poly_y'] = gdf.apply(fn.getPolyCoords, coord_type='y', axis=1)
gdf['xs'] = gdf.poly_x.map(fn.conv_poly_xs)
gdf['ys'] = gdf.poly_y.map(fn.conv_poly_ys)
#---------------------------------------------------------------#
# Merge Evictions Dataset with Shapefile
mdf = gdf.merge(df, right_on='fips', left_on='fips', how='outer')
#---------------------------------------------------------------#
# Grab Individual Eviction Points
df_date['date'] = df_date['status_date'].apply(fn.time)
df_date['XX'] = df_date['x'].apply(fn.convX)
df_date['YY'] = df_date['y'].apply(fn.convY)
dates = df_date['date'].tolist()
unique_dates = list(set(dates))
sorted_unique_dates = sorted(unique_dates)
initial = df_date[df_date['date'] == sorted_unique_dates[0]]
df_dates = pd.DataFrame({'sorted_unique_dates': sorted_unique_dates})
#---------------------------------------------------------------#
# Output Pickle
df_date.to_pickle('./pickled_files/df_date.pkl')
df_dates.to_pickle('./pickled_files/sorted2.pkl')
initial.to_pickle('./pickled_files/initial2.pkl')
mdf.to_pickle('./pickled_files/mdf.pkl')
#---------------------------------------------------------------#
