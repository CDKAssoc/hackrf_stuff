from scipy import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from matplotlib.mlab import bivariate_normal
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import csv
from itertools import cycle
from pylab import *
from pandas import *
from datetime import *
from scipy.interpolate import griddata
from tqdm import tqdm
import time
import matplotlib.colors as colors

plt.close('all')

print 'reading parsed file...'
plotdata_in = read_csv('plotpoints.csv',
                     delimiter=',',
                     usecols = (2,3,4),
                     names=['x','z','y'       #freq, amp, time
                                    ], 
                     header=0,)

#filename, startfreq, stopfreq, vmin, vmax, 
name=0
freqstart=1
freqstop=2
pwrlo=3
pwrhi=4
plotparams = [
                        ['data900',902,928,-70,-50],
                        ['data24',2400,2500,-70,-20],
                        ['data36',3655,3700,-70,-50],
                        ['data5',5170,5835,-70,-50]
                        ]                                                                                    
                                                                                                                                                                                                                                                               
data900 = []
data24 = []
data36 =[]
data5 = []


print 'sorting data by freq...'
print '\n'
time.sleep(1)

for band in range(len(plotparams)):
    datatemp=[]
    print 'sorting' + str(plotparams[band][freqstart]) + '-' + str(plotparams[band][freqstop])
    print'\n'
    for i in tqdm(range(len(plotdata_in))):
        if plotdata_in.x[i] >= plotparams[band][freqstart] and plotdata_in.x[i] <= plotparams[band][freqstop]:
            datatemp.append(plotdata_in.iloc[i])
    exec(plotparams[band][name] + " = datatemp")



for band in range(len(plotparams)):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    print 'plotting...'
    time.sleep(1)

    # Plot the surface.
    exec("x, z, y = zip(*"+ plotparams[band][name]+")")
    z = map(float, z)
    grid_x, grid_y = np.mgrid[min(x):max(x):1000j, min(y):max(y):1000j]
    grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

    ax.plot_surface(grid_x, grid_y, grid_z, rstride=10,cstride=10,cmap='gist_rainbow',linewidth=0,vmin=plotparams[band][pwrlo],vmax=plotparams[band][pwrhi])

    ax.set_title(str(plotparams[band][freqstart]) + '-' + str(plotparams[band][freqstop]) +'MHz')
    ax.set_ylabel('time(secs)')
    ax.set_zlabel('Power(dBm)')
    ax.set_xlabel('freq(MHz)')
    ax.set_ylim(0, 22) #time secs
    ax.set_zlim(plotparams[band][pwrlo], plotparams[band][pwrhi]) #dB
    ax.set_xlim(plotparams[band][freqstart], plotparams[band][freqstop]) #freq
    #fig.savefig(plotparams[band][name]+'scan.png',dpi=300)
    plt.show()
