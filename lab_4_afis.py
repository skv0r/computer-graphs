import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation

# Вершины тетраэдра
vertices = np.array([
    [1, 1, 1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
])

# Грани тетраэдра
faces = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3]
]

# Функция для вращения вокруг оси Y
def rotate_y(points, angle):
    cos_theta, sin_theta = np.cos(angle), np.sin(angle)
    rotation_matrix = np.array([
        [cos_theta, 0, sin_theta],
        [0, 1, 0],
        [-sin_theta, 0, cos_theta]
    ])
    return np.dot(points, rotation_matrix.T)

# Диметрическая проекция
def dimetric_projection(points):
    projection_matrix = np.array([
        [0.935, 0, 0.354],
        [0, 1, 0],
        [0.354, 0, -0.935]
    ])
    return np.dot(points, projection_matrix.T)

# Настройка графики
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Функция для обновления анимации
def update(num, vertices, faces):
    ax.cla()
    angle = np.radians(num)
    rotated_vertices = rotate_y(vertices, angle)
    projected_vertices = dimetric_projection(rotated_vertices)

    poly3d = [[projected_vertices[vert_id] for vert_id in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', edgecolors='b'))

    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_title("Вращение тетраэдра (Диметрическая проекция)")

# Анимация
ani = animation.FuncAnimation(fig, update, frames=360, fargs=(vertices, faces), interval=50)
plt.show()
