import os,sys
sys.path.append('../')

def get_project_paths():
    ROOT = os.path.abspath('..')
    data_dir = os.path.join(ROOT, 'data')
    results_dir = os.path.join(ROOT, 'results')

    paths = {
        "data_dir": data_dir,
        "results_dir": results_dir,

        # Band inputs
        "blue_band": os.path.join(data_dir, 'B02.tiff'),
        "green_band": os.path.join(data_dir, 'B03.tiff'),
        "red_band": os.path.join(data_dir, 'B04.tiff'),
        "nir_band": os.path.join(data_dir, 'B08.tiff'),

        # Stacked single multi-band raster
        "stacked_raster": os.path.join(data_dir, 'sentinel_stack.tif'),

        # K-means classification
        "land_cover_kmeans": os.path.join(results_dir,'land_cover_kmeans.tif'),
        "land_cover_visualise": os.path.join(results_dir,'kmeans_class_distribution.png')
    }

    return paths
