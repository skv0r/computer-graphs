import numpy as np
import matplotlib.pyplot as plt

# Размер изображения
width, height = 800, 800

# Границы отображения
x_min, x_max = -2.5, 1.5
y_min, y_max = -2.0, 2.0
    
# Максимальное количество итераций
max_iter = 256

# Определение цветовой палитры (индексированной)
palette = np.array([
    [66, 30, 15], [25, 7, 26], [9, 1, 47], [4, 4, 73], [0, 7, 100], [12, 44, 138], 
    [24, 82, 177], [57, 125, 209], [134, 181, 229], [211, 236, 248], [241, 233, 191],
    [248, 201, 95], [255, 170, 0], [204, 128, 0], [153, 87, 0], [106, 52, 3]
])

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Создание изображения
image = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        # Преобразование координат пикселя в комплексное число
        real = x_min + (x / width) * (x_max - x_min)
        imag = y_min + (y / height) * (y_max - y_min)
        c = complex(real, imag)
        
        # Вычисление фрактала
        m = mandelbrot(c, max_iter)
        
        # Определение цвета
        color = palette[m % len(palette)] if m < max_iter else [0, 0, 0]
        image[y, x] = color

# Отображение изображения
plt.imshow(image)
plt.axis('off')  # Убираем оси
plt.show()
