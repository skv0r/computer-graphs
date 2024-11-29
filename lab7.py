import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(path):
    """Загрузка изображения и преобразование в массив NumPy."""
    image = Image.open(path).convert("RGB")
    return np.array(image)

def rotate_image(image, angle):
    """Поворот изображения с использованием Pillow."""
    pil_image = Image.fromarray(image)
    rotated_image = pil_image.rotate(angle, resample=Image.BICUBIC, expand=True)
    return np.array(rotated_image)

def shift_image(image, row_shift, col_shift):
    """Сдвиг изображения на заданное количество строк и столбцов."""
    return np.roll(image, row_shift, axis=0), np.roll(image, col_shift, axis=1)

def owen_makedon_rotation(image, angle):
    """Применение алгоритма Оуэна и Македона для поворота с сдвигами."""
    # Поворот изображения с использованием Pillow
    rotated_image = rotate_image(image, angle)
    
    # Получение высоты и ширины нового изображения
    height, width, _ = rotated_image.shape

    # Применяем сдвиг строк и столбцов
    rotated_image, shifted_image = shift_image(rotated_image, height // 4, width // 4)
    rotated_image, shifted_image = shift_image(shifted_image, -height // 4, -width // 4)
    
    return shifted_image

def main():
    # Путь к изображению
    image_path = "35126.jpg"  # Укажите путь к вашему изображению
    original_image = load_image(image_path)

    # Углы поворота
    base_angle = 2  # Сумма цифр порядкового номера
    angles = [base_angle, base_angle * 3, base_angle * 5]

    # Преобразования
    results = [original_image]
    for angle in angles:
        transformed_image = owen_makedon_rotation(original_image, angle)
        results.append(transformed_image)

    # Проверка артефактов
    # Если артефакты отсутствуют, используем другие углы
    # Множители 0.3 и 0.5
    alt_angles = [base_angle, base_angle * 0.3, base_angle * 0.5]
    alt_results = []
    for angle in alt_angles:
        transformed_image = owen_makedon_rotation(original_image, angle)
        alt_results.append(transformed_image)

    # Визуализация
    fig, axes = plt.subplots(2, len(results), figsize=(20, 10))
    
    # Графики для исходных углов
    for i, (ax, img, angle) in enumerate(zip(axes[0], results, ["Оригинал"] + angles)):
        ax.imshow(img)
        ax.set_title(f"{angle}°" if i > 0 else "Оригинал")
        ax.axis("off")
    
    # Графики для альтернативных углов
    for i, (ax, img, angle) in enumerate(zip(axes[1], alt_results, alt_angles)):
        ax.imshow(img)
        ax.set_title(f"{angle:.1f}°")
        ax.axis("off")
    
    # Убираем пустую форму
    for ax in axes[1][len(alt_results):]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
