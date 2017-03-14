from astropy.table import Table, Column
from spectral_cube import SpectralCube
import numpy as np
import matplotlib.pyplot as plt

cohrs=Table.read('output_catalog_withsfr.fits')
cohrs_mass=Table.read('cohrs_ultimate5_clump_mass.fits')

ir_lum=cohrs['ir_luminosity'] #infrared luminosity
bg_lum=cohrs['bg_lum'] #background luminosity

irlum= (ir_lum-bg_lum)*507.7 #corrected infrared luminosity in solar luminosity

SFR= irlum*1.5e-10 #star formation rate, number per year?

clump_mass=cohrs_mass['Clump Mass']

plt.loglog(clump_mass, SFR)
plt.xlabel('Clump Mass')
plt.ylabel('Star Formation Rate')
plt.show()
