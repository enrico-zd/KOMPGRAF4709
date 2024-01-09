import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi skala
def scale(point, sx, sy):
    x, y = point
    x_scaled = x * sx
    y_scaled = y * sy
    return x_scaled, y_scaled

# Fungsi untuk menggambar objek awal dan hasil transformasi skala
def update(frame):
    ax.cla()
    
    # Menggambar objek awal
    polygon_original = Polygon(vertices, closed=True, edgecolor='b', alpha=0.4)
    ax.add_patch(polygon_original)

    # Menghitung dan menggambar objek hasil transformasi skala
    scaling_factor = frame  # Ganti nilai ini sesuai kebutuhan
    print(scaling_factor)
    scaled_vertices = [scale(point, scaling_factor, scaling_factor) for point in vertices]
    print(scaled_vertices)
    polygon_scaled = Polygon(scaled_vertices, closed=True, edgecolor='r', alpha=0.6)
    ax.add_patch(polygon_scaled)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Transformasi Skala {frame}')

# Definisi objek awal (segitiga)
vertices = np.array([[0, 0], [3, 0], [3, 2], [0, 2]])

# Inisialisasi plot
fig, ax = plt.subplots()

# Menggunakan FuncAnimation untuk membuat animasi transformasi skala
animation = FuncAnimation(fig, update, frames=np.arange(0.1, 3, 0.1), interval=100)

plt.show()
