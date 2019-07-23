#creating KDE data frame
#imports
from datetime import datetime 
import functions as fn
import numpy as np
import pandas as pd
from scipy import stats
from progress.bar import Bar  
#################################################################
#data path
df1 = pd.read_csv(f'{fn.get_base_dir()}/data/evictionslatlong.csv')
df2 = pd.read_csv(f'{fn.get_base_dir()}/data/evictionslatlong_2000_2011.csv')
df2['status_date'] = df2['status_date'].apply(fn.datestrconv)
df = pd.concat([df1,df2])
#user controled parameters
bins = 100
tolerance = 0.05   #for KDEs
tolerance2 = 0.25  #for KDE differences 
bw_divider = 1.5
#################################################################
#load data 
df=df[df['process']=='Summary Ejectment']
df['date']=df['status_date'].apply(fn.time)
df=df.sort_values('date')
df['x']=df['x'].apply(fn.reflect)
#globals
startTime = datetime.now()
X=np.array(df['x'].tolist())
Y=np.array(df['y'].tolist())
#---------------------------------------------------------------#
#unique dates to analyze
dates=df['date'].tolist()
unique_dates=list(set(dates))
missing = [2003.01, 2003.02, 2003.03, 2003.04, 2003.05, 2003.07]
sorted_unique_dates = sorted(unique_dates + missing)

df_dates = pd.DataFrame({'sorted_unique_dates': sorted_unique_dates})
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
barmax=len(sorted_unique_dates)*bins*bins
with Bar('Making KDEs', max=barmax,fill='#') as bar:
	for i in range(0,len(sorted_unique_dates)):
		#select
		d=sorted_unique_dates[i]
		df_selection=df[df['date']==d]
		#get x,y
		X1=df_selection['x'].tolist()
		Y1=df_selection['y'].tolist()

		if len(X1) <= 2:
			norm = np.zeros((bins,bins))
			for k in range(bins):
				for j in range(bins):
					norm[k][j]==0
					if norm[k][j] < tolerance:
						norm[k][j] = np.nan
					bar.next()

			heat_map_df=pd.DataFrame({'date':d,'KDE':[norm]})
			heat_map_df.to_pickle(f'{fn.get_base_dir()}/pickled_files/jar/KDE_' + str(i) + '.pkl')
		else:
			#kde
			Sbw=(len(X1))**(-1./(2.+4.))
			bw=Sbw/1.15
			A = fn.KDE(X1,Y1,bins,min(X),max(X),min(Y),max(Y),bw)
			density, xxmin, xxmax, yymin, yymax = fn.KDE_plot(A)
			#normalize and nan it
			norm = fn.normalize(density)
			#Norm = normalize(density)
			for k in range(bins):
				for j in range(bins):
					if norm[k][j] < tolerance:
						norm[k][j] = np.nan
					bar.next()

			heat_map_df=pd.DataFrame({'date':d,'KDE':[norm]})
			heat_map_df.to_pickle(f'{fn.get_base_dir()}/pickled_files/jar/KDE_' + str(i) + '.pkl')
#---------------------------------------------------------------#
print('time to run: ',datetime.now() - startTime)
#---------------------------------------------------------------#
