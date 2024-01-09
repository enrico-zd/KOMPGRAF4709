import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi translasi 3D
def translate_3d(point, tx, ty, tz):
    x, y, z = point
    x_translated = x + tx
    y_translated = y + ty
    z_translated = z + tz
    return x_translated, y_translated, z_translated

# Fungsi untuk menggambar objek awal dan hasil translasi 3D
def update(frame):
    ax.cla()
    
    # Menggambar objek awal
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='b', marker='o', alpha=0.4)

    # Menghitung dan menggambar objek hasil translasi 3D
    translation_vector = [frame, frame, frame]  # Ganti nilai ini sesuai kebutuhan
    translated_vertices = [translate_3d(point, *translation_vector) for point in vertices]
    ax.scatter3D(np.array(translated_vertices)[:, 0], np.array(translated_vertices)[:, 1], np.array(translated_vertices)[:, 2], c='r', marker='o', alpha=0.6)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(f'Translasi 3D (Frame {frame})')

# Definisi objek awal (kubus)
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Inisialisasi plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Menggunakan FuncAnimation untuk membuat animasi translasi 3D
animation = FuncAnimation(fig, update, frames=np.arange(0, 6, 0.1), interval=100)

plt.show()
