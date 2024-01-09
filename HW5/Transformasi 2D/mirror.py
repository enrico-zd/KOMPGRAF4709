import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi mirroring
def mirror(point, axis):
    x, y = point
    if axis == 'x':
        return x, -y
    elif axis == 'y':
        return -x, y
    else:
        return x, y

# Fungsi untuk menggambar objek awal dan hasil transformasi mirroring
def update(frame):
    ax.cla()
    
    # Menggambar objek awal
    polygon_original = Polygon(vertices, closed=True, edgecolor='b', alpha=0.4)
    ax.add_patch(polygon_original)

    # Menghitung dan menggambar objek hasil transformasi mirroring
    axis = 'y'  # Ganti nilai ini dengan 'x' atau 'y' sesuai kebutuhan
    mirrored_vertices = [mirror(point, axis) for point in vertices]
    polygon_mirrored = Polygon(mirrored_vertices, closed=True, edgecolor='r', alpha=0.6)
    ax.add_patch(polygon_mirrored)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Transformasi Pemantulan ({axis}-axis)')

# Definisi objek awal (segitiga)
vertices = np.array([[-2, 0], [1, 0], [3, 2], [0, 2]])

# Inisialisasi plot
fig, ax = plt.subplots()

# Menggunakan FuncAnimation untuk membuat animasi transformasi mirroring
animation = FuncAnimation(fig, update, frames=np.arange(0, 2, 1), interval=100)

plt.show()
