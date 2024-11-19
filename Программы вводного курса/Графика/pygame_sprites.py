# Pygame шаблон - скелет для нового проекта Pygame
# https://pythonru.com/uroki/biblioteka-pygame-chast-3-bolshe-o-sprajtah
# https://waksoft.susu.ru/2019/04/24/pygame-shpargalka-dlja-ispolzovanija/
import pygame
import random
import os
from pygame.locals import *


WIDTH = 1024  # ширина игрового окна
HEIGHT = 640 # высота игрового окна
FPS = 60 # частота кадров в секунду

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


# настройка папки ассетов
# С помощью команды os.path можно позволить ПК самостоятельно определять правильный путь
# команда os.path.dirname указывает путь к папке, в которой сохранен код игры
game_folder = os.path.dirname(__file__)
# картинки будем брать из папки с кодом, в которой создана папка img, а уже в ней картинки
img_folder = os.path.join(game_folder, 'img')
# Изображение загружается с помощью pygame.image.load(), а convert() ускорит прорисовку в Pygame, 
# конвертируя изображение в тот формат, который будет быстрее появляться на экране.
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()


# ---------------------------------- спрайты -------------------------------------
# создаем класс
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        print('Размер спрайта до загрузки картинки:', self.rect.height, 'x', self.rect.width)
        self.image = player_img
        # set_colorkey() говорит Pygame игнорировать любые пиксели указанного цвета
        self.image.set_colorkey(BLACK)
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        print('Размер спрайта после загрузки картинки:', self.rect.height, 'x', self.rect.width)
        self.rect.center = (WIDTH / 2, HEIGHT / 2) # размещаем центр спрайта (rect.center) по центру окна

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
        self.rect.y += random.randrange (-5 , 5)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
        if self.rect.bottom < 0:
            self.rect.bottom = HEIGHT


# --------------------------------------------------------------------------------

# создаем экземпляр класса Player
player = Player()
# добавляем наш экземпляр в набор спрайтов
all_sprites.add(player)


# Цикл игры (один кадр на экране) ========================================================================================
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
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            # ESC key pressed
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE:
            # Space key pressed
            player.rect.y -= 150

    
    # Обновление (Update)
    # ----------------------------------------------------------------------------------------------------------------------
    all_sprites.update()


    # Рендеринг 
    # ----------------------------------------------------------------------------------------------------------------------
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # после отрисовки всего, переворачиваем экран
    # Главное — сделать так, чтобы функция flip() была в конце
    pygame.display.flip()

# Завершение работы
pygame.quit()