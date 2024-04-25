import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(initial_image, current_image, threshold=0.95):
    # Преобразование изображений в оттенки серого
    initial_gray = cv2.cvtColor(initial_image, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)
    
    # Вычисление коэффициента структурной схожести
    similarity = ssim(initial_gray, current_gray, multichannel=True)
    
    # Сравнение коэффициента с порогом
    if similarity < threshold:
        return True  # Изображения сильно отличаются, возможно, изменился ракурс или освещение
    else:
        return False  # Изображения схожи, ракурс и освещение, вероятно, не изменились

# Пример использования функции
initial_image = cv2.imread('initial_image.jpg')
current_image = cv2.imread('current_image.jpg')

if compare_images(initial_image, current_image):
    print("Ракурс или освещение изменились")
else:
    print("Ракурс и освещение не изменились")
