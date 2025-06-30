"""
NDVI Calculator Script
----------------------

This script takes two clipped GeoTIFF raster files — NIR (B08) and Red (B04) —
and calculates the NDVI index, saving the output as a GeoTIFF.

NDVI = (NIR - Red) / (NIR + Red)

Author: Sohini Mallick
Project: NDVI-based Vegetation Masking - Hampi, Karnataka, India
"""

import rasterio
import numpy as np
import os

def calculate_ndvi(nir_path, red_path, output_path):
    """
    Calculate NDVI from NIR and Red band raster files.

    Parameters:
    - nir_path (str): File path to NIR band (Band 8)
    - red_path (str): File path to Red band (Band 4)
    - output_path (str): File path to save the NDVI GeoTIFF
    """

    # Open NIR band
    with rasterio.open(nir_path) as nir_src:
        nir = nir_src.read(1).astype('float32')
        profile = nir_src.profile   

    # Open Red band
    with rasterio.open(red_path) as red_src:
        red = red_src.read(1).astype('float32')

     # Avoid division by zero
    ndvi_denominator = (nir + red)
    ndvi_denominator[ndvi_denominator == 0] = 1e-5

    # Calculate NDVI
    ndvi = (nir - red) / ndvi_denominator

    # Update profile for output
    profile.update(
        dtype='float32',
        count=1,
        compress='lzw'
    )

    # Save NDVI raster
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(ndvi, 1)

    print(f"NDVI calculation complete. Output saved to: {output_path}")


