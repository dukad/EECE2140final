import actualMaker as Maker
from maze import Maze as M

height = int(input('Enter height: '))
length = int(input('Enter length: '))
Maze = M(height, length)

Maze.setup()
print(Maze)
Maze.maker()
print(Maze)


