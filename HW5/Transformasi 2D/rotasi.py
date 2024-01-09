import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi rotasi
def rotate(point, angle):
    x, y = point
    x_rotated = x * np.cos(angle) - y * np.sin(angle)
    y_rotated = x * np.sin(angle) + y * np.cos(angle)
    return x_rotated, y_rotated

# Fungsi untuk menggambar objek awal dan hasil rotasi
def update(frame):
    ax.cla()
    
    # Menggambar objek awal
    polygon_original = Polygon(vertices, closed=True, edgecolor='b', alpha=0.4)
    ax.add_patch(polygon_original)

    # Menghitung dan menggambar objek hasil rotasi
    angle = np.radians(frame)
    print(angle)
    rotated_vertices = [rotate(point, angle) for point in vertices]
    polygon_rotated = Polygon(rotated_vertices, closed=True, edgecolor='r', alpha=0.6)
    ax.add_patch(polygon_rotated)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Rotasi Sudut {frame} Derajat')

# Definisi objek awal (segitiga)
vertices = np.array([[0, 0], [3, 0], [3, 2], [0, 2]])

# Inisialisasi plot
fig, ax = plt.subplots()

# Menggunakan FuncAnimation untuk membuat animasi rotasi
animation = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=100)

plt.show()