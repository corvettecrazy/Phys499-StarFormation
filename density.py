from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np
import matplotlib.pyplot as plt

bgps=Table.read('bgps_v2.1.fits')
cohrs=Table.read('cohrs_ultimate5_clump_mass.fits')
t=Table.read('BGPS_with_cohrs.fits')

clumpdensity=Column(np.zeros(len(t)), name = 'Clump density')

for idx,row in enumerate(t): #for loop that runs through every row in t
	cohrs_label = int(row['COHRS_label']) #defining the cohrs object number
	bgps_label=int(row['BGPS_NUMBER']) #defining the bgps cloud number
	if cohrs_label != 0:
		mass=13.1 * (cohrs[cohrs_label-1]['distance']/1E3)**2 * (bgps[bgps_label-1]['flux']) #in solar mass
		try: 		
			radius=np.float(bgps[bgps_label]['rad'])*cohrs[cohrs_label-1]['distance']/206265 #in parsecs
			density=3*mass/(4*np.pi*(radius)**3)
			clumpdensity[idx] = density
		except ValueError: 
			pass		

t.add_column(clumpdensity)
t.write('BGPS_with_cohrs_and_clumpdensity.fits', overwrite = True)

