import pygame
from cellclasses import Cell, Character
import colors as c
from maze import Maze
from colors import lightgreen, blue


class MazeVisual(Maze):
    """
    The MazeVisual class, a subclass of the Maze class, is used to display a maze in the GUI.
    """
    def __init__(self, gamedimension, width, height):
        super().__init__(height, width)
        self.gamedimension = gamedimension
        self.allspriteslist = None
        self.character = None
        self.startcell = None
        self.endcell = None

    def create_a_maze(self):
        """
        This function creates and draws a maze based on the input width and height dimensions
        """
        allspriteslist = pygame.sprite.Group()  # creates a group of items that will be drawn at the end
        super().setup()
        super().maker()
        g2dimensions = self.gamedimension
        celldimensions = min(g2dimensions / self.length, g2dimensions / self.height)
        # Iterate through the maze, creating a cell for each wall or path
        y = 1
        for row in self.maze:
            x = 1
            for val in row:
                if val == 0:
                    newcell = Cell(c.black, x, y, celldimensions)
                else:
                    newcell = Cell(c.white, x, y, celldimensions)
                x += 1
                allspriteslist.add(newcell)
            y += 1
        # find where the end cell and start cell is in the maze
        startcell = None
        for cells in enumerate(self.maze[0]):
            if cells[1] == 1:
                startcell = cells[0]
        endcell = None
        for cells in enumerate(self.maze[-1]):
            if cells[1] == 1:
                endcell = cells[0]

        x = startcell + 1
        y = 1
        # create the character and add it to the sprite group
        self.character = Character(blue, x, y, celldimensions)
        allspriteslist.add(self.character)
        self.startcell = startcell
        maze = self.maze
        self.endcell = endcell
        self.allspriteslist = allspriteslist
        return allspriteslist, celldimensions, self.character, maze, startcell, endcell


class SolvingAlgorithm:
    def __init__(self, maze, startcell, endcell):
        self.maze = maze
        self.startcell = startcell
        self.endcell = endcell

    def cell_available(self, cell):
        """
        creates a list of all the available directions to progress in the maze
        :param cell: type Cell
        :return: list of characters
        """
        availible = []
        # check every direction to see if it's available
        try:
            if self.maze[cell.ymaze + 1][cell.xmaze] == 1:
                availible.append('d')
            if self.maze[cell.ymaze][cell.xmaze + 1] == 1:
                availible.append('r')
            if self.maze[cell.ymaze - 1][cell.xmaze] == 1:
                availible.append('u')
            if self.maze[cell.ymaze][cell.xmaze - 1] == 1:
                availible.append('l')
        # pass index errors because that implies you are on the edge of the maze, and in that case, the direction
        # is not available
        except IndexError:
            pass
        return availible

    def fill_maze_red(self, screen, celldimensions, startcell, color, solved=False):

        """
        fills a path a certain color going either back to the start of the maze, or until a node
        :param screen: pygame screen to draw on
        :param celldimensions: dimensions of each cell
        :param startcell: coordinate location of the start cell
        :param color: color to fill in the maze
        :param realstartcell: coordinate location of the true start of the maze, not just where to draw to
        :param solved: if the maze is completely solved
        :return: list_of_cells: a list of cells to continue drawing once the maze has been solved
        """
        realstartcell = self.startcell
        first = True  # This variable is needed because if you call the function starting on a node, you still want
        # it to run
        current_cell = startcell  # where to start the process
        cells = []
        list_of_cells = []
        # if the maze is solved, go back all the way to the beginning
        if solved:
            while (current_cell.ymaze, current_cell.xmaze) != realstartcell:
                cells.append(pygame.Rect(20 + celldimensions*current_cell.xmaze, 20 + celldimensions*current_cell.ymaze,
                                         celldimensions, celldimensions))
                for i in range(len(cells)):
                    pygame.draw.rect(screen, color, cells[i])
                list_of_cells.append(Cell(lightgreen, current_cell.xmaze + 1, current_cell.ymaze + 1, celldimensions))
                current_cell = current_cell.prev
        # if the maze hasnt been solved, only go back to the last node
        else:
            while (first) or (not current_cell.Node) and type(current_cell) == Cell:
                cells.append(pygame.Rect(20 + celldimensions*current_cell.xmaze, 20 + celldimensions*current_cell.ymaze,
                                         celldimensions, celldimensions))
                for i in range(len(cells)):
                    pygame.draw.rect(screen, color, cells[i])
                current_cell = current_cell.prev
                first = False
        # return a list of cells to continue drawing
        return list_of_cells

    @staticmethod
    def solve_maze(screen, maze, celldimensions, startcell, endcell, clock, mazeobj, prevnode=None, truestart=None):
        """
        solves the maze
        :param screen: screen to draw on
        :param maze: matrix of ones and zeros
        :param celldimensions: size of each cell
        :param startcell: coordinates of start cell
        :param endcell: coordinates of endcell
        :param clock: pygame clock to change timing
        :param prevnode: previous node(if used in recursion)
        :param truestart: real start of the maze(if used in recursion)
        :return: Bool, list of cells to draw
        """
        cellslist = pygame.sprite.Group()
        # are we starting at the real beginning of the maze, or is this recursion?
        if truestart is None:
            true = startcell
        else:
            true = truestart
        in_maze = True
        # color the current cell yellow
        current_cell = Cell(pygame.Color('Yellow'), startcell[1], startcell[0], celldimensions)
        current_cell.prev = prevnode
        # while in the maze, continue to progress throught the maze and draw a path
        while in_maze:
            newcell = pygame.Rect(20 + celldimensions*current_cell.xmaze, 20 + celldimensions*current_cell.ymaze,
                                  celldimensions, celldimensions)
            pygame.draw.rect(screen, current_cell.color, newcell)
            pygame.display.flip()
            available_cells = mazeobj.cell_available(current_cell)
            # if the maze is solved
            if (current_cell.ymaze, current_cell.xmaze) == endcell:
                loc = mazeobj.fill_maze_red(screen, celldimensions, current_cell, lightgreen, solved=True)
                for cell in loc:
                    cellslist.add(cell)
                cellslist.add(Cell(lightgreen, true[1] + 1, true[0] + 1, celldimensions))
                return True, cellslist
            # if there is more than one available path, recurse this function in each available path.
            # If none of the paths work, color the path red
            elif len(available_cells) > 1:
                maze[current_cell.ymaze][current_cell.xmaze] = 0
                current_cell.Node = True
                for direction in available_cells:
                    if direction == 'd':
                        solved, cells = mazeobj.solve_maze(screen, maze, celldimensions,
                                                   (current_cell.ymaze + 1, current_cell.xmaze), endcell, clock,
                                                           mazeobj, prevnode=current_cell, truestart=true)
                        if solved:
                            cellslist = cells
                            return True, cellslist
                    if direction == 'u':
                        solved, cells = mazeobj.solve_maze(screen, maze, celldimensions,
                                                   (current_cell.ymaze - 1, current_cell.xmaze), endcell, clock,
                                                   mazeobj, prevnode=current_cell, truestart=true)
                        if solved:
                            cellslist = cells
                            return True, cellslist
                        elif direction == available_cells[-1]:
                            maze[current_cell.ymaze][current_cell.xmaze] = 0
                            mazeobj.fill_maze_red(screen, celldimensions, current_cell, pygame.Color('Red'))
                    if direction == 'r':
                        solved, cells = mazeobj.solve_maze(screen, maze, celldimensions,
                                                   (current_cell.ymaze, current_cell.xmaze + 1), endcell, clock,
                                                   mazeobj, prevnode=current_cell, truestart=true)
                        if solved:
                            cellslist = cells
                            return True, cellslist
                        elif direction == available_cells[-1]:
                            maze[current_cell.ymaze][current_cell.xmaze] = 0
                            mazeobj.fill_maze_red(screen, celldimensions, current_cell, pygame.Color('Red'))
                    if direction == 'l':
                        solved, cells = mazeobj.solve_maze(screen, maze, celldimensions,
                                                   (current_cell.ymaze, current_cell.xmaze - 1), endcell, clock,
                                                   mazeobj, prevnode=current_cell, truestart=true)
                        if solved:
                            cellslist = cells
                            return True, cellslist
                        elif direction == available_cells[-1]:
                            maze[current_cell.ymaze][current_cell.xmaze] = 0
                            mazeobj.fill_maze_red(screen, celldimensions, current_cell, pygame.Color('Red'))

            # if there are no cells, color this path red
            elif len(available_cells) == 0:
                maze[current_cell.ymaze][current_cell.xmaze] = 0
                mazeobj.fill_maze_red(screen, celldimensions, current_cell, pygame.Color('Red'))
                in_maze = False
            # if there's only one available cell, go to that cell
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
            clock.tick(5000)
        return False, cellslist
