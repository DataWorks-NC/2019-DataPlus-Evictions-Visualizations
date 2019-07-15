#setting up data for Calendar
#import
import os
import numpy as np
import pandas as pd
import functions as fn
import datetime as dt
#################################################################
# Load Data
df = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_evictions.csv')
#---------------------------------------------------------------#
# Filter, Select, and Clean Dataset
k = 'Summary Ejectment'
df = df.query('process == @k')
df = df[['data_year', 'status_date']]
df.status_date = df.status_date.apply(fn.monthConverter)
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
#---------------------------------------------------------------#
# Transpose again and reset index so columns become: 'data_year', 'status_date', 'evictions'
df = pd.DataFrame(df.stack(), columns=['evictions']).reset_index()
#---------------------------------------------------------------#
# Extend DF by creating new columns with necessary info
new_years_column = list(df.data_year) + [dt.date.today().year] * (12 - len(df.query('data_year == 2019')))

missing_months = [x for x in months if x not in list(df.query('data_year == 2019').status_date)]
new_months_column = list(df.status_date) + missing_months

new_evic_column = list(df.evictions) + [np.nan] * 7
#---------------------------------------------------------------#
# Create new DF
df = pd.DataFrame({'data_year': new_years_column, 'status_date': new_months_column, 'evictions': new_evic_column})
df = df.sort_values(by=['data_year', 'status_date'])
#---------------------------------------------------------------#
# Normalize
norm = []
for i in range(2012, 2019):
	norm = norm + (list(fn.normalize(df.query(f'data_year == {i}').evictions)))
temp = list(df.query('data_year == 2019').evictions)

temp[8] = np.nan #'May' data is incomplete, so manually muting it for now

k = dt.date.today().year - 1
query = df.query('data_year == @k').evictions
for i in range(len(temp)): #Normalizing most up-to-date data using previous year's data, 2019 >> 2018
	temp[i] = (temp[i] - query.min()) / (query.max() - query.min())

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
df.to_pickle(f'{fn.get_base_dir()}/pickled_files/df_calendar.pkl')
np.save(os.path.join('npy', 'years'), years)
np.save(os.path.join('npy', 'months'), months)
#---------------------------------------------------------------#


