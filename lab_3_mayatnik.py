import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation

# Параметры маятника
L = 5  # Длина маятника
angle_max = np.pi / 6  # Максимальный угол отклонения (30 градусов)
num_frames = 100  # Количество кадров на одно качание

# Функция для создания правильного шестиугольника
def create_hexagon(center, size):
    angles = np.linspace(0, 2 * np.pi, 7)
    x_hexagon = center[0] + size * np.cos(angles)
    y_hexagon = center[1] + size * np.sin(angles)
    return x_hexagon, y_hexagon

# Функция для обновления анимации
def update(frame):
    angle = angle_max * np.sin(2 * np.pi * frame / num_frames)
    x = L * np.sin(angle)
    y = -L * np.cos(angle)
    hexagon.set_xy(np.column_stack(create_hexagon((x, y), 0.5)))
    rod.set_data([0, x], [0, y])
    return hexagon, rod

# Создание фигуры и осей
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-L - 1, L + 1)  # Расширяем зону видимости по X
ax.set_ylim(-L - 1, 1)  # Расширяем зону видимости по Y
ax.axis('off')

# Добавление дуги, которая показывает область движения маятника
arc = patches.Arc((0, 0), 2*L, 2*L, angle=0, theta1=-angle_max*180/np.pi, theta2=angle_max*180/np.pi, color='gray', linestyle='--')
ax.add_patch(arc)

# Рисование маятника
hexagon = patches.Polygon(np.column_stack(create_hexagon((0, -L), 0.5)), closed=True, edgecolor='black', facecolor='lightblue')
ax.add_patch(hexagon)
rod, = ax.plot([0, 0], [0, -L], color='black')

# Анимация
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True, repeat=True)

# Отображение
plt.show()
