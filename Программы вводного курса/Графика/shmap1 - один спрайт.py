# Игра Shmup - 1 часть
# Cпрайт игрока и управление стрелками для его перемещения
# В программу входит:
# 1) инициализация класса pygame
# 2) создание игрового окна
# 3) Описание класса спрайта игрока с начальным расположением спрайта в окне и изменением его координат при вызове свойства update
# 4) создаем экземпляр спрайта игрока и добавляем его в список спрайтов игры
# 5) Начинаем бесконечный игровой цикл. Во время работы цикла:
#                                       - проверяем нажатие клавиш управления и выхода из игры
#                                       - вызываем свойства update у всех спрайтов
#                                       - отрисовываем все спрайты в буфер экрана
#                                       - меняем местами экран и буфер
import pygame

WIDTH = 480
HEIGHT = 600
FPS = 60

# Задаем разные цвета, на будущее
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()       # инициализация игры
pygame.mixer.init() # инициализация звука
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создание игрового окна
pygame.display.set_caption("Shmup!") # заголовок окна
clock = pygame.time.Clock()         # отчет частоты кадров

# Описание класса Player (управляемый с клавиатуры спрайт)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() # установка размера спрайта до размера картинки спрайта
        self.rect.centerx = WIDTH / 2   # установка начального расположения спрайта на игровом поле: середина спрайта по середине окна
        self.rect.bottom = HEIGHT - 10  # нижняя граница спрайта на 10 пикселей выше нижней точки окна
        self.speedx = 0                 # начальная скорость по Х равна 0

    def update(self): # функция вызывается из цикла игры
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx  # изменение координат спрайта в зависимости от переменной speedx
        if self.rect.right > WIDTH: # вовремя остановиться у края
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# создаем новый набор для всех спрайтов игры
all_sprites = pygame.sprite.Group()
# создаем один экземпляр класса Player
player = Player()
# добавляем наш экземпляр в общий набор спрайтов
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # ESC key pressed
            running = False

    # Обновление состояния игры, у всех экземпляров вызвает описанную в классе функцию update()
    all_sprites.update()
    
    # Рендеринг
    screen.fill(BLACK)
    # отрисовать все спрайты списка в экранный буфер
    all_sprites.draw(screen)
    # После отрисовки буфера, меняем местами экран и буфер
    pygame.display.flip()

pygame.quit()