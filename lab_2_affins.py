import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation

# Определяем вершины октаэдра
vertices = np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
])

# Грани октаэдра (каждая грань — это треугольник)
faces = [
    [0, 2, 4],
    [0, 2, 5],
    [0, 3, 4],
    [0, 3, 5],
    [1, 2, 4],
    [1, 2, 5],
    [1, 3, 4],
    [1, 3, 5]
]

# Функция для поворота октаэдра вокруг произвольной оси
def rotate(points, angle, axis):
    axis = axis / np.linalg.norm(axis)  # Нормализация оси
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    u_x, u_y, u_z = axis

    # Матрица вращения
    rotation_matrix = np.array([
        [cos_theta + u_x**2 * (1 - cos_theta), u_x * u_y * (1 - cos_theta) - u_z * sin_theta, u_x * u_z * (1 - cos_theta) + u_y * sin_theta],
        [u_y * u_x * (1 - cos_theta) + u_z * sin_theta, cos_theta + u_y**2 * (1 - cos_theta), u_y * u_z * (1 - cos_theta) - u_x * sin_theta],
        [u_z * u_x * (1 - cos_theta) - u_y * sin_theta, u_z * u_y * (1 - cos_theta) + u_x * sin_theta, cos_theta + u_z**2 * (1 - cos_theta)]
    ])

    return np.dot(points, rotation_matrix.T)

# Настройка графики
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Определяем ось вращения (например, [1, 1, 0])
axis_of_rotation = np.array([1, 1, 0])

# Функция для обновления анимации
def update(num, vertices, faces, axis):
    ax.cla()  # Очистка предыдущего кадра
    angle = np.radians(num)  # Угол в радианах
    rotated_vertices = rotate(vertices, angle, axis)

    # Отрисовка октаэдра
    poly3d = [[rotated_vertices[face] for face in f] for f in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))

    # Настройки осей
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_title("Вращение октаэдра")

# Анимация
ani = animation.FuncAnimation(fig, update, frames=360, fargs=(vertices, faces, axis_of_rotation), interval=50)

plt.show()
