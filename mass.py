from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np
import matplotlib.pyplot as plt

t=Table.read('BGPS_with_cohrs.fits')

bgps=Table.read('bgps_v2.1.fits')
cohrs=Table.read('cohrs_ultimatecatalog5.fits')

clumpmass = Column(np.zeros(len(cohrs)), name='Clump Mass')

for row in t: #for loop that runs through every row in t
	cohrs_label = int(row['COHRS_label']) #defining the cohrs object number
	bgps_label=int(row['BGPS_NUMBER']) #defining the bgps cloud number
	if cohrs_label != 0:
		mass= 13.1 * (cohrs[cohrs_label-1]['distance']/1E3)**2 * (bgps[bgps_label-1]['flux']) #mass in solar mass
#In the above, we feed in the cohrs cloud number into the ultimate catologue and pull the distance to that cloud. Then, we input the bgps number into the v2 catologue and pull the flux of that cloud.
			
		clumpmass[cohrs_label - 1] += mass
cohrs.add_column(clumpmass)
cohrs.write('cohrs_ultimate5_clump_mass.fits', overwrite = True)

totalmass=cohrs['mlum_ex_msun']
#plt.subplot(221)
plt.loglog(totalmass, clumpmass,'ro', label=" ") #x Vs. y

plt.plot([1E0,1E5],[1E0,1E5], lw=3,alpha=0.5, label="100% of Clump mass vs cloud mass") #clumpmass = total mass line
plt.plot([1E0/0.1,1E5/0.1],[1E0,1E5], label="10% of clump mass vs cloud mass")
plt.xlabel('Total Mass')
plt.ylabel('Clump Mass')
plt.title('Total Mass of Dense Gas Clumps Vs. Total Mass of Cloud')
plt.legend()
plt.show()

massfraction=mass/totalmass
#plt.subplot(224)
plt.loglog(totalmass, massfraction)
plt.xlabel('Total Mass')
plt.ylabel('Mass Fraction')
plt.title('Fraction of Cloud Mass Held in Dense Gas Clumps Vs. Total Cloud Mass')
plt.show()
