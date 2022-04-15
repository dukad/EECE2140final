import random


def setup(height, length, maze, walls):
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
    for i in range(0, height):
        row = []
        for j in range(0, length):
            row.append('u')
        maze.append(row)

    # Randomize starting point for first path
    start_h = random.randint(1, height - 1)
    start_l = random.randint(1, length - 1)

    # create first path block and add its wall coordinates to list
    maze[start_h][start_l] = 1
    walls.append([start_h - 1, start_l])
    walls.append([start_h, start_l - 1])
    walls.append([start_h, start_l + 1])
    walls.append([start_h + 1, start_l])

    # mark cells surrounding original in actual maze as 0 to represent walls
    maze[start_h - 1][start_l] = 0
    maze[start_h][start_l - 1] = 0
    maze[start_h][start_l + 1] = 0
    maze[start_h + 1][start_l] = 0
