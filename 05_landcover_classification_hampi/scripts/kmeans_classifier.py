import rasterio
import numpy as np
from sklearn.cluster import KMeans

def classify_land_cover(input_stack_path, output_class_path, n_classes=5):
    """
    Performs K-Means classification on a multi-band raster.

    Parameters:
        input_stack_path (str): Path to stacked raster
        output_class_path (str): Path to save classified output
        n_classes (int): Number of land cover classes
    """
    with rasterio.open(input_stack_path) as src:
        stack = src.read()  
        profile = src.profile
        profile.update(count=1, dtype='uint8', compress='lzw')

    # Reshape for clustering
    bands, height, width = stack.shape
    reshaped = stack.reshape(bands, -1).T  

    # Mask out no-data
    mask = np.any(reshaped == 0, axis=1)
    valid_pixels = reshaped[~mask]

    print("Running K-Means...")
    kmeans = KMeans(n_clusters=n_classes, random_state=0).fit(valid_pixels)
    labels = np.full((reshaped.shape[0],), fill_value=255, dtype='uint8')  
    labels[~mask] = kmeans.labels_

    # Reshape to raster
    classified = labels.reshape(height, width)

    # Save classified map
    with rasterio.open(output_class_path, 'w', **profile) as dst:
        dst.write(classified, 1)

    print(f"Classified raster saved to {output_class_path}")
