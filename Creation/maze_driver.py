import maze_printer as mp
import random as rand
cell = 'c'
wall = 'w'
height = 11
width = 27
x = mp.init_maze(width, height)
# check = mp.print_maze(x)
# print(check)
start_h = int(rand.random() * height)
start_w = int(rand.random() * width)

if start_h == 0:
    start_h += 1
if start_h == height-1:
    start_h -= 1
if start_w == 0:
    start_w += 1
if start_w == width-1:
    start_w -= 1

x[start_h][start_w] = cell
walls = []
walls.append([start_h - 1, start_w])
walls.append([start_h, start_w - 1])
walls.append([start_h, start_w + 1])
walls.append([start_h + 1, start_w])
x[start_h - 1][start_w] = wall
x[start_h][start_w -1] = wall
x[start_h][start_w + 1] = wall
x[start_h + 1][start_w] = wall

def surroundingCells(rand_wall):
    s_cells = 0
    if (x[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (x[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (x[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells +=1
    if (x[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1
    return s_cells

def delete_wall(rand_wall):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

while walls:
    rand_wall = walls[int(rand.random() * len(walls)) - 1]

    if rand_wall[1] != 0:
        if x[rand_wall[0]][rand_wall[1] - 1] == 'u' and x[rand_wall[0]][rand_wall[1] + 1] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                x[rand_wall[0]][rand_wall[1]] = 'c'
                if (rand_wall[0] != 0):
                    if (x[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        x[rand_wall[0] - 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])
            delete_wall(rand_wall)
            continue
        continue
    if rand_wall[0] != 0:
        if x[rand_wall[0] - 1][rand_wall[1]] == 'u' and x[rand_wall[0] + 1][rand_wall[1] + 1] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                x[rand_wall[0]][rand_wall[1]] = 'c'
                if (rand_wall[0] != 0):
                    if (x[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        x[rand_wall[0] - 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])
            delete_wall(rand_wall)
            continue
        continue
    if rand_wall[0] != height - 1:
        if x[rand_wall[0] + 1][rand_wall[1]] == 'u' and x[rand_wall[0] - 1][rand_wall[1]] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                x[rand_wall[0]][rand_wall[1]] = 'c'
                if (rand_wall[0] != 0):
                    if (x[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        x[rand_wall[0] - 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])
            delete_wall(rand_wall)
            continue
        continue
    if rand_wall[1] != width - 1:
        if x[rand_wall[0]][rand_wall[1] + 1] == 'u' and x[rand_wall[0]][rand_wall[1] - 1] == 'c':
            s_cells = surroundingCells(rand_wall)
            if s_cells < 2:
                x[rand_wall[0]][rand_wall[1]] = 'c'
                if (rand_wall[0] != 0):
                    if (x[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        x[rand_wall[0] - 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])
            delete_wall(rand_wall)
            continue
        continue

def make_walls(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if (x[i][j] == 'u'):
                x[i][j] = 'w'

def create_entrance_exit(width, height):
    for i in range(0, width):
        if (x[1][i] == 'c'):
            x[0][i] == 'c'
            break
    for i in range( width - 1, 0, -1):
        if (x[height - 2][i] == 'c'):
            x[height - 1][i] = 'c'
            break

check = mp.print_maze(x)
print(check)
