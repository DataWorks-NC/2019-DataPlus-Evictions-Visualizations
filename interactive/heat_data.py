#creating KDE data frame
#imports
from datetime import datetime
startTime = datetime.now() 
import functions as fn
import numpy as np
import pandas as pd
from scipy import stats
from progress.bar import Bar  
#################################################################
#data path
data_path= f'{fn.get_base_dir()}/data/evictionslatlong.csv'
#user controled parameters
bins = 1000
tolerance = 0.01   #for KDEs
bw_divider = 1.5   #what to divide bandwidth by to show neighborhoods more clearly
#---------------------------------------------------------------#
#load data 
df = pd.read_csv(data_path)
df=df[df['process']=='Summary Ejectment']
df['date']=df['status_date'].apply(fn.time)
df=df.sort_values('date')
df['x']=df['x'].apply(fn.reflect)
#globals
X=np.array(df['x'].tolist())
Y=np.array(df['y'].tolist())
#---------------------------------------------------------------#
#unique dates to analyze
dates=df['date'].tolist()
unique_dates=list(set(dates))
sorted_unique_dates=sorted(unique_dates)
df_dates = pd.DataFrame({'sorted_unique_dates': sorted_unique_dates})
#starting date in dataset
df['xneg']=df['x'].apply(fn.reflect)
df['XX']=df['xneg'].apply(fn.convX)
df['YY']=df['y'].apply(fn.convY)
initial=df[df['date']==sorted_unique_dates[0]]
#output dataframes to pickles
initial.to_pickle(f'{fn.get_base_dir()}/pickled_files/initial.pkl')
df.to_pickle(f'{fn.get_base_dir()}/pickled_files/df.pkl')
df_dates.to_pickle(f'{fn.get_base_dir()}/pickled_files/sorted.pkl')
#---------------------------------------------------------------#
#saving max and mins
df_max_min = pd.DataFrame({'xmin': fn.conv_poly_xs([min(-1 * X)]),'xmax': fn.conv_poly_xs([max(-1 * X)]),
                           'ymin': fn.conv_poly_ys([min(Y)]),'ymax': fn.conv_poly_ys([max(Y)]),'xs': [X],'ys': [Y]})
df_max_min.to_pickle(f'{fn.get_base_dir()}/pickled_files/maxmin.pkl')
#---------------------------------------------------------------#
print('--------------------------------------------------------------------------------')
print('Date Formatting: YEAR.[(MONTH)/100]. For example, July 2019 would be enterted as 2019.07')
print('             ')
print('Enter the minimum date for which the KDE algorithm needs to be run (inclusive).')
min_year = float(input('Enter date: '))
print('--------------------------------------------------------------------------------')
#---------------------------------------------------------------#
#KDEs
barmax=len([i for i in sorted_unique_dates if i >= min_year])*bins*bins
with Bar('Making KDEs', max=barmax,fill='#') as bar:
	for i in range(0,len(sorted_unique_dates)):
		if sorted_unique_dates[i] >= min_year:

			#select
			d=sorted_unique_dates[i]
			df_selection=df[df['date']==d]
			#get x,y
			X1=df_selection['x'].tolist()
			Y1=df_selection['y'].tolist()
			#kde
			Sbw=(len(X1))**(-1./(2.+4.))
			bw=Sbw/bw_divider

			A = fn.KDE(X1,Y1,bins,min(X),max(X),min(Y),max(Y),bw)
			density, xxmin, xxmax, yymin, yymax = fn.KDE_plot(A)
			#normalize and nan it
			norm = fn.normalize(density)

			for k in range(bins):
				for j in range(bins):
					if norm[k][j] < tolerance:
						norm[k][j] = np.nan
					bar.next()

			heat_map_df=pd.DataFrame({'date':d,'KDE':[norm]})
			heat_map_df.to_pickle(f'{fn.get_base_dir()}/pickled_files/jar/KDE_' + str(i) + '.pkl')

		else:
			pass
#---------------------------------------------------------------#
print('time to run: ',datetime.now() - startTime)
#---------------------------------------------------------------#
