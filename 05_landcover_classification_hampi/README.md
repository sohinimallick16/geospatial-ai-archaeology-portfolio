# Land Cover Classification Using K-means Clustering – Archaeological Site of Hampi, India

This project performs unsupervised land cover classification over the Hampi Group of Monuments using **Sentinel-2 multispectral imagery** and **k-means clustering**. The goal is to classify terrain types such as vegetation, rock, habitation, and water — offering insights into site layout, terrain accessibility, and preservation environments.

---

## 🏛️ Introduction

Land cover classification using satellite imagery provides archaeologists with a scalable way to map and monitor landscape zones around ancient sites. This is especially useful in sites like **Hampi**, where the mix of vegetation, exposed bedrock, habitation, and monuments makes landscape reading complex.

This project uses **unsupervised clustering** to group land cover into 5 classes, supporting tasks like:

- Identifying **archaeological zones** (temples, habitation)
- Mapping **environmental exposure** (bare soil, scrub)
- Assessing **preservation risks** (vegetation encroachment, erosion)
- Building baselines for **multi-seasonal comparison**

---

## 📍 Study Area

- **Location**: Hampi, Karnataka, India
- **Coordinates**: approx. 15.3350° N, 76.4619° E
- **AOI**: Manually drawn polygon around core monument zone and Tungabhadra river valley

---

## 🎯 Objective

To apply **unsupervised k-means clustering** to selected Sentinel-2 bands in order to classify the Hampi landscape into 5 land cover types — providing a foundational environmental map for archaeological interpretation.

---

## 🛰️ Data Used

| Source           | Description                                    |
|------------------|------------------------------------------------|
| Sentinel-2 (L2A) | Bands 2, 3, 4, 8 – 10m resolution              |
| GeoJSON AOI      | Custom boundary polygon for the Hampi region  |

- **Acquisition date**: April 2024 (early dry season)

---

## 🛠️ Tools and Libraries

- QGIS (visual interpretation, band stacking)
- Python 3.8+
  - `rasterio`, `numpy`, `matplotlib`, `sklearn` (k-means)

---

## 🔄 Workflow

1. Download Sentinel-2 bands (B2, B3, B4, B8) from [EO Browser](https://apps.sentinel-hub.com/eo-browser/)
2. Clip bands to AOI using QGIS
3. Stack selected bands into a single multi-band image
4. K-means clustering to group pixels into 5 classes
5. Visualise and interpret the classes using GIS and the histograms

---

## 🧩 Scripts Overview

| Script | Description |
|--------|-------------|
| `band_stacking.py` | Stacks selected Sentinel-2 bands (e.g., Blue, Green, Red, NIR) into a multi-band raster for classification. |
| `kmeans_classifier.py` | Applies k-means clustering on stacked bands and saves the classification raster |
| `kmeans_analyse.py` | Visualizes the classified output and generates a color-coded legend |
| `paths_to_data_results.py` | Manages consistent paths to all data and result files |
| `band_stack.ipynb` | Jupyter notebook to load, stack, and export band rasters for use in unsupervised classification. |
| `kmeans_classify.ipynb` | Notebook to preprocess bands and run classification |
| `kmeans_analyse.ipynb` | Notebook to generate histograms and perform visual interpretation |

---

## 🖼️ Outputs

| Output File | Description |
|-------------|-------------|
| `sentinel_stack.tif` | Combined spectral image used as input |
| `land_cover_kmeans.tif` | Classified raster with 5 classes (0–4) |
| `landcover_classification.png` | Colorized classification map |
| `kmeans_class_distribution.png` | Histogram showing pixel distribution per class |

---

## 📈 Analysis & Interpretation

A full breakdown of the classification accuracy, limitations, and archaeological implications is available in the [Analysis Report](analysis.md).

---

## Conclusion

Classifying land cover from satellite imagery allows for:

- Targeting **field surveys** toward underdocumented terrain types
- Understanding **settlement placement** in relation to water or rocky features
- Monitoring **encroachment or vegetation change** near sensitive monuments
- Laying groundwork for **seasonal comparison** and **supervised learning** projects

Even with limitations, unsupervised classification offers a fast and cost-effective overview of heritage landscapes.

