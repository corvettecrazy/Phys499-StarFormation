from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np

t=Table.read('BGPS_with_cohrs.fits') #import data

y=t['COHRS_label'].data #make vector of object numbers
print y

vals=np.unique(y) #find the number of unique values in y
for val in vals:
	count = val (y == val)
	print count
