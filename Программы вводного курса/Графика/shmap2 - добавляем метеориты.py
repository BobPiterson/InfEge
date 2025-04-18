# Игра Shmap - 2 часть - добавлены метеориты

# к предыдущей версии добавлено:
# 1) описание класса метеоритов - случайная координата появления, направление движения и скорость у каждого спрайта, добавление новых
# 2) создаем заданное количество экземпляров класса метеоритов

import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init() # инициализация звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра!")
clock = pygame.time.Clock() # отчет частоты кадров

# Описание класса игрока (управляемый с клавиатуры спрайт)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))   # размер спрайта
        self.image.fill(GREEN)                  # цвет спрайта
        self.rect = self.image.get_rect() # изменение размера спрайта до размера картинки спрайта (если в виде спрайта загружена картинка)
        self.rect.centerx = WIDTH / 2   # определение координаты начального расположения спрайта: середина спрайта по середине окна
        self.rect.bottom = HEIGHT - 10  # определение координаты начального расположения спрайта: нижняя граница спрайта на 10 пикселей выше нижней точки окна
        self.speedx = 0                 # начальная скорость по Х равна 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed() # обработка буфера нажатых клавиш
        if keystate[pygame.K_LEFT]:
            self.speedx = -8                # если нажата стрелка влево, делаем скорость по Х = -8 пикселей за 1 кадр
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8                 # если нажата стрелка вправо, делаем скорость по Х = +8 пикселей за 1 кадр
        self.rect.x += self.speedx          # меняем координату спрайта по Х на скорость по Х
        if self.rect.right > WIDTH:         # проверяем выход спрайта за границы окна
            self.rect.right = WIDTH         # не даем правой границе спрайта уйти за правую границу окна
        if self.rect.left < 0:
            self.rect.left = 0              # не даем левой границе спрайта уйти за левую границу окна

# Описание класса врагов (управляемые алгоритмом спрайты)
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) # задаем начальную координату левого верхнего угла по Х от 0 до ширины окна-ширина спрайта
        self.rect.y = random.randrange(-100, -40)  # задаем начальную координату левого верхнего угла по Y от -100 до -40 (т.е. спрайт рождается за пределами окна)
        self.speedy = random.randrange(4, 8)        # устанавливаем начальную скорость по У в диапазоне от 1 до 8
        self.speedx = random.randrange(-3, 3)       # устанавливаем начальную скорость по Х в диапазоне от -3 до 3
    def update(self):
        if self.rect.right > WIDTH:         # проверяем выход спрайта за границы окна
            self.speedx = -self.speedx      # делаем отскок от правую границу окна
        if self.rect.left < 0:
            self.speedx = -self.speedx      # делаем отскок от левой границы окна

        self.rect.y += self.speedy  # изменяем координату спрайта по вертикали в зависимости от скорости
        self.rect.x += self.speedx  # изменяем координату спрайта по горизонтали в зависимости от скорости
        if self.rect.top > HEIGHT: # задаем условие - пока спрайт не долетит до нижнего края окна, новый спрайт не появится
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(4, 8)

# создаем новый набор для всех спрайтов
all_sprites = pygame.sprite.Group()
# создаем экземпляр класса Player
player = Player()
# добавляем наш экземпляр в набор спрайтов
all_sprites.add(player)

# создаем новый набор спрайтов для врагов:
mobs = pygame.sprite.Group()
# создаем экземпляры классов Враги:
for i in range(10):
    m = Mob()           # создаем в переменной m экземпляр класса
    all_sprites.add(m)  # добавляем экземпляр в набор всех спрайтов
    mobs.add(m)         # добавляем экземпляр в набор для врагов

# Цикл игры
running = True
while running: # пока не закончилась игра
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Обработка очереди событий
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # ESC key pressed
            running = False

    # Обновление спрайтов - вызывает для каждого спрайта из общего набора спрайтов метод update
    all_sprites.update()
    
    # Рендеринг (отрисовка)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки буфера, переворачиваем экран
    pygame.display.flip()

pygame.quit()