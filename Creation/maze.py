import random


class Maze:
    def __init__(self, height, length):
        self.maze = []
        self.walls = []
        self.height = height
        self.length = length

    def __str__(self):
        for row in self.maze:
            for j in range(len(row)):
                print(row[j], end='')
            print('\n', end='')
        return '\n'

    def setup(self):
        """
        This function takes care of the first two steps of Prim's algorithm:
        1. Start with a grid full of walls
        2. Pick a cell, mark it as part of the maze, and add its walls to a list of walls
        :param height: desired maze height
        :param length: desired maze length
        :param maze: matrix representing cells of the maze
        :param walls: list of walls
        :return: no return, just modifies the input maze and list of walls
        """
        # Mark everything as untouched
        for i in range(0, self.height):
            row = []
            for j in range(0, self.length):
                row.append('u')
            self.maze.append(row)

        # Randomize starting point for first path
        start_h = random.randint(1, self.height - 2)
        start_l = random.randint(1, self.length - 2)

        # create first path block and add its wall coordinates to list
        self.maze[start_h][start_l] = 1
        self.walls.append([start_h - 1, start_l])
        self.walls.append([start_h, start_l - 1])
        self.walls.append([start_h, start_l + 1])
        self.walls.append([start_h + 1, start_l])

        # mark cells surrounding original in actual maze as 0 to represent walls
        self.maze[start_h - 1][start_l] = 0
        self.maze[start_h][start_l - 1] = 0
        self.maze[start_h][start_l + 1] = 0
        self.maze[start_h + 1][start_l] = 0

    def del_wall(self, r_wall):
        """
        This function deletes a given wall from a given list
        :param r_wall: wall to delete
        :param walls: list of walls to delete from
        :return: no return, just modifies the input list
        """
        for wall in self.walls:
            if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
                self.walls.remove(wall)

    # count surrounding pathings
    def surr_count(self, wall):
        """
        This function helps to count the number of cells that aren't walls
        directly bordering a given cell
        :param wall: reference wall used to index the surrounding cells
        :param maze: maze grid
        :return: return the number of surrounding cells
        """
        s_cells = 0
        if self.maze[wall[0] - 1][wall[1]] == 1:
            s_cells += 1
        if self.maze[wall[0] + 1][wall[1]] == 1:
            s_cells += 1
        if self.maze[wall[0]][wall[1] - 1] == 1:
            s_cells += 1
        if self.maze[wall[0]][wall[1] + 1] == 1:
            s_cells += 1

        return s_cells

    def maker(self):
        while self.walls:
            # get random wall
            r_wall = self.walls[random.randint(0, len(self.walls) - 1)]
            # Make sure not a left-most wall to avoid index error:
            if r_wall[1] != 0:
                # If left cell is untouched and right cell is a path:
                if self.maze[r_wall[0]][r_wall[1] - 1] == 'u' and self.maze[r_wall[0]][r_wall[1] + 1] == 1:
                    # Find number of surrounding paths
                    s_cells = self.surr_count(r_wall)
                    # If cell does not have more than one path around it:
                    if s_cells < 2:
                        # Turn wall into a new path
                        self.maze[r_wall[0]][r_wall[1]] = 1

                        # Mark new walls in maze:
                        # make sure not a top-most wall to avoid index error:
                        if r_wall[0] != 0:
                            # As long as top cell is not already a path, make it a wall:
                            if self.maze[r_wall[0] - 1][r_wall[1]] != 1:
                                self.maze[r_wall[0] - 1][r_wall[1]] = 0
                            # Add this new wall to the list of walls as long as it isn't already in there
                            if [r_wall[0] - 1, r_wall[1]] not in self.walls:
                                self.walls.append([r_wall[0] - 1, r_wall[1]])

                        # Make sure not a bottom-most wall to avoid index error
                        if r_wall[0] != self.height - 1:
                            # As long as the bottom cell is not already a path, make it a wall
                            if self.maze[r_wall[0] + 1][r_wall[1]] != 1:
                                self.maze[r_wall[0] + 1][r_wall[1]] = 0
                            # Add this new wall to the list of walls as long as it isn't already in there
                            if [r_wall[0] + 1, r_wall[1]] not in self.walls:
                                self.walls.append([r_wall[0] + 1, r_wall[1]])

                        # Make sure not a left-most wall to avoid index error
                        if r_wall[1] != 0:
                            # As long as the left cell is not already a path, make it a wall
                            if self.maze[r_wall[0]][r_wall[1] - 1] != 1:
                                self.maze[r_wall[0]][r_wall[1] - 1] = 0
                            # Add this new wall to the list of walls as long as it isn't already in there
                            if [r_wall[0], r_wall[1] - 1] not in self.walls:
                                self.walls.append([r_wall[0], r_wall[1] - 1])
                    # Note that we don't need to do anything for the 'right wall' because we know it is a path already
                    # Delete random wall so loop isn't infinite :)
                    self.del_wall(r_wall)
                    continue

            # Make sure not a top-most cell to avoid index error:
            if r_wall[0] != 0:
                # if top cell is untouched and bottom cell is a path:
                if self.maze[r_wall[0] - 1][r_wall[1]] == 'u' and self.maze[r_wall[0] + 1][r_wall[1]] == 1:

                    s_cells = self.surr_count(r_wall)
                    if s_cells < 2:
                        self.maze[r_wall[0]][r_wall[1]] = 1

                        if r_wall[0] != 0:
                            if self.maze[r_wall[0] - 1][r_wall[1]] != 1:
                                self.maze[r_wall[0] - 1][r_wall[1]] = 0
                            if [r_wall[0] - 1, r_wall[1]] not in self.walls:
                                self.walls.append([r_wall[0] - 1, r_wall[1]])

                        if r_wall[1] != 0:
                            if self.maze[r_wall[0]][r_wall[1] - 1] != 1:
                                self.maze[r_wall[0]][r_wall[1] - 1] = 0
                            if [r_wall[0], r_wall[1] - 1] not in self.walls:
                                self.walls.append([r_wall[0], r_wall[1] - 1])

                        if r_wall[1] != self.length - 1:
                            if self.maze[r_wall[0]][r_wall[1] + 1] != 1:
                                self.maze[r_wall[0]][r_wall[1] + 1] = 0
                            if [r_wall[0], r_wall[1] + 1] not in self.walls:
                                self.walls.append([r_wall[0], r_wall[1] + 1])

                    self.del_wall(r_wall)
                    continue

            # Make sure not a bottom-most cell to avoid index error:
            if r_wall[0] != self.height - 1:
                # if bottom cell is untouched and top cell is a path:
                if self.maze[r_wall[0] + 1][r_wall[1]] == 'u' and self.maze[r_wall[0] - 1][r_wall[1]] == 1:

                    s_cells = self.surr_count(r_wall)
                    if s_cells < 2:
                        self.maze[r_wall[0]][r_wall[1]] = 1

                        if r_wall[0] != self.height - 1:
                            if self.maze[r_wall[0] + 1][r_wall[1]] != 1:
                                self.maze[r_wall[0] + 1][r_wall[1]] = 0
                            if [r_wall[0] + 1, r_wall[1]] not in self.walls:
                                self.walls.append([r_wall[0] + 1, r_wall[1]])
                        if r_wall[1] != 0:
                            if self.maze[r_wall[0]][r_wall[1] - 1] != 1:
                                self.maze[r_wall[0]][r_wall[1] - 1] = 0
                            if [r_wall[0], r_wall[1] - 1] not in self.walls:
                                self.walls.append([r_wall[0], r_wall[1] - 1])
                        if r_wall[1] != self.length - 1:
                            if self.maze[r_wall[0]][r_wall[1] + 1] != 1:
                                self.maze[r_wall[0]][r_wall[1] + 1] = 0
                            if [r_wall[0], r_wall[1] + 1] not in self.walls:
                                self.walls.append([r_wall[0], r_wall[1] + 1])

                    self.del_wall(r_wall)
                    continue

            # Make sure not a right-most cell to avoid index error
            if r_wall[1] != self.length - 1:
                # if right cell is untouched and left cell is a path:
                if self.maze[r_wall[0]][r_wall[1] + 1] == 'u' and self.maze[r_wall[0]][r_wall[1] - 1] == 1:

                    s_cells = self.surr_count(r_wall)
                    if s_cells < 2:
                        self.maze[r_wall[0]][r_wall[1]] = 1

                        if r_wall[1] != self.length - 1:
                            if self.maze[r_wall[0]][r_wall[1] + 1] != 1:
                                self.maze[r_wall[0]][r_wall[1] + 1] = 0
                            if [r_wall[0], r_wall[1] + 1] not in self.walls:
                                self.walls.append([r_wall[0], r_wall[1] + 1])
                        if r_wall[0] != self.height - 1:
                            if self.maze[r_wall[0] + 1][r_wall[1]] != 1:
                                self.maze[r_wall[0] + 1][r_wall[1]] = 0
                            if [r_wall[0] + 1, r_wall[1]] not in self.walls:
                                self.walls.append([r_wall[0] + 1, r_wall[1]])
                        if r_wall[0] != 0:
                            if self.maze[r_wall[0] - 1][r_wall[1]] != 1:
                                self.maze[r_wall[0] - 1][r_wall[1]] = 0
                            if [r_wall[0] - 1, r_wall[1]] not in self.walls:
                                self.walls.append([r_wall[0] - 1, r_wall[1]])

                    self.del_wall(r_wall)
                    continue

            # Delete the wall from the list regardless
            self.del_wall(r_wall)

        # Mark all remaining untouched points as walls
        for i in range(0, self.height):
            for j in range(0, self.length):
                if self.maze[i][j] == 'u':
                    self.maze[i][j] = 0

        # Make start
        for i in range(0, self.length):
            # Go through top row of maze to find a place to insert a start
            if self.maze[1][i] == 1:
                self.maze[0][i] = 1
                break
        # Make end
        for i in range(self.length - 1, 0, -1):
            # Go through bottom row of maze to find a place to end
            if self.maze[self.height - 2][i] == 1:
                self.maze[self.height - 1][i] = 1
                break
