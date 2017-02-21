from astropy.table import Table
from spectral_cube import SpectralCube

t=Table.read('BGPS_vlsr.fits')
s=SpectralCube.read('cohrs_30p50_29p50_fasgn.fits')


#in this cohrs_fasgn file, the x pixels run from [0,912], the y values run from [0,630], and the velocity runs through [0,188] layers

#I want to loop through all the entries in the BGPS file and convert them from pixel to wcg. There are 3124 items in the BGPS file that will need to be looked through.

#longitude runs from 29.5->30.5 in both the cohrs files

for row in t:
	lon, lat, vel = row['GLON'], row['GLAT'], row['VLSR']

	x, y, z = s.wcs.wcs_world2pix(lon, lat, vel, 0) #takes the 		inputed wgc coordinate, and converts it to a pixel number
	if x > 0 and x < s.shape[2]: 
		if y > 0 and y < 630:

			val=s.filled_data[:][int(z), int(y), int(x)] #takes 			the pixel number from the BGPS file, and assigns that 				to the coresponding	object in the cohrs file

#typing val into the command window now displays what object number that coordinate coresponds to in the cohrs file. If I were to type x,y,z into the command window, I would see specifically what pixels we are looking at in the cohrs file. 
