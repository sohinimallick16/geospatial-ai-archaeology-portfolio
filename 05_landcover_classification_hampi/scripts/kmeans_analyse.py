import rasterio
import numpy as np
import matplotlib.pyplot as plt

def plot_class_distribution(classified_path, output_path):
    with rasterio.open(classified_path) as src:
        classified = src.read(1)

    unique, counts = np.unique(classified[classified != 255], return_counts=True)

    plt.figure(figsize=(8, 6))
    plt.bar(unique, counts, color='skyblue')
    plt.xlabel("Land Cover Class")
    plt.ylabel("Pixel Count")
    plt.title("Land Cover Class Distribution")
    plt.xticks(unique)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Histogram saved to {output_path}")
