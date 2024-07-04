# пинг - понг
# два игрока управляют ракетками с помощью клавиш
# "W", "S" и стрелок вверх / вниз, а мяч отражается от стен и ракеток.

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width = 800
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Пинг-понг")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(win, WHITE, self.rect)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.dx = 5
        self.dy = 5

    def draw(self):
        pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.topleft = (self.x, self.y)

# Создание игровых объектов
paddle1 = Paddle(50, height // 2 - 50)
paddle2 = Paddle(width - 60, height // 2 - 50)
ball = Ball(width // 2, height // 2)

# Очки игры
score1 = 0
score2 = 0

# Флаг начала игры
game_started = False

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_started = True

    if game_started:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1.y > 0:
            paddle1.y -= 5
        if keys[pygame.K_s] and paddle1.y < height - paddle1.height:
            paddle1.y += 5
        if keys[pygame.K_UP] and paddle2.y > 0:
            paddle2.y -= 5
        if keys[pygame.K_DOWN] and paddle2.y < height - paddle2.height:
            paddle2.y += 5

        ball.move()

        # Отражение мяча от стен и ракеток
        if ball.y <= 0 or ball.y >= height - ball.radius * 2:
            ball.dy = -ball.dy
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.dx = -ball.dx

        # Подсчет очков
        if ball.x <= 0:
            score2 += 1
            ball.x, ball.y = width // 2, height // 2
        if ball.x >= width:
            score1 += 1
            ball.x, ball.y = width // 2, height // 2

        # Отрисовка объектов
        win.fill(BLACK)
        paddle1.rect.topleft = (paddle1.x, paddle1.y)
        paddle2.rect.topleft = (paddle2.x, paddle2.y)
        paddle1.draw()
        paddle2.draw()
        ball.draw()

        # Отрисовка счета
        font = pygame.font.Font(None, 36)
        text = font.render(f"{score1} : {score2}", True, WHITE)
        win.blit(text, (width // 2 - text.get_width() // 2, 20))

        pygame.display.flip()