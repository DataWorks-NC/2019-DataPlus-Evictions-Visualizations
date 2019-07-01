#setting up data for Chloropleth
#import
import _functions as fn
import pandas as pd
import geopandas as gpd
#################################################################
# Load Data
k = 'Summary Ejectment'
df_tract_m = pd.read_csv('./data/evictions_tract_months.csv')
df_tract_y = pd.read_csv('./data/dataworksnc_housing_summary_ejectments__tract__year.csv')
df_blockg_m = pd.read_csv('./data/evictions_blockgroup_months.csv')
df_blockg_y = pd.read_csv('./data/dataworksnc_housing_summary_ejectments__blockgroup__year.csv')
df_date = pd.read_csv('./data/evictionslatlong.csv')
gdf_tract = gpd.read_file('./data/durham_tracts/durhamtracts.shp')
gdf_blockg = gpd.read_file('./data/durham_blockgroups/durhamblockgroups.shp')
#---------------------------------------------------------------#
# Manipulate Data for Plotting
df_tract_m = df_tract_m.query('process == @k')
df_blockg_m = df_blockg_m.query('process == @k')

temp1 = df_tract_m[['fips','tract']]
temp1 = temp1.drop_duplicates()
temp1.reset_index(drop=True)

temp2 = df_blockg_m[['fips','tract', 'blockgroup']]
temp2 = temp2.drop_duplicates()
temp2.reset_index(drop=True)

df_tract_m = df_tract_m.drop(['docket_num', 'year', 'month', 'process', 'tract', 'status_date'], axis=1)
df_tract_m = df_tract_m.groupby('fips').sum()
df_tract_m.reset_index(level=0, inplace=True)
tract_month = df_tract_m.merge(temp1, left_on='fips', right_on='fips')

df_blockg_m = df_blockg_m.drop(['docket_num', 'year', 'month', 'process', 'tract', 'blockgroup', 'status_date'], axis=1)
df_blockg_m = df_blockg_m.groupby('fips').sum()
df_blockg_m.reset_index(level=0, inplace=True)
blockg_month = df_blockg_m.merge(temp2, left_on='fips', right_on='fips')

tract_year = df_tract_y.merge(temp1, left_on='fips', right_on='fips')
blockg_year = df_blockg_y.merge(temp2, left_on='fips', right_on='fips')


gdf_t = gdf_tract[['fips', 'geometry', 'area__sqmi']]
gdf_bg = gdf_blockg[['fips', 'geometry', 'area__sqmi']]

for i in range(len(gdf_t)):
    gdf_t.fips[i] = int(gdf_t.fips[i]) # convert fips into integer

for i in range(len(gdf_bg)):
    gdf_bg.fips[i] = int(gdf_bg.fips[i]) # convert fips into integer
#---------------------------------------------------------------#
# Grab and Convert Coords from Shapefile
gdf_t['poly_x'] = gdf_t.apply(fn.getPolyCoords, coord_type='x', axis=1)
gdf_t['poly_y'] = gdf_t.apply(fn.getPolyCoords, coord_type='y', axis=1)
gdf_t['xs'] = gdf_t.poly_x.map(fn.conv_poly_xs)
gdf_t['ys'] = gdf_t.poly_y.map(fn.conv_poly_ys)

gdf_bg['poly_x'] = gdf_bg.apply(fn.getPolyCoords, coord_type='x', axis=1)
gdf_bg['poly_y'] = gdf_bg.apply(fn.getPolyCoords, coord_type='y', axis=1)
gdf_bg['xs'] = gdf_bg.poly_x.map(fn.conv_poly_xs)
gdf_bg['ys'] = gdf_bg.poly_y.map(fn.conv_poly_ys)
#---------------------------------------------------------------#
# Merge Evictions Dataset with Shapefile
mdf1 = gdf_t.merge(tract_month, right_on='fips', left_on='fips', how='outer')
mdf2 = gdf_t.merge(tract_year, right_on='fips', left_on='fips', how='outer')
mdf3 = gdf_bg.merge(blockg_month, right_on='fips', left_on='fips', how='outer')
mdf4 = gdf_bg.merge(blockg_year, right_on='fips', left_on='fips', how='outer')
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
mdf1.to_pickle('./pickled_files/mdf1.pkl')
mdf2.to_pickle('./pickled_files/mdf2.pkl')
mdf3.to_pickle('./pickled_files/mdf3.pkl')
mdf4.to_pickle('./pickled_files/mdf4.pkl')
#---------------------------------------------------------------#
