#creating KDE data frame
#imports
import _functions as fn
import numpy as np
import pandas as pd
from scipy import stats
from progress.bar import Bar  
#################################################################
#data path
data_path='./data/evictionslatlong.csv'
#user controled parameters
bins = 250
tolerance = 0.01   #for KDEs
tolerance2 = 0.25  #for KDE differences 
#################################################################
#load data 
df = pd.read_csv(data_path)
df=df[df['process']=='Summary Ejectment']
df['date']=df['status_date'].apply(fn.time)
df=df.sort_values('date')
df['x']=df['x'].apply(fn.reflect)
#globals
xy=[df['x'].tolist(), df['y'].tolist()]
X=xy[0]
Y=xy[1]
xmin=min(X)
xmax=max(X)
ymin=min(Y)
ymax=max(Y)
#---------------------------------------------------------------#
#unique dates to analyze
dates=df['date'].tolist()
unique_dates=list(set(dates))
sorted_unique_dates=sorted(unique_dates)
df_dates = pd.DataFrame({'sorted_unique_dates': sorted_unique_dates})
df_dates.to_pickle('./pickled_files/sorted.pkl')
#---------------------------------------------------------------#
#saving max and mins
df_max_min = pd.DataFrame({'xmin': fn.conv_poly_xs([min(-1 * np.array(xy[0]))]),'xmax': fn.conv_poly_xs([max(-1 * np.array(xy[0]))]),
                           'ymin': fn.conv_poly_ys([min(xy[1])]),'ymax': fn.conv_poly_ys([max(xy[1])]),'xs': [xy[0]],'ys': [xy[1]]})
df_max_min.to_pickle('./pickled_files/maxmin.pkl')
#---------------------------------------------------------------#
df['xneg']=df['x'].apply(fn.reflect)
df['XX']=df['xneg'].apply(fn.convX)
df['YY']=df['y'].apply(fn.convY)
initial=df[df['date']==sorted_unique_dates[0]]
initial.to_pickle('./pickled_files/initial.pkl')
df.to_pickle('./pickled_files/df.pkl')
#---------------------------------------------------------------#
#KDEs
normframe=[]
normframe_nans=[]
barmax=len(sorted_unique_dates)*bins*bins
with Bar('Making KDEs', max=barmax,fill='#') as bar:
	for i in range(0,len(sorted_unique_dates)):
    	#select
		df_selection=df[df['date']==sorted_unique_dates[i]]
		#get x,y
		X1=df_selection['x'].tolist()
		Y1=df_selection['y'].tolist()
		#kde
		A = fn.KDE(X1, Y1, bins, xmin, xmax, ymin, ymax)
		density, xxmin, xxmax, yymin, yymax = fn.KDE_plot(A)
		#normalize and nan it
		norm = fn.normalize(density)
		Norm = fn.normalize(density)
		for k in range(bins):
			for j in range(bins):
				if norm[k][j] < tolerance:
					norm[k][j] = np.nan
				bar.next()
		norm=np.array(norm)
		normframe_nans.append(norm)
		Norm=np.array(Norm)
		normframe.append(Norm) 
#---------------------------------------------------------------#
# create dataframe
heat_map_df=pd.DataFrame({'date':sorted_unique_dates,'KDE':normframe_nans,'KDE_raw':normframe})
heat_map_df.to_pickle('./pickled_files/KDE_df.pkl')
#---------------------------------------------------------------#
# #producing KDE differences 
# normframe_diff=[]
# normframe_diff_nans=[]
# date_ranges=[]
# barmax1=(len(normframe)-1)*bins*bins
# with Bar('KDE differences', max=barmax1,fill='#') as bar:
# 	for i in range(0,len(normframe)-1):
# 		delta_m=normframe[i+1]-normframe[i]

# 		normed_delta=fn.normalize2(delta_m)
# 		Normed_delta=fn.normalize2(delta_m)
# 		normframe_diff.append(normed_delta)

# 		date_ranges.append(str(sorted_unique_dates[i+1])+'-'+str(sorted_unique_dates[i]))

# 		for i in range(bins):
# 			for j in range(bins):
# 				if abs(Normed_delta[i][j]) < tolerance2:
# 					Normed_delta[i][j] = np.nan
# 				bar.next()
# 		normframe_diff_nans.append(Normed_delta)
# heat_map_diff_df=pd.DataFrame({'date_range':date_ranges,'KDE_diffs':normframe_diff_nans,'KDE_diffs_raw':normframe_diff})
# heat_map_diff_df.to_pickle('./pickled_files/KDE_diffs_df.pkl')
# #---------------------------------------------------------------#
# #total durham changes
# total_diffs=sum(normframe_diff)
# total_diffs=fn.normalize(total_diffs)
# total_diffs_nans=total_diffs
# barmax2=bins*bins
# with Bar('Diffs', max=barmax2,fill='#') as bar:
# 	for i in range(bins):
# 		for j in range(bins):
# 			if abs(total_diffs_nans[i][j]) < tolerance:
# 				total_diffs_nans[i][j] = np.nan
# 			bar.next()	
# normed_total_diffs = fn.normalize2(total_diffs)
# total_diff_df=pd.DataFrame({'type':['total_diff'],'KDE_tdiff':[total_diffs_nans],'KDE_tdiff_raw':[total_diffs]})
# total_diff_df.to_pickle('./pickled_files/KDE_sum_diffs_df.pkl')
# #---------------------------------------------------------------#
