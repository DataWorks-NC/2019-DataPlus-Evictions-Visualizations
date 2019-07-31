#setting up data for Calendar
#import
import os
import numpy as np
import pandas as pd
import functions as fn
import datetime as dt
#################################################################
# Load Data
df1 = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_evictions.csv')
df2 = pd.read_csv(f'{fn.get_base_dir()}/data/dataworksnc_housing_evictions_2000_2011.csv')
#---------------------------------------------------------------#
# Combine Dataset
df = pd.concat([df1,df2])
df = df.drop(['gid'], axis=1)
df = df.reset_index(drop=True)
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
k = dt.date.today().year
df.at[df.query("data_year == 2003 and status_date == 'Jun'").index.tolist()[0], 'evictions'] = np.nan #'Jun' data is incomplete, so manually muting it for now
df.at[df.query("data_year == 2019 and status_date == 'May'").index.tolist()[0], 'evictions'] = np.nan #'May' data is incomplete, so manually muting it for now

new_years_column = list(df.data_year) + [dt.date.today().year] * (12 - len(df.query('data_year == @k')))

missing_months = [x for x in months if x not in list(df.query('data_year == @k').status_date)]
new_months_column = list(df.status_date) + missing_months

new_evic_column = list(df.evictions) + [np.nan] * 7

#2003 data for Jan - Jun is incomplete, so manually muting it
new_years_column += [2003] * 6
new_months_column += [x for x in months if x not in list(df.query('data_year == 2003').status_date)]
new_evic_column += [np.nan] * 6
#---------------------------------------------------------------#
# Create new DF
df = pd.DataFrame({'data_year': new_years_column, 'status_date': new_months_column, 'evictions': new_evic_column})
df = df.sort_values(by=['data_year', 'status_date'])
#---------------------------------------------------------------#
# Normalize
norm = []
for i in range(df.data_year.min(), df.data_year.max()):
	if i == 2003:
		query = df.query('data_year == 2002').evictions
		temp = list(df.query('data_year == 2003').evictions)
		for j in range(len(list(df.query('data_year == 2003').evictions))):
			norm = norm + [(temp[j] - query.min()) / (query.max() - query.min())]
	else:
		norm = norm + (list(fn.normalize(df.query(f'data_year == {i}').evictions)))
temp = list(df.query('data_year == @k').evictions)

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
