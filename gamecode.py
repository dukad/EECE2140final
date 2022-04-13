import pygame
from cellclasses import Cell, Character
import colors as c
from gamefunctions import create_a_maze

# pg code!
pygame.init()
# create the screen
gamedimension = 600
extra_space = 200
screenwidth = gamedimension + extra_space
screen = pygame.display.set_mode((screenwidth, gamedimension + 100)) # input dimensions of the game
screen.fill(pygame.Color(c.white)) # sets the background colo
pygame.display.set_caption('Maze Game!') # This is the window of the game
inputx = '50'
inputy = '50'
allspriteslist, celldimensions, character, maze, startcell, endcell = create_a_maze(gamedimension, int(inputx), int(inputy))

# initialize sizing and location of buttons and text boxes
base_font = pygame.font.Font(None, 25)
xdimensions_rect = pygame.Rect(gamedimension + extra_space/2 - 50, 50, 100, 20)
ydimensions_rect = pygame.Rect(gamedimension + extra_space/2 - 50, 100, 100, 20)
create_new_maze = pygame.Rect(gamedimension + extra_space/2 - 50, 150, 100, 50)

clock = pygame.time.Clock()
running = True
inxtextbox = False
inytextbox = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.move('left', maze)
            if event.key == pygame.K_RIGHT:
                character.move('right', maze)
            if event.key == pygame.K_UP:
                character.move('up', maze)
            if event.key == pygame.K_DOWN:
                character.move('down', maze)
            if inxtextbox:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        inputx = inputx[:-1]
                    elif event.unicode.isdigit():
                        inputx += event.unicode
            elif inytextbox:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        inputy = inputy[:-1]
                    elif event.unicode.isdigit():
                        inputy += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if xdimensions_rect.collidepoint(event.pos):
                inxtextbox = True
            else:
                inxtextbox = False
            if ydimensions_rect.collidepoint(event.pos):
                inytextbox = True
            else:
                inytextbox = False
            if create_new_maze.collidepoint(event.pos):
                allspriteslist, celldimensions, character, maze, startcell, endcell = create_a_maze(gamedimension, int(inputx), int(inputy))

    allspriteslist.remove(character)
    character = Character(c.lightgreen, character.xmaze, character.ymaze, celldimensions)

    allspriteslist.add(character)

    # -- Draw everything
    # Clear screen
    screen.fill(c.white)
    allspriteslist.draw(screen)

    # code for boxes
    #textbox for x dimension
    pygame.draw.rect(screen, pygame.Color('gray'), xdimensions_rect)
    xdimbox = base_font.render(inputx, True, (255, 255, 255))
    screen.blit(xdimbox, (xdimensions_rect.x + 5, xdimensions_rect.y + 3))
    xdimensions_rect.w = max(100, xdimbox.get_width() + 10)

    # textbox for y dimension
    pygame.draw.rect(screen, pygame.Color('gray'), ydimensions_rect)
    ydimbox = base_font.render(inputy, True, (255, 255, 255))
    screen.blit(ydimbox, (ydimensions_rect.x + 5, ydimensions_rect.y + 3))
    ydimensions_rect.w = max(100, ydimbox.get_width() + 10)

    # button for creating a new maze
    pygame.draw.rect(screen, c.lightgreen, create_new_maze)
    createtext = base_font.render('NEW MAZE', True, c.black)
    screen.blit(createtext, (create_new_maze.x + 5, create_new_maze.y + 15))

    # code for text
    # text for x dimension
    xdimension = base_font.render('Width:', True, c.black)
    screen.blit(xdimension, (xdimensions_rect.x + 5, xdimensions_rect.y - 20))

    # text for y dimension
    ydimension = base_font.render('Height:', True, c.black)
    screen.blit(ydimension, (ydimensions_rect.x + 5, ydimensions_rect.y - 20))

    # Flip screen? apparently this is necessary
    pygame.display.flip()

    if (character.ymaze, character.xmaze) == (len(maze) , endcell + 1):
        allspriteslist, celldimensions, character, maze, startcell, endcell = create_a_maze(gamedimension, int(inputx), int(inputy))

    # Pause
    clock.tick(5)


