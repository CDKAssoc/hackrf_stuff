from scipy import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv
from itertools import cycle
from pylab import *
from pandas import *
from datetime import *
from tqdm import tqdm
import time

data = read_csv('hackscanout.txt',
                     delimiter=',',
                     usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
                     names=['date','time','startfreq','stopfreq','step','num_samples',
                                    'dB0','dB1','dB2','dB3','dB4','dB5','dB6','dB7','dB8','dB9',
                                    'dB10','dB11','dB12','dB13','dB14','dB15','dB16','dB17','dB18','dB19',
                                    'dB20','dB21','dB22','dB23','dB24'
                                    ], 
                     header=0,)

def timetosecs(timestring):
            timesplit = timestring.split(':')
            timeseconds = int(timesplit[0])*60*60 + int(timesplit[1])*60 + float(timesplit[2])
            return timeseconds

hack_freq_steps = 5 #MHz
hack_hz_bin_width = 200000 # Hz
channelwidth = hack_hz_bin_width/1000000.  #in MHz

fdivs =25                                                                          
time_zero = timetosecs(data.time[0])
                                          
points = len(data)
print points

plotdata=[]

print 'parsing the data...'
print '\n'
time.sleep(1)

for i in tqdm(range(points)):
    #print i,time
    etime = float(timetosecs(data.time[i])-time_zero)
    for j in range(0,fdivs):
        freq = data.startfreq[i]/1000000+j*channelwidth
        amp = float(data.loc[i][j+6])
        plotdata.append([freq,amp,etime])

plotdata_df= DataFrame.from_records(plotdata, columns=['x','z','y']) #convert list to dataframe

print 'remove low power samples...'
print '\n'
time.sleep(1)
threshold = -70
plotdata_culled = plotdata_df.query('z >' + str(threshold))
plotdata_culled.reset_index(inplace = True)

plotdata_culled.to_csv('plotpoints.csv')
'''
print 'creating output file...' 
with open('plotpoints.txt','w') as file:
    csv_writer =csv.writer(file)
    csv_writer.writerows(plotdata)
    '''