import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание класса блока
class Block:
    def __init__(self, x, y, color, shape):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Создание класса игры
class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(10)] for _ in range(20)]
        self.current_block = self.generate_block()
        self.score = 0

    def generate_block(self):
        shapes = [
            [[1, 1, 1, 1]],
            [[1, 1, 1], [0, 1, 0]],
            [[1, 1, 0], [0, 1, 1]],
            [[1, 1], [1, 1]],
            [[1, 0], [1, 1], [0, 1]],
            [[0, 1], [1, 1], [1, 0]],
            [[1, 1, 1], [0, 1, 0]]
        ]
        shape = random.choice(shapes)
        color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        return Block(4, 0, color)

    def check_collision(self):
        for i in range(len(self.current_block.shape)):
            for j in range(len(self.current_block.shape[i])):
                if self.current_block.shape[i][j] == 1:
                    if self.current_block.y + i >= len(self.grid) or self.current_block.x + j < 0 or self.current_block.x + j >= len(self.grid[0]) or self.grid[self.current_block.y + i][self.current_block.x + j] != 0:
                        return True
        return False

    def merge_block(self):
        for i in range(len(self.current_block.shape)):
            for j in range(len(self.current_block.shape[i])):
                if self.current_block.shape[i][j] == 1:
                    self.grid[self.current_block.y + i][self.current_block.x + j] = self.current_block.color

    def check_lines(self):
        lines_cleared = 0
        for i in range(len(self.grid)):
            if all(self.grid[i]):
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(10)])
                lines_cleared += 1
        self.score += lines_cleared ** 2

    def update(self):
        self.current_block.y += 1
        if self.check_collision():
            self.current_block.y -= 1
            self.merge_block()
            self.check_lines()
            self.current_block = self.generate_block()

    def draw(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != 0:
                    block = Block(j, i, self.grid[i][j])
                    block.draw()
        self.current_block.draw()

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Создание объекта игры
tetris = Tetris()

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    tetris.update()
    tetris.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(5)

pygame.quit()