import actualMaker as Maker
import mazeSetup as Setup

height = int(input('Enter height: '))
length = int(input('Enter length: '))
maze = []
walls = []

Setup.setup(height, length, maze, walls)
Maker.maker(height, length, maze, walls)

for row in maze:
    for j in range(len(row)):
        print(row[j], end='')
    print('\n', end='')
