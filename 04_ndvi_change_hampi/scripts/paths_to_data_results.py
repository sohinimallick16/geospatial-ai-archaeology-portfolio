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
        "nir_dry": os.path.join(data_dir, 'nir_20240205.tiff'),
        "red_dry": os.path.join(data_dir, 'red_20240205.tiff'),
        "nir_wet": os.path.join(data_dir, 'nir_20240530.tiff'),
        "red_wet": os.path.join(data_dir, 'red_20240530.tiff'),

        # NDVI raster outputs
        "ndvi_dry": os.path.join(results_dir, 'ndvi_hampi_dry.tif'),
        "ndvi_wet": os.path.join(results_dir, 'ndvi_hampi_wet.tif'),
        "ndvi_diff": os.path.join(results_dir, 'ndvi_diff.tif'),

        # Visualization: NDVI maps
        "plot_dry": os.path.join(results_dir, 'ndvi_hampi_dry.png'),
        "plot_wet": os.path.join(results_dir, 'ndvi_hampi_wet.png'),
        "plot_diff": os.path.join(results_dir, 'ndvi_diff_map.png'),

        # Visualization: histograms
        "hist_dry": os.path.join(results_dir, 'histogram_dry.png'),
        "hist_wet": os.path.join(results_dir, 'histogram_wet.png'),
        "hist_diff": os.path.join(results_dir, 'histogram_diff.png'),
    }

    return paths
