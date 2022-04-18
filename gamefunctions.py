import pygame
from cellclasses import Cell, Character
import colors as c
from Creation import actualMaker
from Creation import mazeSetup
from colors import lightgreen, blue

def create_a_maze(gamedimension, width, height):
    allspriteslist = pygame.sprite.Group()  # creates a group of items that will be drawn at the end
    maze = []
    walls = []
    mazeSetup.setup(height, width, maze, walls)
    actualMaker.maker(height, width, maze, walls)
    g2dimensions = gamedimension
    celldimensions = min((g2dimensions) / len(maze[1]), (g2dimensions) / len(maze))
    y = 1
    for row in maze:
        x = 1
        for val in row:
            if val == 0:
                newcell = Cell(c.black, x, y, celldimensions)
            else:
                newcell = Cell(c.white, x, y, celldimensions)
            x += 1
            allspriteslist.add(newcell)
        y += 1

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


def cell_available(cell, maze):
    availible = []
    try:
        if maze[cell.ymaze + 1][cell.xmaze] == 1:
            availible.append('d')
        if maze[cell.ymaze - 1][cell.xmaze] == 1:
            availible.append('u')
        if maze[cell.ymaze][cell.xmaze - 1] == 1:
            availible.append('l')
        if maze[cell.ymaze][cell.xmaze + 1] == 1:
            availible.append('r')
    except IndexError:
        pass
    return availible


def fill_maze_red(screen, celldimensions, startcell, color, realstartcell):
    current_cell = startcell
    cells = []
    list_of_cells = []
    while (current_cell.ymaze, current_cell.xmaze) != realstartcell:
        cells.append(pygame.Rect(20 + celldimensions*current_cell.xmaze, 20 + celldimensions*current_cell.ymaze, celldimensions, celldimensions))
        for i in range(len(cells)):
            pygame.draw.rect(screen, color, cells[i])
        list_of_cells.append(Cell(blue, current_cell.xmaze + 1, current_cell.ymaze + 1, celldimensions))
        current_cell = current_cell.prev
    return list_of_cells


def solve_maze(screen, maze, celldimensions, startcell, endcell, clock, prevnode=None, truestart=None):
    cellslist = pygame.sprite.Group()
    if truestart == None:
        true = startcell
    else:
        true = truestart
    in_maze = True
    current_cell = Cell(pygame.Color('Yellow'), startcell[1], startcell[0], celldimensions)
    current_cell.prev = prevnode
    while in_maze:
        newcell = pygame.Rect(20 + celldimensions*current_cell.xmaze, 20 + celldimensions*current_cell.ymaze, celldimensions, celldimensions)
        pygame.draw.rect(screen, current_cell.color, newcell)
        pygame.display.flip()
        available_cells = cell_available(current_cell, maze)
        if (current_cell.ymaze, current_cell.xmaze) == endcell:
            loc = fill_maze_red(screen, celldimensions, current_cell, lightgreen, true)
            for cell in loc:
                cellslist.add(cell)
            cellslist.add(Cell(blue, true[1] + 1, true[0] + 1, celldimensions))
            return True, cellslist
        elif len(available_cells) > 1:
            maze[current_cell.ymaze][current_cell.xmaze] = 0
            current_cell.Node = True
            for direction in available_cells:
                if direction == 'd':
                    solved, cells = solve_maze(screen, maze, celldimensions, (current_cell.ymaze + 1,current_cell.xmaze), endcell, clock, prevnode=current_cell, truestart=true)
                    if solved == True:
                        cellslist = cells
                        return True, cellslist
                if direction == 'r':
                    solved, cells = solve_maze(screen, maze, celldimensions,
                                               (current_cell.ymaze, current_cell.xmaze + 1), endcell, clock,
                                               prevnode=current_cell, truestart=true)
                    if solved == True:
                        cellslist = cells
                        return True, cellslist
                if direction == 'u':
                    solved, cells = solve_maze(screen, maze, celldimensions,
                                               (current_cell.ymaze - 1, current_cell.xmaze), endcell, clock,
                                               prevnode=current_cell, truestart=true)
                    if solved == True:
                        cellslist = cells
                        return True, cellslist
                if direction == 'l':
                    solved, cells = solve_maze(screen, maze, celldimensions,
                                               (current_cell.ymaze, current_cell.xmaze - 1), endcell, clock,
                                               prevnode=current_cell, truestart=true)
                    if solved == True:
                        cellslist = cells
                        return True, cellslist
        elif len(available_cells) == 0:
            maze[current_cell.ymaze][current_cell.xmaze] = 0
            fill_maze_red(screen, celldimensions, current_cell, pygame.Color('Yellow'), true)
            in_maze = False
        elif len(available_cells) == 1:
            if available_cells[0] == 'r':
                maze[current_cell.ymaze][current_cell.xmaze] = 0
                newcell = Cell(pygame.Color('Yellow'), current_cell.xmaze + 1, current_cell.ymaze, celldimensions)
                current_cell.next = newcell
                current_cell.next.prev = current_cell
                current_cell = current_cell.next
            elif available_cells[0] == 'l':
                maze[current_cell.ymaze][current_cell.xmaze] = 0
                newcell = Cell(pygame.Color('Yellow'), current_cell.xmaze - 1, current_cell.ymaze, celldimensions)
                current_cell.next = newcell
                current_cell.next.prev = current_cell
                current_cell = current_cell.next
            elif available_cells[0] == 'u':
                maze[current_cell.ymaze][current_cell.xmaze] = 0
                newcell = Cell(pygame.Color('Yellow'), current_cell.xmaze, current_cell.ymaze - 1, celldimensions)
                current_cell.next = newcell
                current_cell.next.prev = current_cell
                current_cell = current_cell.next
            elif available_cells[0] == 'd':
                maze[current_cell.ymaze][current_cell.xmaze] = 0
                nextcell = Cell(pygame.Color('Yellow'), current_cell.xmaze, current_cell.ymaze + 1, celldimensions)
                current_cell.next = nextcell
                current_cell.next.prev = current_cell
                current_cell = current_cell.next
    return False, cellslist