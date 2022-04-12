import actualMaker as Maker
import mazeSetup as Setup

height = int(input('Enter height: '))
width = int(input('Enter width: '))
maze = []
walls = []

Setup.setup(height, width, maze, walls)
Maker.maker(height, width, maze, walls)

for row in maze:
    for j in range(len(row)):
        print(row[j], end='')
    print('\n', end='')
