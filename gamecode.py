import pygame
from cellclasses import Character
import colors as c
from gamefunctions import create_a_maze
from timer import Timer

# pg code!
pygame.init()
# create the screen
gamedimension = 600
extra_space = 200
screenwidth = gamedimension + extra_space
screen = pygame.display.set_mode((screenwidth, gamedimension + 50)) # input dimensions of the game
image = pygame.image.load('mazeimage.jpg')
screen.fill(pygame.Color(c.white)) # sets the background colo
pygame.display.set_caption('Maze Game!') # This is the window of the game
pygame.display.set_icon(image)
inputx = '50'
inputy = '50'
allspriteslist, celldimensions, character, maze, startcell, endcell = create_a_maze(gamedimension, int(inputx), int(inputy))
points_earned = '--'

with open('mazepoints.txt', 'r+') as f:
    maze_points = int(f.readline())
    highscore = int(f.readline())

# initialize sizing and location of buttons and text boxes
base_font = pygame.font.Font(None, 25)

xdimensions_rect = pygame.Rect(gamedimension + extra_space/2 - 50, 50, 100, 20)
ydimensions_rect = pygame.Rect(gamedimension + extra_space/2 - 50, 100, 100, 20)
create_new_maze = pygame.Rect(gamedimension + extra_space/2 - 50, 150, 100, 50)
solve_the_maze = pygame.Rect(gamedimension + extra_space/2 - 50, 225, 100, 50)

clock = pygame.time.Clock()
running = True
inxtextbox = False
inytextbox = False
timer = Timer()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('mazepoints.txt', 'w') as f:
                f.write(str(maze_points))
                f.write('\n')
                f.write(str(highscore))
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
                timer.reset()
            if solve_the_maze.collidepoint(event.pos):
                points_earned = (len(maze) * len(maze[0])) // max(timer.time_in_secs(), 1)
                if highscore < points_earned:
                    highscore = points_earned
                maze_points += points_earned
                allspriteslist, celldimensions, character, maze, startcell, endcell = create_a_maze(gamedimension,
                                                                                                    int(inputx),
                                                                                                    int(inputy))
                timer.reset()

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

    # button for solving the maze
    pygame.draw.rect(screen, pygame.Color('yellow'), solve_the_maze)
    createtext2 = base_font.render('SOLVE', True, c.black)
    screen.blit(createtext2, (solve_the_maze.x + 25, solve_the_maze.y + 15))

    # code for text
    # text for x dimension
    xdimension = base_font.render('Width:', True, c.black)
    screen.blit(xdimension, (xdimensions_rect.x + 5, xdimensions_rect.y - 20))

    # text for y dimension
    ydimension = base_font.render('Height:', True, c.black)
    screen.blit(ydimension, (ydimensions_rect.x + 5, ydimensions_rect.y - 20))

    # code for maze points
    fontsize = min(int(300/len(str(maze_points))), 100)
    number_font = pygame.font.Font(None, fontsize)
    textcentering = gamedimension + extra_space/2 - (6/35*fontsize*len(str(maze_points)))
    mazetext = number_font.render(str(maze_points), True, c.black)
    screen.blit(mazetext, (textcentering, 325))
    mazepointstext = base_font.render('Points:', True, c.black)
    screen.blit(mazepointstext, (gamedimension + 75, 300))

    #code for highscore
    fontsize2 = min(int(150 / len(str(highscore))), 100)
    number_font2 = pygame.font.Font(None, fontsize2)
    textcentering2 = gamedimension + extra_space / 2 - (6 / 35 * fontsize2 * len(str(highscore)))
    hightext = number_font2.render(str(highscore), True, c.black)
    screen.blit(hightext, (textcentering2, 475))
    highscoretext = base_font.render('Highscore:', True, c.black)
    screen.blit(highscoretext, (gamedimension + 65, 450))

    # code for latestscore
    fontsize3 = min(int(150 / len(str(points_earned))), 100)
    number_font3 = pygame.font.Font(None, fontsize3)
    textcentering3 = gamedimension + extra_space / 2 - (6 / 35 * fontsize3 * len(str(points_earned))) +15
    latesttext = number_font3.render(str(points_earned), True, c.black)
    screen.blit(latesttext, (textcentering3, 550))
    latestpointstext = base_font.render('Last Score:', True, c.black)
    screen.blit(latestpointstext, (gamedimension + 65, 525))

    # code for timer
    timerfont = pygame.font.Font(None, 50)
    timertext = base_font.render('Time:', True, c.black)
    screen.blit(timertext, (gamedimension + 80, 375))
    timernumbs = timerfont.render(str(timer.time())[:7], True, c.black)
    screen.blit(timernumbs, (gamedimension + 50, 400))

    # Flip screen? apparently this is necessary
    pygame.display.flip()

    if (character.ymaze, character.xmaze) == (len(maze) , endcell + 1):
        points_earned = (len(maze)*len(maze[0]))//max(timer.time_in_secs(), 1)
        if highscore < points_earned:
            highscore = points_earned
        maze_points += points_earned
        allspriteslist, celldimensions, character, maze, startcell, endcell = create_a_maze(gamedimension, int(inputx), int(inputy))
        timer.reset()

    # Pause
    clock.tick(100)
