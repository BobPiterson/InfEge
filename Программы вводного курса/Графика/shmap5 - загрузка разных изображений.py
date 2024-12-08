  # Игра Shmup - 5 часть
# вращение спрайтов, случайная загрузка изображений метеоритов
import pygame
import random
from os import path # для определения пути к файлу в любой операционной системе
# в переменную сохраняется правильный путь к папке относительно файла с кодом игры
img_dir = path.join(path.dirname(__file__), 'img') # в кавычках указывается папка с картинками
print(img_dir)
# размеры игрового окна
WIDTH = 1400
HEIGHT = 800
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
# масштабируем фон на весь экран
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "H-09.png")).convert()

# Загрузим в список все изображения метеоритов
meteor_images = []
meteor_list =['rotationY1.png','rotationY2.png','rotationY3.png','rotationY4.png','rotationY5.png','rotationY6.png','rotationY7.png',
              'rotationY8.png','rotationY9.png','rotationY10.png','rotationY11.png','rotationY12.png','rotationY13.png','rotationY14.png',
              'rotationY15.png','rotationY16.png','rotationY17.png','rotationY18.png','rotationY19.png','rotationY20.png','rotationY21.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

#meteor_img = pygame.image.load(path.join(img_dir, "rotationY1.png")).convert()
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
        # Зададим радиус игрока и временно нарисуем круг, чтобы определить правильность установки радиуса
        # это зависит от реального изображения космического корабля и применяется при рассчете сталкновений
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

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

        # при создании нового экземляра будем использовать случайное изображение из списка meteor_images
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()

        #self.image = meteor_img 
        self.image = pygame.transform.scale(self.image, (50, 50)) # уменьшаем размер картинки до заданного
        self.image.set_colorkey(BLACK) # убрать черный прямоугольник вокруг спрайта 

        #self.image = pygame.Surface((30, 40))
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        # Зададим радиус игрока и временно нарисуем круг, чтобы определить правильность установки радиуса
        # это зависит от реального изображения космического корабля и применяется при рассчете сталкновений
        # Если со временем будет решено использовать астероиды разных размеров, то указав радиус как 1/2.5 ширины изображения, 
        # можно будет не возвращаться к редактированию кода.
        self.radius = int(self.rect.width / 2.5)
        #pygame.draw.circle(self.image, YELLOW, self.rect.center, self.radius)

        self.rect.x = random.randrange(WIDTH - self.rect.width) # задаем начальную координату левого верхнего угла по Х от 0 до ширины окна-ширина спрайта
        self.rect.y = random.randrange(-1000, -40)  # задаем начальную координату левого верхнего угла по Y от -100 до -40 (т.е. спрайт рождается за пределами окна)
        self.speedy = random.randrange(4, 8)        # устанавливаем начальную скорость по У в диапазоне от 4 до 8
        self.speedx = random.randrange(-3, 3)       # устанавливаем начальную скорость по Х в диапазоне от -3 до 3

        # Зададим вращение метеоритам
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)

        # необходимо для контроля скорости анимации. Для игры не нужно каждый раз менять изображение спрайта в каждом кадре. 
        # При анимации изображения спрайта нужно лишь определить время — как часто оно будет меняться.
        # Вызывая pygame.time.get_ticks(), можно узнать, сколько миллисекунд прошло с тех пор, как часы были запущены. 
        # Так можно будет узнать, не пора ли менять изображение спрайта.
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rotate()
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

    def rotate(self): # вращение спрайтов
        now = pygame.time.get_ticks() # получаем текущее время в милисекундах
        if now - self.last_update > 50: # если с предыдущего вызова метода прошло более 50 милисекунд, обновляем переменную с временем
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360 # в переменную угла вращения записываем остаток от деления на 360 градусов, чтобы избежать величин углов больше 360
            #self.image = pygame.transform.rotate(self.image_orig, self.rot) 
            # зададим центр вращения спрайта и будем его восстанавливать каждый раз при вращении
            new_image = pygame.transform.rotate(self.image_orig, self.rot)#создадим новое изображение,указывая исходное изображение и угол поворота          
            #self.image = pygame.transform.scale(self.image, (50, 50)) # уменьшаем размер картинки до заданного
            old_center = self.rect.center
            self.image = pygame.transform.scale(new_image, (50, 50)) # уменьшаем размер картинки до заданного
            #self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


# Описание класса пуль (управляемые с клавиатуры)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y): # где x, y - координаты спрайта игрока
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img 

        # self.image = pygame.Surface((5, 50))
        # self.image.fill(GREEN)

        self.image = pygame.transform.scale(bullet_img, (4, 50)) # уменьшаем размер картинки до заданного
        self.image.set_colorkey(BLACK) # убрать черный прямоугольник вокруг спрайта 

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

# создаем новый набор спрайтов для метеоритов:
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


    # проверка, не ударил ли моб игрока, используя круглые пересечения
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False

    # Проверка, не ударил ли моб игрока, используя прямоугольные пересечения
    # hits = pygame.sprite.spritecollide(player, mobs, False)
    # if hits:
    #     running = False
        
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