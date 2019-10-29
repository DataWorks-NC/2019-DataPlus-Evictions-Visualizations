#acquiring data
#imports
from datetime import datetime
startTime = datetime.now() 
import sys, os
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2
import _functions as fn
#---------------------------------------------------------------#
#user input of credentials
name=input('Username: ')
pssword=input('Password: ')
#---------------------------------------------------------------#
PGHOST=input('Host: ')
PGDATABASE=input('Database: ')
PGUSER=name
PGPASSWORD=pssword
#---------------------------------------------------------------#
#set up a connection to the postgres server.
conn_string = 'host='+ PGHOST +' port='+ '5432' +' dbname='+ PGDATABASE +' user=' + PGUSER +' password='+ PGPASSWORD
conn=psycopg2.connect(conn_string)
print('Connected to Server')
#create a cursor object
cursor = conn.cursor()
#---------------------------------------------------------------#
#test eviction data loading
evictions=fn.load_data('housing','evictions')
summary_ejectments_blockgroup_year=fn.load_data('housing','summary_ejectments__blockgroup__year')
summary_ejectments_tract_year=fn.load_data('housing','summary_ejectments__tract__year')
#evictions_blockgroup_months.csv# to add
#evictions_tract_months.csv# to add
#evictionslatlong.csv# to add
print('Data Loaded From: '+PGDATABASE)
print('Time to Load: ',datetime.now() - startTime)
#---------------------------------------------------------------#
#save data to location
evictions.to_csv('./data/dataworksnc_housing_evictions.csv')
summary_ejectments_blockgroup_year.to_csv('./data/dataworksnc_housing_summary_ejectments__blockgroup__year.csv')
summary_ejectments_tract_year.to_csv('./data/dataworksnc_housing_summary_ejectments__tract__year.csv')
## ADD.to_csv('./data/evictions_blockgroup_months.csv')
## ADD.to_csv('.data/evictions_tract_months.csv')
## ADD.to_csv('.data/evictionslatlong.csv')
print('data saved to working directory')
#---------------------------------------------------------------#
print('time to run: ',datetime.now() - startTime)
