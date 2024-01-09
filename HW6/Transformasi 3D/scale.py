import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi skala 3D
def scale_3d(point, sx, sy, sz):
    x, y, z = point
    x_scaled = x * sx
    y_scaled = y * sy
    z_scaled = z * sz
    return x_scaled, y_scaled, z_scaled

# Fungsi untuk menggambar objek awal dan hasil transformasi skala 3D
def update(frame):
    ax.cla()
    
    # Menggambar objek awal
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='b', marker='o', alpha=0.4)

    # Menghitung dan menggambar objek hasil transformasi skala 3D
    scaling_factor = frame  # Ganti nilai ini sesuai kebutuhan
    print(scaling_factor)
    scaled_vertices = [scale_3d(point, scaling_factor, scaling_factor, scaling_factor) for point in vertices]
    print(scaled_vertices)
    ax.scatter3D(np.array(scaled_vertices)[:, 0], np.array(scaled_vertices)[:, 1], np.array(scaled_vertices)[:, 2], c='r', marker='o', alpha=0.6)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(f'Transformasi Skala 3D (Frame {frame})')

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

# Menggunakan FuncAnimation untuk membuat animasi transformasi skala 3D
animation = FuncAnimation(fig, update, frames=np.arange(0.1, 3, 0.1), interval=100)

plt.show()
