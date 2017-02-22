from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np
import glob

t=Table.read('BGPS_vlsr.fits')

#in this cohrs_fasgn file, the x pixels run from [0,912], the y values run from [0,630], and the velocity runs through [0,188] layers

#I want to loop through all the entries in the BGPS file and convert them from pixel to wcg. There are 3124 items in the BGPS file that will need to be looked through.

#longitude runs from 29.5->30.5 in both the cohrs files

valuecolumn = Column(np.zeros(len(t)), name='COHRS_label') #defines a vector full of zeros, with the same size as t, the BGPS file

filelist = glob.glob('/mnt/bigdata/erosolow/cohrs/FINALASGNS/cohrs*fits')

for filename in filelist:

	s=SpectralCube.read(filename)
	data = s.filled_data[:]

	for index, row in enumerate(t): #defines a variable called index, which will keep track of which items our input and output data belong to
		lon, lat, vel = row['GLON'], row['GLAT'], row['VLSR']

		x, y, z = s.wcs.wcs_world2pix(lon, lat, vel*1E3, 0) #takes the 		inputed wgc coordinate, and converts it to a pixel number
		if x > 0 and x < s.shape[2]: 
			if y > 0 and y < s.shape[1]:

				#print x,y,z
				val=data[int(z), int(y), int(x)] #takes 			the pixel number from the BGPS file, and assigns that 				to the coresponding	object in the cohrs file
				print val
				valuecolumn[index] = val
t.add_column(valuecolumn) #adds the cohrs item number to BGPS data file
t.write('BGPS_with_cohrs.fits', overwrite = True) #saves the new BGPS file with the cohrs item numbers. The true part will make sure the file is overwritten everytime I run it
#typing val into the command window now displays what object number that coordinate coresponds to in the cohrs file. If I were to type x,y,z into the command window, I would see specifically what pixels we are looking at in the cohrs file. 
