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


def compute_ndvi_difference(ndvi1_path, ndvi2_path, output_path):
    """
    Computes the difference between two NDVI rasters and saves the result as a new raster.

    This function is typically used for temporal NDVI analysis — e.g., comparing vegetation 
    changes between dry and wet seasons or across multiple years.

    Parameters:
    -----------
    ndvi1_path : str
        File path to the first NDVI raster (e.g., from the earlier season or year).
    ndvi2_path : str
        File path to the second NDVI raster (e.g., from the later season or year).
    output_path : str
        File path where the NDVI difference raster will be saved.

    Output:
    -------
    A new GeoTIFF raster will be saved at `output_path`, with pixel values representing:
        NDVI_change = NDVI_later - NDVI_earlier
    Positive values → increase in vegetation
    Negative values → decrease in vegetation

    Notes:
    ------
    - Assumes both NDVI rasters are already pre-processed, clipped to the same AOI,
      and have the same resolution and coordinate system.
    - The output is saved as a single-band float32 raster with LZW compression.
    """

    # Open the first NDVI raster
    with rasterio.open(ndvi1_path) as src1:
        ndvi1 = src1.read(1).astype('float32')
        profile = src1.profile  # Use profile from first raster for output

    # Open the second NDVI raster
    with rasterio.open(ndvi2_path) as src2:
        ndvi2 = src2.read(1).astype('float32')

    # Compute the NDVI difference (second - first)
    ndvi_diff = ndvi2 - ndvi1

    # Update the output raster metadata
    profile.update(
        dtype='float32',
        count=1,
        compress='lzw'
    )

    # Write the NDVI difference to file
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(ndvi_diff, 1)

    print(f"NDVI difference saved to: {output_path}")

