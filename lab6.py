import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
import tkinter as tk

# Функции для гармонических колебаний и построения кривой Безье
def harmonic_wave(x):
    return np.sin(x)

def bezier_curve(points, t_values):
    n = len(points) - 1
    curve_points = np.zeros((len(t_values), 2))
    for i, t in enumerate(t_values):
        curve_points[i] = sum(comb(n, k) * (t**k) * ((1 - t)**(n - k)) * points[k] for k in range(n + 1))
    return curve_points[:, 0], curve_points[:, 1]

# Функция для построения графика с определенным количеством точек
def plot_bezier_curve(n_points):
    x = np.linspace(0, 2 * np.pi, 100)
    y = harmonic_wave(x)
    plt.plot(x, y, label='Гармоническое колебание')

    t_points = np.linspace(0, 2 * np.pi, n_points)
    control_points = np.array([[t, harmonic_wave(t)] for t in t_points])

    t_values = np.linspace(0, 1, 100)
    bezier_x, bezier_y = bezier_curve(control_points, t_values)
    plt.plot(bezier_x, bezier_y, '--', label=f'Кривая Безье по {n_points} точкам')

    original_y = harmonic_wave(bezier_x)
    error = np.mean(np.abs(original_y - bezier_y))

    plt.scatter(control_points[:, 0], control_points[:, 1], color='red', label='Опорные точки')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Кривая Безье для гармонических колебаний\nСредняя ошибка: {error:.4f}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Основной интерфейс с кнопками
def main():
    base_points = 6
    root = tk.Tk()
    root.title("Построение кривой Безье")
    root.configure(bg='#333333')  # Темно-серый фон

    # Установим цвет текста метки на белый и немного увеличим размер шрифта
    label = tk.Label(root, text="Выберите количество опорных точек для кривой Безье", 
                     bg='#333333', fg='#FFFFFF', font=("Arial", 14, "bold"))
    label.pack(pady=10)

    # Установим кнопкам яркий цвет фона и черный текст для улучшенной видимости
    btn_base = tk.Button(root, text=f"Построить с {base_points} точками", 
                         command=lambda: plot_bezier_curve(base_points),
                         bg='#00FF00', fg='#000000', font=("Arial", 12, "bold"))  # Ярко-зеленая кнопка с черным текстом
    btn_base.pack(pady=5)

    btn_less = tk.Button(root, text=f"Построить с {base_points - 2} точками", 
                         command=lambda: plot_bezier_curve(base_points - 2),
                         bg='#FF0000', fg='#000000', font=("Arial", 12, "bold"))  # Ярко-красная кнопка с черным текстом
    btn_less.pack(pady=5)

    btn_more = tk.Button(root, text=f"Построить с {base_points + 2} точками", 
                         command=lambda: plot_bezier_curve(base_points + 2),
                         bg='#0000FF', fg='#000000', font=("Arial", 12, "bold"))  # Ярко-синяя кнопка с черным текстом
    btn_more.pack(pady=5)

    root.mainloop()

# Запуск программы
if __name__ == "__main__":
    main()
