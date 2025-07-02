"""
Band Stacking (Multi-band raster creation)

This script contains a function to stack multiple single-band GeoTIFFs 
(Sentinel-2 bands or similar) into a single multi-band raster. 
Useful as a preprocessing step before classification or unsupervised clustering.

Dependencies:
- rasterio
"""

import rasterio

def stack_bands(band_paths, output_path):
    """
    Stack multiple single-band rasters into a multi-band GeoTIFF.

    Parameters:
    ----------
    band_paths : list of str
        List of file paths to the single-band raster files (e.g., ['B02.tif', 'B03.tif', ...])
        All rasters must:
            - Be clipped to the same extent
            - Have the same CRS and resolution
            - Be perfectly aligned (pixel-to-pixel)

    output_path : str
        Path where the output multi-band raster will be saved

    Returns:
    -------
    None
        Saves a new multi-band raster file to the specified output path.

    """
    bands = []
    meta = None

    for path in band_paths:
        with rasterio.open(path) as src:
            band = src.read(1)  
            bands.append(band)

            if meta is None:
                # Copy metadata from the first band as a template
                meta = src.meta.copy()

    # Update metadata to reflect the number of bands in the new stack
    meta.update(count=len(bands))

    # Write out the multi-band raster
    with rasterio.open(output_path, 'w', **meta) as dst:
        for i, band in enumerate(bands, start=1):
            dst.write(band, i)

    print(f"Stacked raster saved to: {output_path}")
