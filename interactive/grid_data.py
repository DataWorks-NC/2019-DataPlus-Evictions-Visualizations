#setting up data for Calendar
#import
import os
import numpy as np
import pandas as pd
from functions import get_base_dir

#################################################################
# Load Data
df = pd.read_csv(f'{get_base_dir()}/data/dataworksnc_housing_evictions.csv')
#---------------------------------------------------------------#
# Filter, Select, and Clean Dataset
k = 'Summary Ejectment'
df = df.query('process == @k')
df = df[['data_year', 'status_date']]
df.status_date = df.status_date.apply(monthConverter)
#---------------------------------------------------------------#
# Add evictions column with value of one
df['evictions'] = [1] * df.data_year.count()
#---------------------------------------------------------------#
# Groupby year and month and count evictions
df = df.groupby(['data_year', 'status_date']).count()
#---------------------------------------------------------------#
# Transpose so columns become months in 'status_date'
df = df.unstack(level=1)
#---------------------------------------------------------------#
# Setup Globals
years = list(df.index.astype(str))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
missing_months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#---------------------------------------------------------------#
# Transpose again and reset index so columns become: 'data_year', 'status_date', 'evictions'
# Add in missing months as NAN
df = pd.DataFrame(df.stack(), columns=['evictions']).reset_index()
new_years = list(df.data_year) + [2019] * 7
new_months = list(df.status_date) + missing_months
new_evic = list(df.evictions) + [np.nan] * 7
df = pd.DataFrame({'data_year': new_years, 'status_date': new_months, 'evictions': new_evic})
df = df.sort_values(by=['data_year', 'status_date'])
norm = []
for i in range(2012, 2019):
	norm = norm + (list(normalize(df.query(f'data_year == {i}').evictions)))
temp = list(df.query('data_year == 2019').evictions)
temp[8] = np.nan
for i in range(len(temp)):
	temp[i] = (temp[i] - (df.query('data_year == 2018').evictions.min())) / ((df.query('data_year == 2018').evictions.max()) - (df.query('data_year == 2018').evictions.min()))
norm = norm + temp
df['normalize'] = norm
#---------------------------------------------------------------#
# Sort by year and months
df['status_date'] = pd.Categorical(df['status_date'], months)
df = df.sort_values(by=['data_year', 'status_date'])
df = df.rename(columns={'data_year': 'Year', 'status_date': 'Month'})
df = df.reset_index(drop=True)
df.Year = df.Year.astype(str)
df.Month = df.Month.astype(str)
#---------------------------------------------------------------#
# Output Pickle
df.to_pickle('/pickled_files/df_calendar.pkl')
np.save(os.path.join('npy', 'years'), years)
np.save(os.path.join('npy', 'months'), months)
#---------------------------------------------------------------#


