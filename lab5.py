import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Задаем интервал и функцию
x = np.linspace(-4, 4, 6)  # 6 опорных точки
y = np.tanh(x)  # Значения функции в опорных точках

# Интерполяция CubicSpline с 'natural' граничными условиями
cs = CubicSpline(x, y, bc_type='natural')

# Подготовка данных для построения кривой
x_fine = np.linspace(-4, 4, 100)  # Больше точек для плавности кривой
y_fine = np.tanh(x_fine)  # Оригинальная функция
y_interp = cs(x_fine)  # Интерполированная кривая

# Вычисление ошибки восстановления
error = np.abs(y_fine - y_interp)
mean_error = np.mean(error)

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_fine, label="Оригинальная функция tanh(x)", color='blue')
plt.plot(x_fine, y_interp, label="Интерполяция CubicSpline", linestyle='--', color='orange')
plt.scatter(x, y, color='red', label="Опорные точки")
plt.title("Интерполяционная кривая для функции tanh(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

# Вывод значения ошибки
plt.figtext(0.15, 0.02, f"Средняя ошибка восстановления: {mean_error:.4f}", fontsize=10)
plt.show()
