from scipy import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import csv
from itertools import cycle
from pylab import *
from pandas import *
from datetime import *

plt.close('all')

data = read_csv('hackscanout.txt',
                     delimiter=',',
                     usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
                     names=['date','time','startfreq','stopfreq','step','num_samples',
                                    'dB0','dB1','dB2','dB3','dB4','dB5','dB6','dB7','dB8','dB9',
                                    'dB10','dB11','dB12','dB13','dB14','dB15','dB16','dB17','dB18','dB19',
                                    'dB20','dB21','dB22','dB23','dB24'
                                    ], 
                     header=0,)
   
fdivs = 25
step = 200000
channelwidth = step/1000000.  #in MHz

def timetosecs(timestring):
            timesplit = timestring.split(':')
            timeseconds = int(timesplit[0])*60*60 + int(timesplit[1])*60 + float(timesplit[2])
            return timeseconds
                                                                                  
time_zero = timetosecs(data.time[0])
                                          
points = len(data)
print points

plotdata=[]
for i in range(points):
    print i,time
    time = timetosecs(data.time[i])-time_zero
    for j in range(0,fdivs):
        freq = data.startfreq[i]+j*channelwidth
        amp = data.loc[i][j+6]
        plotdata.append([freq,amp,time])
   
data.to_csv('plotpoints.csv')
