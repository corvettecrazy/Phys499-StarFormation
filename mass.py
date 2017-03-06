from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np

t1=Table.read('bgps_v2.1.fits')
t2=Table.read('cohrs_ultimatecatalog5.fits')

valuecolumn = Column(np.zeros(len(t1)), name='Clump Mass')

distance=t2['distance']
flux=t1['flux']

#Problem: length of distance and flux is not the same

#mass=13.1*flux*distance**2 need to integrate a for loop
