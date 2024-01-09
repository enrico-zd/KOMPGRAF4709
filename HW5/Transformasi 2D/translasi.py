import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi translasi
def translate(point, tx, ty):
    x, y = point
    x_translated = x + tx
    y_translated = y + ty
    return x_translated, y_translated

# Fungsi untuk menggambar objek awal dan hasil translasi
def update(frame):
    ax.cla()
    
    # Menggambar objek awal
    polygon_original = Polygon(vertices, closed=True, edgecolor='b', alpha=0.4)
    ax.add_patch(polygon_original)

    # Menghitung dan menggambar objek hasil translasi
    translation_vector = [frame, frame]  # Ganti nilai ini sesuai kebutuhan
    translated_vertices = [translate(point, *translation_vector) for point in vertices]
    polygon_translated = Polygon(translated_vertices, closed=True, edgecolor='r', alpha=0.6)
    ax.add_patch(polygon_translated)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Translasi {frame} Satuan')

# Definisi objek awal (segitiga)
vertices = np.array([[0, 0], [3, 0], [3, 2], [0, 2]])

# Inisialisasi plot
fig, ax = plt.subplots()

# Menggunakan FuncAnimation untuk membuat animasi translasi
animation = FuncAnimation(fig, update, frames=np.arange(0, 6, 0.1), interval=100)

plt.show()