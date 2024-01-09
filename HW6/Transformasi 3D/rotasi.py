import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Fungsi untuk melakukan transformasi rotasi 3D
def rotate_3d(point, angle_x, angle_y, angle_z):
    x, y, z = point

    # Rotasi terhadap sumbu X
    x_rotated = x
    y_rotated = y * np.cos(angle_x) - z * np.sin(angle_x)
    z_rotated = y * np.sin(angle_x) + z * np.cos(angle_x)

    # Rotasi terhadap sumbu Y
    x_rotated = x_rotated * np.cos(angle_y) + z_rotated * np.sin(angle_y)
    y_rotated = y_rotated
    z_rotated = -x_rotated * np.sin(angle_y) + z_rotated * np.cos(angle_y)

    # Rotasi terhadap sumbu Z
    x_rotated = x_rotated * np.cos(angle_z) - y_rotated * np.sin(angle_z)
    y_rotated = x_rotated * np.sin(angle_z) + y_rotated * np.cos(angle_z)
    z_rotated = z_rotated

    return x_rotated, y_rotated, z_rotated

# Fungsi untuk menggambar objek awal dan hasil rotasi 3D
def update(frame):
    ax.cla()

    # Menggambar objek awal
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='b', marker='o', alpha=0.4)

    # Menghitung dan menggambar objek hasil rotasi 3D
    angle_x, angle_y, angle_z = frame, frame, frame  # Ganti nilai ini sesuai kebutuhan
    rotated_vertices = [rotate_3d(point, angle_x, angle_y, angle_z) for point in vertices]
    ax.scatter3D(np.array(rotated_vertices)[:, 0], np.array(rotated_vertices)[:, 1], np.array(rotated_vertices)[:, 2], c='r', marker='o', alpha=0.6)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(f'Rotasi 3D (Frame {frame})')

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
# Menggunakan FuncAniation untuk membuat animasi rotasi 3D
animation = FuncAnimation(fig, update, frames=np.arange(0, 2 * np.pi, 0.1), interval=100)

plt.show()
