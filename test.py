import matplotlib.pyplot as plt
import numpy as np
from xraydb import f0

# # Углы от 0 до 2*pi
# f0()
# theta = np.linspace(0, 1, 1000)
# x = np.sin(theta) / 1.58184
# # Функции атомного рассеяния для элементов Na, Cl, Li, Pb
# na_scattering = f0('Na')
# cl_scattering = f0('Cl', x)
# li_scattering = f0('Li', x)
# pb_scattering = f0('Pb', x)

# # Строим графики
# plt.figure(figsize=(10, 6))

# plt.plot(x , na_scattering, label='Na')
# plt.plot(x , cl_scattering, label='Cl')
# plt.plot(x , li_scattering, label='Li')
# plt.plot(x , pb_scattering, label='Pb')

# plt.title('Atomic Scattering Function')
# plt.xlabel('Theta')
# plt.ylabel('Scattering Intensity')
# plt.legend()
# plt.grid(True)
# plt.show()

import pygame
import sys
import math

pygame.init()

# настройка окна
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")

# цвета
white = (255, 255, 255)
black = (0, 0, 0)

# начальные углы для стрелок
angle_big_arrow = 90
angle_small_arrow = 90

# Главный цикл анимации
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(white)

    # циферблат
    pygame.draw.circle(screen, black, (width // 2, height // 2), 200, 2)

    # большая стрелка
    big_arrow_length = 180
    big_arrow_x = width // 2 + big_arrow_length * math.cos(math.radians(angle_big_arrow))
    big_arrow_y = height // 2 - big_arrow_length * math.sin(math.radians(angle_big_arrow))
    pygame.draw.line(screen, black, (width // 2, height // 2), (big_arrow_x, big_arrow_y), 4)

    #малая стрелка
    small_arrow_length = 120
    small_arrow_x = width // 2 + small_arrow_length * math.cos(math.radians(angle_small_arrow))
    small_arrow_y = height // 2 - small_arrow_length * math.sin(math.radians(angle_small_arrow))
    pygame.draw.line(screen, black, (width // 2, height // 2), (small_arrow_x, small_arrow_y), 2)

    # Обновление углов (3/12 = 0.25)
    speed = 1
    angle_big_arrow -= speed
    angle_small_arrow -= speed / 12

    # Обновление экрана
    pygame.display.flip()

    # Ограничение скорости анимации
    clock.tick(60)  