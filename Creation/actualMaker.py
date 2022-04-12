import random
import surroundings as surr


def maker(height, width, maze, walls):
    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Check if it is a left wall
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 1:
                # Find the number of surrounding cells
                s_cells = surr.surrounding_cells(rand_wall, maze)

                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
                    # Upper cell
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom cell
                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Leftmost cell
                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if rand_wall[0] != 0:
            if maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == 1:

                s_cells = surr.surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
                    # Upper cell
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 1:
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Leftmost cell
                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Rightmost cell
                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 1:
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if rand_wall[0] != height - 1:
            if maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == 1:

                s_cells = surr.surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
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

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Check the right wall
        if rand_wall[1] != width - 1:
            if maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == 1:

                s_cells = surr.surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
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

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if maze[i][j] == 'u':
                maze[i][j] = 0

    # Set entrance and exit
    for i in range(0, width):
        if maze[1][i] == 1:
            maze[0][i] = 1
            break

    for i in range(width - 1, 0, -1):
        if maze[height - 2][i] == 1:
            maze[height - 1][i] = 1
            break
