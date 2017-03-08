from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np
import matplotlib.pyplot as plt

bgps=Table.read('bgps_v2.1.fits')
cohrs=Table.read('cohrs_ultimate5_clump_mass.fits')
t=Table.read('BGPS_with_cohrs.fits')

clumpdensity=Column(np.zeros(len(cohrs)), name = 'Clump density')

for row in t: #for loop that runs through every row in t
	cohrs_label = int(row['COHRS_label']) #defining the cohrs object number
	bgps_label=int(row['BGPS_NUMBER']) #defining the bgps cloud number
	if cohrs_label != 0:
		density=3*cohrs[cohrs_label-1]['Clump Mass']/(4*3.14159*(bgps[bgps_label]['rad'])*cohrs[cohrs_label-1]['distance']/206265)**3)
		clumpdensity[cohrs_label-1] +=density

