from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np

t=Table.read('BGPS_with_cohrs.fits') #import data
z=Table.read('cohrs_ultimatecatalog5.fits')
valuecolumn = Column(np.zeros(len(z)), name='COHRS_number_of_hits')

y=t['COHRS_label'].data #make vector of object numbers
#print y

vals=np.unique(y) #find the number of unique values in y
vals = vals[1:] #starts reading vals at the second entry. It starts at zero, which we don't care about how many times zero is present.

for val in vals:
	count = np.sum(y == val)
	#print count
	valuecolumn[val-1] = count

z.add_column(valuecolumn)
z.write('cohrs_ultimatecatalog5_with_num_hits.fits', overwrite = True)
