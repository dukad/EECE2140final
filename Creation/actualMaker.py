import random
import surroundings as surr


def maker(height, width, maze, walls):
    while walls:
        # get random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Left wall:
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 1:
                # Find number of surrounding paths
                s_cells = surr.surrounding_cells(rand_wall, maze)

                if s_cells < 2:
                    # Make new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark new walls in maze:
                    # Upper
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom
                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Left
                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall so loop isn't infinite :)
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Upper wall:
        if rand_wall[0] != 0:
            if maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == 1:

                s_cells = surr.surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                continue

        # Bottom wall
        if rand_wall[0] != height - 1:
            if maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == 1:

                s_cells = surr.surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                continue

        # Right wall:
        if rand_wall[1] != width - 1:
            if maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == 1:

                s_cells = surr.surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                continue

        # Delete the wall from the list regardless
        for wall in walls:
            if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                walls.remove(wall)

    # Mark all untouched points as walls
    for i in range(0, height):
        for j in range(0, width):
            if maze[i][j] == 'u':
                maze[i][j] = 0

    # Make start
    for i in range(0, width):
        if maze[1][i] == 1:
            maze[0][i] = 1
            break
    # Make end
    for i in range(width - 1, 0, -1):
        if maze[height - 2][i] == 1:
            maze[height - 1][i] = 1
            break
