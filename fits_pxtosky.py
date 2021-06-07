# fits_pxtosky.py
# Simple script to convert pixel coordinates to sky (RADEC) coordinates taken from # https://learn.astropy.org/rst-tutorials/celestial_coords1.html?highlight=filtertutorials#step-2-read-in-the-fits-image-coordinate-system-with-astropy-wcs-wcs

# Simon George (2021)
# zinar7@gmail.com


# Import astropy and everything needed
from astropy.wcs import WCS
from astropy.io import fits
from astropy.wcs.utils import pixel_to_skycoord
import matplotlib.pyplot as plt

# Open desired FITS file and output header information
# header_data_unit_list = fits.open('https://github.com/astropy/astropy-data/raw/6d92878d18e970ce6497b70a9253f65c925978bf/tutorials/celestial-coords1/tailored_dss.22.29.38.50-20.50.13_60arcmin.fits')
header_data_unit_list = fits.open('C:\h_e_20201118_55_1_1_1.fits')

# Open FITS header data
header = header_data_unit_list[0].header

# Open FITS image data
image = header_data_unit_list[0].data

# Read in WCS values from FITS header
wcs_helix = WCS(header)

# Plot figure (simple)
fig = plt.figure(figsize=(10, 10))
plt.imshow(image, origin='lower', cmap='cividis')

# Plot figure (with sky grid)
fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(projection=wcs_helix)
plt.imshow(image, origin='lower', cmap='cividis', aspect='equal')
plt.xlabel(r'RA')
plt.ylabel(r'Dec')

overlay = ax.get_coords_overlay('icrs')
overlay.grid(color='white', ls='dotted')

# Subtract one because Python is zero-based
xp = 57.5412-1
yp = 61.5412-1

RADEC_new = pixel_to_skycoord(xp, yp, wcs_helix, origin=0, mode='all', cls=None)
print(RADEC_new)