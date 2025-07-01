import rasterio
import numpy as np
import matplotlib.pyplot as plt

def visualize_ndvi(input_path, output_path, title, cmap='RdYlGn', vmin=-1, vmax=1):
    """
    Plots and saves an NDVI map.

    Parameters:
    - input_path (str): Path to the input .tif NDVI file
    - output_path (str): Path to save the PNG output
    - title (str): Title of the plot
    - cmap (str): Colormap for visualization
    - vmin, vmax (float): NDVI value range for color scaling
    """
    with rasterio.open(input_path) as src:
        ndvi = src.read(1)
        meta = src.meta
        nodata = meta.get('nodata', -9999)

    ndvi = np.where(ndvi == nodata, np.nan, ndvi)

    print(f"{title} - NDVI range: {np.nanmin(ndvi):.3f} to {np.nanmax(ndvi):.3f}")

    plt.figure(figsize=(10, 8))
    plt.imshow(ndvi, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.colorbar(label="NDVI")
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
