import random
from Creation import surroundings as surr
from Creation import deleteWall as delWall


def maker(height, length, maze, walls):
    while walls:
        # get random wall
        r_wall = walls[random.randint(0, len(walls) - 1)]
        # Make sure not a left-most wall to avoid index error:
        if r_wall[1] != 0:
            # If left cell is untouched and right cell is a path:
            if maze[r_wall[0]][r_wall[1] - 1] == 'u' and maze[r_wall[0]][r_wall[1] + 1] == 1:
                # Find number of surrounding paths
                s_cells = surr.surr_count(r_wall, maze)
                # If cell does not have more than one path around it:
                if s_cells < 2:
                    # Turn wall into a new path
                    maze[r_wall[0]][r_wall[1]] = 1

                    # Mark new walls in maze:
                    # make sure not a top-most wall to avoid index error:
                    if r_wall[0] != 0:
                        # As long as bottom cell is not already a path, make it a wall:
                        if maze[r_wall[0] - 1][r_wall[1]] != 1:
                            maze[r_wall[0] - 1][r_wall[1]] = 0
                        # Add this new wall to the list of walls as long as it isn't already in there
                        if [r_wall[0] - 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] - 1, r_wall[1]])

                    # Make sure not a bottom-most wall to avoid index error
                    if r_wall[0] != height - 1:
                        # As long as the top cell is not already a path, make it a wall
                        if maze[r_wall[0] + 1][r_wall[1]] != 1:
                            maze[r_wall[0] + 1][r_wall[1]] = 0
                        # Add this new wall to the list of walls as long as it isn't already in there
                        if [r_wall[0] + 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])

                    # Make sure not a left-most wall to avoid index error
                    if r_wall[1] != 0:
                        # As long as the left cell is not already a path, make it a wall
                        if maze[r_wall[0]][r_wall[1] - 1] != 1:
                            maze[r_wall[0]][r_wall[1] - 1] = 0
                        # Add this new wall to the list of walls as long as it isn't already in there
                        if [r_wall[0], r_wall[1] - 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] - 1])
                # Note that we don't need to do anything for the 'right wall' because we know it is a path already
                # Delete random wall so loop isn't infinite :)
                delWall.del_wall(r_wall, walls)
                continue

        # Make sure not a top-most cell to avoid index error:
        if r_wall[0] != 0:
            # if bottom cell is untouched and top cell is a path:
            if maze[r_wall[0] - 1][r_wall[1]] == 'u' and maze[r_wall[0] + 1][r_wall[1]] == 1:

                s_cells = surr.surr_count(r_wall, maze)
                if s_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = 1

                    if r_wall[0] != 0:
                        if maze[r_wall[0] - 1][r_wall[1]] != 1:
                            maze[r_wall[0] - 1][r_wall[1]] = 0
                        if [r_wall[0] - 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] - 1, r_wall[1]])

                    if r_wall[1] != 0:
                        if maze[r_wall[0]][r_wall[1] - 1] != 1:
                            maze[r_wall[0]][r_wall[1] - 1] = 0
                        if [r_wall[0], r_wall[1] - 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] - 1])

                    if r_wall[1] != length - 1:
                        if maze[r_wall[0]][r_wall[1] + 1] != 1:
                            maze[r_wall[0]][r_wall[1] + 1] = 0
                        if [r_wall[0], r_wall[1] + 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] + 1])

                delWall.del_wall(r_wall, walls)
                continue

        # Make sure not a bottom-most cell to avoid index error:
        if r_wall[0] != height - 1:
            # if top cell is untouched and bottom cell is a path:
            if maze[r_wall[0] + 1][r_wall[1]] == 'u' and maze[r_wall[0] - 1][r_wall[1]] == 1:

                s_cells = surr.surr_count(r_wall, maze)
                if s_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = 1

                    if r_wall[0] != height - 1:
                        if maze[r_wall[0] + 1][r_wall[1]] != 1:
                            maze[r_wall[0] + 1][r_wall[1]] = 0
                        if [r_wall[0] + 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])
                    if r_wall[1] != 0:
                        if maze[r_wall[0]][r_wall[1] - 1] != 1:
                            maze[r_wall[0]][r_wall[1] - 1] = 0
                        if [r_wall[0], r_wall[1] - 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] - 1])
                    if r_wall[1] != length - 1:
                        if maze[r_wall[0]][r_wall[1] + 1] != 1:
                            maze[r_wall[0]][r_wall[1] + 1] = 0
                        if [r_wall[0], r_wall[1] + 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] + 1])

                delWall.del_wall(r_wall, walls)
                continue

        # Make sure not a right-most cell to avoid index error
        if r_wall[1] != length - 1:
            # if right cell is untouched and left cell is a path:
            if maze[r_wall[0]][r_wall[1] + 1] == 'u' and maze[r_wall[0]][r_wall[1] - 1] == 1:

                s_cells = surr.surr_count(r_wall, maze)
                if s_cells < 2:
                    maze[r_wall[0]][r_wall[1]] = 1

                    if r_wall[1] != length - 1:
                        if maze[r_wall[0]][r_wall[1] + 1] != 1:
                            maze[r_wall[0]][r_wall[1] + 1] = 0
                        if [r_wall[0], r_wall[1] + 1] not in walls:
                            walls.append([r_wall[0], r_wall[1] + 1])
                    if r_wall[0] != height - 1:
                        if maze[r_wall[0] + 1][r_wall[1]] != 1:
                            maze[r_wall[0] + 1][r_wall[1]] = 0
                        if [r_wall[0] + 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] + 1, r_wall[1]])
                    if r_wall[0] != 0:
                        if maze[r_wall[0] - 1][r_wall[1]] != 1:
                            maze[r_wall[0] - 1][r_wall[1]] = 0
                        if [r_wall[0] - 1, r_wall[1]] not in walls:
                            walls.append([r_wall[0] - 1, r_wall[1]])

                delWall.del_wall(r_wall, walls)
                continue

        # Delete the wall from the list regardless
        delWall.del_wall(r_wall, walls)

    # Mark all remaining untouched points as walls
    for i in range(0, height):
        for j in range(0, length):
            if maze[i][j] == 'u':
                maze[i][j] = 0

    # Make start
    for i in range(0, length):
        # Go through top row of maze to find a place to insert a start
        if maze[1][i] == 1:
            maze[0][i] = 1
            break
    # Make end
    for i in range(length - 1, 0, -1):
        # Go through bottom row of maze to find a place to end
        if maze[height - 2][i] == 1:
            maze[height - 1][i] = 1
            break
