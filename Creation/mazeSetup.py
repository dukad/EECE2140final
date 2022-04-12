import random


def setup(height, width, maze, walls):
    # Mark everything as untouched
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)

    # Randomize starting point for first path
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    if starting_height == 0:
        starting_height += 1
    if starting_height == height - 1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width - 1:
        starting_width -= 1

    # create first path block and add its wall coordinates to list
    maze[starting_height][starting_width] = 1
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # mark walls in actual maze as 0
    maze[starting_height - 1][starting_width] = 0
    maze[starting_height][starting_width - 1] = 0
    maze[starting_height][starting_width + 1] = 0
    maze[starting_height + 1][starting_width] = 0
