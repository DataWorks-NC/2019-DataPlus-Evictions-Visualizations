import numpy as np
import pandas as pd
import os
from scipy import stats

def reflect(input):

    return -1.0*input

def time(input):
    strarray = input.split('-')
    farray=[float(i) for i in strarray ]
    #year, month, day
    return farray[0]+(farray[1]/100.0)

def conv_poly_ys(row):
    import math
    r = 6378137.0
    return [math.log(math.tan(math.pi / 4 + math.radians(x) / 2)) * r for x in row]

def conv_poly_xs(row):
    import math
    r = 6378137.0
    return [math.radians(x) * r for x in row]

def convY(input):
    import math
    r = 6378137.0
    return math.log(math.tan(math.pi / 4 + math.radians(input) / 2)) * r 

def convX(input):
    import math
    r = 6378137.0
    return math.radians(input) * r 

def KDE(x,y,bins,xmin,xmax,ymin,ymax,bw):
    nbins=bins
    data=[x,y]
    kde = stats.gaussian_kde(data)
    kde.set_bandwidth(bw_method=bw)
    xx, yy = np.mgrid[xmin:xmax:nbins*1j, ymin:ymax:nbins*1j]
    density = kde(np.c_[xx.flat, yy.flat].T).reshape(xx.shape)
    density=np.transpose(density)
    return [xx,yy,density]

def KDE_plot(kde_data):
    #make layout
    xx=-1.0*np.array(kde_data[0])
    yy=kde_data[1]
    #flip density
    density=np.array(kde_data[2])
    density=np.flip(np.flip(density),0)
    #define image max/min
    xxmin=xx.min()
    xxmax=xx.max()
    yymin=yy.min()
    yymax=yy.max()
    return density, xxmin, xxmax, yymin, yymax

def normalize(data):
    b=np.interp(data, (data.min(), data.max()), (0,1))
    return b

def normalize2(data):
    b=np.interp(data, (data.min(), data.max()), (-1,1))
    return 

def normalize3(input, data):
    return ((input - min(data)) / (max(data) - min(data)))

def getPolyCoords(row, coord_type, geom="geometry"):
    exterior = row[geom].exterior
    if coord_type == "x":
        return list(exterior.coords.xy[0])
    if coord_type == "y":
        return list(exterior.coords.xy[1])

def monthConverter(input):
    strarray = input.split('/')
    month = int(strarray[0])
    if month == 1:
        return 'Jan'
    if month == 2:
        return 'Feb'
    if month == 3:
        return 'Mar'
    if month == 4:
        return 'Apr'
    if month == 5:
        return 'May'
    if month == 6:
        return 'Jun'
    if month == 7:
        return 'Jul'
    if month == 8:
        return 'Aug'
    if month == 9:
        return 'Sep'
    if month == 10:
        return 'Oct'
    if month == 11:
        return 'Nov'
    if month == 12:
        return 'Dec'  

def load_data(schema, table):

    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    print ('sql command: '+sql_command)

    # Load the data
    data = pd.read_sql(sql_command, conn)

    print('data shape: '+str(data.shape))
    return (data)


def get_base_dir():
    return os.path.dirname(__file__)

def datetimeconv(input):
    return datetime.strptime(input, '%Y-%m-%d')

def datestrconv(input):
    strarray = input.split('/')
    return strarray[2] + '-' + strarray[0] + '-' + strarray[1]
              
