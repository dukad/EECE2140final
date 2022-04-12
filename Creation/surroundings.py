# Find number of surrounding cells
def surrounding_cells(rand_wall, maze):
    s_cells = 0
    if maze[rand_wall[0] - 1][rand_wall[1]] == 1:
        s_cells += 1
    if maze[rand_wall[0] + 1][rand_wall[1]] == 1:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] - 1] == 1:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] + 1] == 1:
        s_cells += 1

    return s_cells
