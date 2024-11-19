# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Цикл игры (один кадр на экране)
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    # ----------------------------------------------------------------------------------------------------------------------
    # обрабатываем очередь событий
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    
    # Обновление (Update)
    # ----------------------------------------------------------------------------------------------------------------------
    all_sprites.update()


    # Рендеринг 
    # ----------------------------------------------------------------------------------------------------------------------
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # после отрисовки всего, переворачиваем экран
    # Главное — сделать так, чтобы функция flip() была в конце
    pygame.display.flip()

# Завершение работы
pygame.quit()