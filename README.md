# Geospatial Analytics and GeoAI for Archaeology

This portfolio showcases a progressive series of geospatial AI projects focused on archaeological landscape analysis. Each project leverages satellite imagery, elevation models, and open-source geospatial tools (QGIS, Python, GRASS GIS) to explore visibility, vegetation, terrain, and temporal change in cultural heritage sites — starting with the UNESCO World Heritage site of **Hampi, India**.

---

## 📁 Projects Overview

### 1. [NDVI-Based Vegetation Masking – Hampi](01_ndvi_hampi/README.md)
**Objective**: Identify vegetated vs. non-vegetated areas using Sentinel-2 satellite imagery.  
**Method**: Calculate NDVI in Python to support further archaeological feature detection.  
**Output**: A binary vegetation mask map and NDVI raster visualized in QGIS.

---

### 2. [Terrain Analysis Using DEM – Hampi](02_terrain_hampi/README.md)
**Objective**: Understand elevation patterns and terrain variation across the Hampi landscape.  
**Method**: Generate hillshades and elevation histograms using DEM data.  
**Output**: A shaded relief map and statistical terrain profile of the area.

---

### 3. [Viewshed Analysis – Hampi](03_viewshed_hampi/README.md)
**Objective**: Simulate lines of sight from key monuments (Virupaksha Temple & Hemakuta Hill).  
**Method**: Perform viewshed analysis using GRASS `r.viewshed` in QGIS.  
**Output**: Visibility maps.

### 4. [NDVI Temporal Change Analysis – Hampi (Wet vs. Dry Season)](04_ndvi_change_hampi/README.md)  
**Objective**: Assess how vegetation coverage changes between seasons and how this affects archaeological visibility.  
**Method**: Compute NDVI for two Sentinel-2 scenes (wet and dry season), calculate pixel-wise difference, and visualize results.  
**Output**: NDVI maps for each season, NDVI difference map, and histograms showing vegetation fluctuation.
