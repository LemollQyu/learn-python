import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import os

MAX_SIZE = (800, 800)  # Maksimum dimensi gambar

# ubah rgb to hexa
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def get_dominant_color(image_path, n_clusters=3):
    # Baca gambar dan konversi ke format RGB
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)
    
    # Reshape data menjadi array 2D (jumlah piksel x 3 warna RGB)
    pixels = data.reshape((-1, 3))

    # Terapkan K-means clustering untuk menemukan cluster warna
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(pixels)

    # Ambil warna dari cluster yang paling dominan (dengan jumlah piksel terbanyak)
    unique, counts = np.unique(kmeans.labels_, return_counts=True)
    dominant_cluster = unique[np.argmax(counts)]  # Cluster dengan jumlah piksel terbanyak
    dominant_color_rgb = kmeans.cluster_centers_[dominant_cluster].astype(int)
    
    # Konversi RGB ke Hex
    dominant_color_hex = rgb_to_hex(dominant_color_rgb)
    
    return dominant_color_hex  # Mengembalikan warna dominan dalam format hex

# tutup

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def prepare_image(path):
    image = Image.open(path).convert("RGB")
    image.thumbnail(MAX_SIZE)  # Resize (preserve aspect ratio)
    return image

def calculate_color_distance(color1, color2):
    # Menghitung jarak Euclidean antara dua warna RGB
    return np.linalg.norm(np.array(color1) - np.array(color2))

def create_color_mask(data, target_rgb, tolerance):
    # Buat mask berdasarkan perhitungan jarak Euclidean antar piksel dan warna target
    return np.apply_along_axis(lambda px: calculate_color_distance(px, target_rgb) < tolerance, 2, data)

def replace_color_with_hex_list(image_path, target_hex, hex_file_path, result_dir, tolerance=30):
    image = prepare_image(image_path)
    data = np.array(image)
    target_rgb = hex_to_rgb(target_hex)

    # Gunakan mask untuk mendeteksi warna yang mirip dengan warna target
    mask = create_color_mask(data, target_rgb, tolerance)

    # Load daftar warna hex
    with open(hex_file_path, 'r') as file:
        hex_colors = [line.strip() for line in file.readlines() if line.strip()]

    result_paths = []

    for i, hex_code in enumerate(hex_colors):
        rgb = hex_to_rgb(hex_code)
        new_data = data.copy()
        new_data[mask] = rgb
        result_img = Image.fromarray(new_data)
        result_path = os.path.join(result_dir, f"result_{i}.png")
        result_img.save(result_path)
        result_paths.append(result_path)

    return result_paths

def replace_color_with_texture(image_path, texture_path, target_hex, result_dir, tolerance=30):
    image = prepare_image(image_path)
    texture = prepare_image(texture_path)
    texture = texture.resize(image.size)

    data = np.array(image)
    texture_data = np.array(texture)

    target_rgb = hex_to_rgb(target_hex)

    # Gunakan mask untuk mendeteksi warna yang mirip dengan warna target
    mask = create_color_mask(data, target_rgb, tolerance)

    new_data = data.copy()
    new_data[mask] = texture_data[mask]

    result_img = Image.fromarray(new_data)
    result_path = os.path.join(result_dir, "result_texture.png")
    result_img.save(result_path)
    return result_path
