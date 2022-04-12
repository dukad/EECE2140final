from colorama import init, Fore
init()

def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)
    return maze

def print_maze(maze):
    s = ''
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                s += maze[i][j]
                # print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'c':
                # print(Fore.GREEN, f'{maze[i][j]}', end="")
                s += maze[i][j]
            else:
                # print(Fore.RED, f'{maze[i][j]}', end="")
                s += maze[i][j]
        s += '\n'
        # print('\n')
    return s