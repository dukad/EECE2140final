def del_wall(r_wall, walls):
    """
    This function deletes a given wall from a given list
    :param r_wall: wall to delete
    :param walls: list of walls to delete from
    :return: no return, just modifies the input list
    """
    for wall in walls:
        if wall[0] == r_wall[0] and wall[1] == r_wall[1]:
            walls.remove(wall)