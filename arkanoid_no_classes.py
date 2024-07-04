import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Арканоид')

# Платформа
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH,
                     PADDLE_HEIGHT)

# Мяч
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, 5]

# Кирпичи
bricks = []
for y in range(10):
    for x in range(SCREEN_WIDTH // BRICK_WIDTH):
        brick = pygame.Rect(x * BRICK_WIDTH, y * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= 5
    if keys[pygame.K_RIGHT]:
        paddle.x += 5

    # Движение мяча
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Отскок от стен
    if ball.x <= 0 or ball.x + ball.width >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.y <= 0:
        ball_speed[1] = -ball_speed[1]

    # Отскок от платформы
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Проверка столкновения мяча с кирпичами
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed[1] = -ball_speed[1]

    # Отрисовка элементов
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.circle(screen, RED, (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
