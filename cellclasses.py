import pygame


class Cell(pygame.sprite.Sprite):
    """
    Cell class, used for each box in the maze, contains color, location, and size
    """
    def __init__(self, color, x, y, dimension):
        super().__init__()
        self.dimension = dimension
        self.color = color
        self.image = pygame.Surface([self.dimension, self.dimension])
        self.image.fill(self.color)
        self.xmaze = x
        self.ymaze = y
        # rectangluar position of the cell is dependant on its location in the maze
        self.rect = self.image.get_rect()
        self.rect.x = (self.xmaze - 1) * self.dimension + 20
        self.rect.y = (self.ymaze - 1) * self.dimension + 20
        self.prev = None
        self.next = None
        self.Node = False

    def __str__(self):
        # return color location and size of the cell
        return f'{self.color} cell at {self.ymaze},{self.xmaze} of dimension {self.dimension}'


class Character(pygame.sprite.Sprite):
    """
    character class, similar to a cell, but with an included move method needed to change the characters position
    """
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
        self.rect.x = (self.xmaze - 1) * self.dimension + 20
        self.rect.y = (self.ymaze - 1) * self.dimension + 20

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
        # dont let the character out of bounds
        except IndexError:
            pass
