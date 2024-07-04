import pygame
import random

# Инициализация Pygame
pygame.init()

# Создание окна игры
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Арканоид")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Размеры платформы
platform_width = 100
platform_height = 10


# Класс для платформы
class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(win, BLUE, (self.x, self.y, platform_width, platform_height))


# Класс для мяча
class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        pygame.draw.circle(win, RED, (self.x, self.y), self.radius)


# Создание платформы и мяча
platform = Platform(win_width // 2 - platform_width // 2, win_height - 20)
ball = Ball(win_width // 2, win_height // 2, 10, random.choice([2, -2]), -2)

# Флаг для проверки завершения игры
game_over = False

# Основной игровой цикл
run = True
while run:
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform.x > 0:
        platform.x -= 3
    if keys[pygame.K_RIGHT] and platform.x < win_width - platform_width:
        platform.x += 3

    # Движение мяча
    ball.x += ball.speed_x
    ball.y += ball.speed_y

    if ball.y + ball.radius > win_height or ball.y - ball.radius < 0:
        ball.speed_y = -ball.speed_y
    if ball.x + ball.radius > win_width or ball.x - ball.radius < 0:
        ball.speed_x = -ball.speed_x

    # Проверка столкновения мяча с платформой
    if ball.y + ball.radius > platform.y and ball.x > platform.x and ball.x < platform.x + platform_width:
        ball.speed_y = -ball.speed_y

    # Проверка завершения игры
    if ball.y + ball.radius > win_height:
        game_over = True

    # Отрисовка платформы и мяча
    platform.draw()
    ball.draw()

    pygame.display.update()

    # Задержка
    pygame.time.delay(10)

# Завершение игры
pygame.quit()
