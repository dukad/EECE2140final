# count surrounding pathings
def surr_count(wall, maze):
    """
    This function helps to count the number of cells that aren't walls
    directly bordering a given cell
    :param wall: reference wall used to index the surrounding cells
    :param maze: maze grid
    :return: return the number of surrounding cells
    """
    s_cells = 0
    if maze[wall[0] - 1][wall[1]] == 1:
        s_cells += 1
    if maze[wall[0] + 1][wall[1]] == 1:
        s_cells += 1
    if maze[wall[0]][wall[1] - 1] == 1:
        s_cells += 1
    if maze[wall[0]][wall[1] + 1] == 1:
        s_cells += 1

    return s_cells
