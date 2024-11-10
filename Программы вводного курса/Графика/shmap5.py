  # Игра Shmup - 1 часть
# Cпрайт игрока и управление
import pygame
import random
from os import path # для определения пути к файлу в любой операционной системе
# в переменную сохраняется правильный путь к папке относительно файла с кодом игры
img_dir = path.join(path.dirname(__file__), 'img') # в кавычках указывается папка с картинками
print(img_dir)
# размеры игрового окна
WIDTH = 800
HEIGHT = 480
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

# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, 'starfield2.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "H-09.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "rotationY1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laser19.png")).convert()

# Описание класса игрока (управляемый с клавиатуры спрайт)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img 
        self.image = pygame.transform.scale(player_img, (50, 38)) # уменьшаем размер картинки до заданного
        self.image.set_colorkey(BLACK) # убрать черный прямоугольник вокруг спрайта 
        # self.image = pygame.Surface((50, 90))   # размер спрайта 
        #self.image.fill(GREEN)                  # цвет спрайта
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
    # Метод для выстрела игрока
    def shoot(self):
        # Создаем экземпляр класса Bullet и передаем в него координаты спрайта игрока
        bullet = Bullet(self.rect.centerx, self.rect.top)
        # добавляем экземпляр в общий набор спрайтов 
        all_sprites.add(bullet)
        # добавляем экземпляр в набор пуль
        bullets.add(bullet)

# Описание класса врагов (управляемые алгоритмом спрайты)
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img 
        self.image = pygame.transform.scale(meteor_img, (50, 50)) # уменьшаем размер картинки до заданного
        self.image.set_colorkey(BLACK) # убрать черный прямоугольник вокруг спрайта 

        #self.image = pygame.Surface((30, 40))
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) # задаем начальную координату левого верхнего угла по Х от 0 до ширины окна-ширина спрайта
        self.rect.y = random.randrange(-1000, -40)  # задаем начальную координату левого верхнего угла по Y от -100 до -40 (т.е. спрайт рождается за пределами окна)
        self.speedy = random.randrange(4, 8)        # устанавливаем начальную скорость по У в диапазоне от 4 до 8
        self.speedx = random.randrange(-3, 3)       # устанавливаем начальную скорость по Х в диапазоне от -3 до 3
    def update(self):
        if self.rect.right > WIDTH:         # проверяем выход спрайта за границы окна
            self.speedx = -self.speedx      # делаем отскок от правой границы окна
        if self.rect.left < 0:
            self.speedx = -self.speedx      # делаем отскок от левой границы окна

        self.rect.y += self.speedy  # изменяем координату спрайта по вертикали в зависимости от скорости
        self.rect.x += self.speedx  # изменяем координату спрайта по горизонтали в зависимости от скорости
        if self.rect.top > HEIGHT: # задаем условие - пока спрайт не долетит до нижнего края окна, новый спрайт не появится
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-1000, -40)
            self.speedy = random.randrange(4, 8)

# Описание класса пуль (управляемые с клавиатуры)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y): # где x, y - координаты спрайта игрока
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img 
        self.image = pygame.transform.scale(bullet_img, (5, 50)) # уменьшаем размер картинки до заданного
        self.image.set_colorkey(BLACK) # убрать черный прямоугольник вокруг спрайта 


        #self.image = pygame.Surface((10, 20))
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        # удалить из списка, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()




# создаем новый набор для всех спрайтов
all_sprites = pygame.sprite.Group()
# создаем экземпляр класса Player
player = Player()
# добавляем наш экземпляр в общий набор спрайтов
all_sprites.add(player)

# создаем новый набор спрайтов для врагов:
mobs = pygame.sprite.Group()
# создаем экземпляры классов Враги:
for i in range(4):
    m = Mob()           # создаем в переменной m экземпляр класса
    all_sprites.add(m)  # добавляем экземпляр в общий набор всех спрайтов
    mobs.add(m)         # добавляем экземпляр в набор для врагов

# создаем новый набор спрайтов для пуль:
bullets = pygame.sprite.Group()







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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # ESC key pressed
                running = False
            elif event.key == pygame.K_SPACE:
                player.shoot()



    # Обновление спрайтов - вызывает для каждого спрайта из общего набора спрайтов метод update
    all_sprites.update()
    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
        
    # Проверка, не попала ли пуля в mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    # При попадании в mob удаляется спрайт mob. Компенсируем удаление созданием нового mob
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)



    # Рендеринг (отрисовка)
    screen.fill(BLACK)
    screen.blit(background, background_rect) # прорисовка фона - файл starfield2.png
    all_sprites.draw(screen)
    # После отрисовки буфера, переворачиваем экран
    pygame.display.flip()

pygame.quit()