# NDVI-Based Vegetation Masking – Hampi

This project demonstrates the use of NDVI (Normalized Difference Vegetation Index) to identify and mask vegetated areas around the Hampi Group of Monuments (UNESCO World Heritage Site) using Sentinel-2 satellite imagery and Python.

## 📍 Study Area

- **Location**: Hampi, Karnataka, India
- **Coordinates**: approx. 15.3350° N, 76.4619° E
- **AOI**: Manually defined polygon enclosing the core monument zone

## 🎯 Objective

To calculate NDVI from Sentinel-2 bands and generate a vegetation mask that highlights areas with NDVI > 0.4 (dense vegetation), potentially obscuring archaeological features.

## 🛰️ Data Used

| Source | Description |
|--------|-------------|
| Sentinel-2 (L2A) | Band 4 (Red) and Band 8 (NIR), 10m resolution |
| GeoJSON AOI | Custom-drawn boundary around Hampi monuments |

## 🛠️ Tools and Libraries

- QGIS (AOI generation, visualization)
- Python 3.8
  - `rasterio`, `numpy`, `matplotlib`

## 🔄 Workflow

1. Download Sentinel-2 bands for Hampi
2. Clip B04 and B08 rasters to AOI
3. Calculate NDVI: `(NIR - Red) / (NIR + Red)`
4. Generate vegetation mask: NDVI > 0.4
5. Visualize and export results

## 🖼️ Outputs

| Output File | Description |
|-------------|-------------|
| `ndvi_hampi.tiff` | NDVI GeoTIFF |
| `ndvi_hampi.png` | NDVI visualization |
| `vegetation_mask.tiff` | Binary vegetation mask (GeoTIFF) |
| `vegetation_mask.png` | Binary mask visualization |

## 🌿 NDVI Preview

![NDVI Hampi](results/ndvi_hampi.png)

## 🚀 Next Steps

- Combine NDVI with DEM/hillshade to map surface features
- Apply the same method to other Indian archaeological sites
- Perform time-series NDVI analysis for change detection

---







