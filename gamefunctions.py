import pygame
from cellclasses import Cell, Character
import colors as c
from Creation import actualMaker
from Creation import mazeSetup

def create_a_maze(gamedimension, width, height):
    allspriteslist = pygame.sprite.Group()  # creates a group of items that will be drawn at the end
    maze = []
    walls = []
    mazeSetup.setup(height, width, maze, walls)
    actualMaker.maker(height, width, maze, walls)

    g2dimensions = gamedimension
    celldimensions = min((g2dimensions) / len(maze[1]), (g2dimensions) / len(maze))
    cellspacing = celldimensions
    y = 0
    for row in maze:
        y += cellspacing
        x = 0
        for val in row:
            x += cellspacing
            if val == 0:
                newcell = Cell(c.black, x, y, celldimensions)
            else:
                newcell = Cell(c.white, x, y, celldimensions)
            allspriteslist.add(newcell)

    startcell = None
    for cells in enumerate(maze[0]):
        if cells[1] == 1:
            startcell = cells[0]
    endcell = None
    for cells in enumerate(maze[-1]):
        if cells[1] == 1:
            endcell = cells[0]

    x = (startcell) + 1
    y = 1
    character = Character(c.lightgreen, x, y, celldimensions)
    allspriteslist.add(character)

    return allspriteslist, celldimensions, character, maze, startcell, endcell
