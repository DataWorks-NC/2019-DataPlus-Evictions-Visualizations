#setting up data for Chloropleth
#import
import functions as fn
import pandas as pd
import geopandas as gpd
#################################################################
# Load Data
k = 'Summary Ejectment'
df_tract_m1 = pd.read_csv(f'{fn.get_base_dir()}/data/evictions_tract_months.csv')
df_tract_m2 = pd.read_csv(f'{fn.get_base_dir()}/data/evictions_tract_months_2000_2011.csv')
df_tract_m2.tract = df_tract_m2.tract.replace(1.0, 9801.0)
df_tract_m2['status_date'] = df_tract_m2['status_date'].apply(fn.datestrconv)
df_tract_m = pd.concat([df_tract_m1,df_tract_m2], sort=False)
df_tract_m = df_tract_m.fillna(0)
df_tract_m = df_tract_m.sort_values(by=['year'])

df_tract_y1 = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_summary_ejectments__tract__year.csv')
df_tract_y2 = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_summary_ejectments__tract__year_2000_2011.csv')
df_tract_y = df_tract_y2.merge(df_tract_y1, right_on='fips', left_on='fips', how='outer')

df_blockg_m1 = pd.read_csv(f'{fn.get_base_dir()}/data/evictions_blockgroup_months.csv')
df_blockg_m2 = pd.read_csv(f'{fn.get_base_dir()}/data/evictions_blockgroup_months_2000_2011.csv')
df_blockg_m2['status_date'] = df_blockg_m2['status_date'].apply(fn.datestrconv)
df_blockg_m = pd.concat([df_blockg_m1,df_blockg_m2], sort=False)
df_blockg_m = df_blockg_m.fillna(0)
df_blockg_m = df_blockg_m.sort_values(by=['year'])

df_blockg_y1 = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_summary_ejectments__blockgroup__year.csv')
df_blockg_y2 = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_summary_ejectments__blockgroup__year_2000_2011.csv')
df_blockg_y = df_blockg_y2.merge(df_blockg_y1, right_on='fips', left_on='fips', how='outer')

df_date1 = pd.read_csv(f'{fn.get_base_dir()}/data/evictionslatlong.csv')
df_date2 = pd.read_csv(f'{fn.get_base_dir()}/data/evictionslatlong_2000_2011.csv')
df_date2['status_date'] = df_date2['status_date'].apply(fn.datestrconv)
df_date = pd.concat([df_date1,df_date2])

gdf_tract = gpd.read_file(f'{fn.get_base_dir()}/data/durham_tracts/durhamtracts.shp')
gdf_blockg = gpd.read_file(f'{fn.get_base_dir()}/data/durham_blockgroups/durhamblockgroups.shp')
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
# Output Pickle
mdf1.to_pickle(f'{fn.get_base_dir()}/pickled_files/mdf1.pkl')
mdf2.to_pickle(f'{fn.get_base_dir()}/pickled_files/mdf2.pkl')
mdf3.to_pickle(f'{fn.get_base_dir()}/pickled_files/mdf3.pkl')
mdf4.to_pickle(f'{fn.get_base_dir()}/pickled_files/mdf4.pkl')
#---------------------------------------------------------------#
