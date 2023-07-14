import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import os

figureDirectory = '~/steady_plots/'
storageDirectory = '/scratch/bell/jjernig/'
try:
	experimentName = 'exomuffin_0-' + sys.argv[1]
except IndexError:
	raise SystemExit(f"Usage: {sys.argv[0]} <experiment name>")
fileDirectory = '/biogem/'
fseaairFileName = 'biogem_series_fseaair_pO2.res'
concentrationFileName = 'biogem_series_ocn_PO4.res'

fseaairData = np.loadtxt(storageDirectory + experimentName + fileDirectory + fseaairFileName, comments="%")
concentrationData = np.loadtxt(storageDirectory + experimentName + fileDirectory + concentrationFileName, comments="%")
time_f = fseaairData[:,0]
fseaair  = fseaairData[:,1]
concentration = concentrationData[:,3]
time_c = concentrationData[:,0]

fig, arr = plt.subplots(2,3,figsize=(30,20), sharex='col',sharey='row')

for j in [0,1,2]:
	arr[0,j].plot(time_f,fseaair/1E12)
	arr[1,j].plot(time_c,concentration*1E6)
	arr[1,j].set_xlabel("Time (yr)", fontsize=30)
	for i in [0,1]:
		arr[i,j].yaxis.set_ticks_position('both')
		arr[i,j].tick_params(labelsize=24)

arr[0,0].set_xlim(0,10000)
arr[0,1].set_xlim(9000,10000)
arr[0,2].set_xlim(9900,10000)
arr[0,0].set_ylabel(r"Total O$_2$ Sea-Air Flux (Tmol yr$^{-1}$)", fontsize=30)
arr[1,0].set_ylabel(r"Surface Phosphorous (10$^{-6}$ mol kg$^{-1}$)", fontsize=30)

fig.tight_layout()
fig.savefig(os.path.expanduser(figureDirectory + experimentName + '_steady.png'))
plt.close(fig)
