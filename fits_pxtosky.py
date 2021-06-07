from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt

# Open desired FITS file and output header information
# header_data_unit_list = fits.open('https://github.com/astropy/astropy-data/raw/6d92878d18e970ce6497b70a9253f65c925978bf/tutorials/celestial-coords1/tailored_dss.22.29.38.50-20.50.13_60arcmin.fits')
header_data_unit_list = fits.open('C:\h_e_20201118_55_1_1_1.fits')
header_data_unit_list.info()

# Open FITS header data
header = header_data_unit_list[0].header

# Open FITS image data
image = header_data_unit_list[0].data

# Read in WCS values from FITS header
wcs_helix = WCS(header)
wcs_helix


# Plot figure
fig = plt.figure(figsize=(10, 10))
plt.imshow(image, origin='lower', cmap='cividis')