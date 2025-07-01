# Viewshed Analysis – Hampi

This project explores the visual dominance of key monuments in the Hampi heritage landscape using GIS-based viewshed analysis. By simulating what is visible from two major elevated locations—**Virupaksha Temple** and **Hemakuta Hill**—this analysis highlights how topography and monumentality intersect to shape sacred geography and spatial planning.

---

## 🎯 Objective

To model and compare the areas visible from:
- **Virupaksha Temple** (~50 m high)
- **Hemakuta Hill** (~60m high)

This helps assess:
- How these monuments command the surrounding landscape
- Potential visual relationships between sacred, residential, and hydrological features

---

## 🛠️ Methodology

### 1. **Data Preparation**
- Clipped a DEM of Hampi to the area of interest using `hampi_boundary.geojson`
- Created observer locations (`viewpoints.geojson`) for:
  - Virupaksha Temple (15.33513, 76.45868)
  - Hemakuta Hill (15.33330, 76.45800)

### 2. **Viewshed Generation**
- Used **GRASS GIS `r.viewshed`** plugin in QGIS
- Parameters:
  - **Observer height**: 50 m (to simulate top of monument)
  - **Target height**: 0 m
  - **Max distance**: 5000 m

### 3. **Output Layers**
- `viewshed_virupaksha.tif`
- `viewshed_hemakuta.tif`
- Styled and exported for comparison using QGIS Print Layout

---

## 🗺️ Results

### 🔹 Virupaksha Temple Viewshed

![Virupaksha Viewshed](results/viewshed_virupaksha.png)

---

### 🔸 Hemakuta Hill Viewshed


![Hemakuta Viewshed](results/viewshed_hemakuta.png)

---

## 🏛️ Archaeological Relevance

- Demonstrates the role of **elevation and monumentality** in sacred landscape design.
- Supports interpretation of **ceremonial pathways**, **visual communication**, and **hierarchical structuring** in Vijayanagara urbanism.
- Shows how **GIS tools can reveal non-obvious spatial logic** in archaeological landscapes.

---

## 🧩 Tools Used

- QGIS 3.40+
- GRASS GIS Plugin (`r.viewshed`)
- EPSG:4326 CRS
- SRTM-derived DEM clipped to Hampi AOI

---
