import pygame
import colors as c

class Cell(pygame.sprite.Sprite):
    def __init__(self, color, x, y, dimension):
        super().__init__()
        self.dimension = dimension
        self.color = color

        self.image = pygame.Surface([self.dimension, self.dimension])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Character(pygame.sprite.Sprite):
    def __init__(self, color, xmaze, ymaze, dimension):
        super().__init__()
        self.color = color
        self.dimension = dimension
        self.image = pygame.Surface([self.dimension, self.dimension])
        self.image.fill(self.color)
        self.xmaze = xmaze
        self.ymaze = ymaze

        # i want the position of this character to depend on its location in the maze
        self.rect = self.image.get_rect()
        self.rect.x = self.xmaze * self.dimension
        self.rect.y = self.ymaze * self.dimension

    def move(self, direction, maze):
        x = self.xmaze - 1
        y = self.ymaze - 1
        try:
            if direction == 'up':
                if maze[y-1][x] == 1:
                    self.ymaze += -1
            if direction == 'down':
                if maze[y+1][x] == 1:
                    self.ymaze += 1
            if direction == 'left':
                if maze[y][x-1] == 1:
                    self.xmaze += -1
            if direction == 'right':
                if maze[y][x+1] == 1:
                    self.xmaze += 1
        except IndexError:
            pass
