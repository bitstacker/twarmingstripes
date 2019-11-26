# -*- coding: utf-8; -*-

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import os

#Add your local path here for loading the csv
#os.chdir('/Users/your_local_path_here')
os.chdir('C:\Temp\climat')

#Name of CSV file containing the data (one column only)
temp_data = 'global_temps.csv'
#temp_data = 'combined_temps_base_1971_to_2000.csv'


savename = 'global_temps_line'

temps = np.genfromtxt(temp_data, delimiter=",", usecols=(5))[1:]
#temps = np.genfromtxt(temp_data, delimiter=",")

temps_normed = ((temps - temps.min(0)) / temps.ptp(0)) * (len(temps) - 1)
print ( temps)
elements = len(temps)

x_lbls = np.arange(elements)
print (x_lbls)
y_vals = temps_normed / (len(temps) - 1)
y_vals2 = np.full(elements, 1)
bar_wd  = 2

# choose colormap to use for bars, by default RdBu_r
# Choose one diverging colormaps type
# https://matplotlib.org/users/colormaps.html
my_cmap = plt.cm.RdBu_r
norm = Normalize(vmin=0, vmax=elements - 1)

def colorval(num):
    return my_cmap(norm(num))

#print(list(map(colorval, temps_normed)).reshape(-1,4))

fig=plt.figure(figsize=(12,6))
plt.axis('off')
plt.axis('tight')

#Plot warming stripes. Change y_vals2 to y_vals to plot stripes under the line only.
plt.bar(x_lbls, y_vals2, color = list(map(colorval, temps_normed)), width=1.0)

#Plot temperature timeseries. Comment out to only plot stripes
#plt.plot(x_lbls, y_vals - 0.002, color='black', linewidth=1)

plt.xticks( x_lbls + bar_wd, x_lbls)
plt.ylim(0, 1)
fig.subplots_adjust(bottom = 0)
fig.subplots_adjust(top = 1)
fig.subplots_adjust(right = 1.005)
fig.subplots_adjust(left = 0)
fig.savefig(savename+'.png', dpi=600)
