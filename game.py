class Game:
    def __init__(self):
        import pygame
        from cellclasses import Character
        import colors as c
        from gamefunctions import MazeVisual, SolvingAlgorithm
        from timer import Timer

        # pg code!
        pygame.init()
        # create the screen
        self.gamedimension = 600
        extra_space = 200
        screenwidth = self.gamedimension + extra_space
        self.screen = pygame.display.set_mode((screenwidth, self.gamedimension + 50))  # input dimensions of the game
        image = pygame.image.load('mazeimage.jpg')
        self.screen.fill(c.white)  # sets the background color
        pygame.display.set_caption('Maze Game!')  # This is the window of the game
        pygame.display.set_icon(image)
        inputx = '50'
        inputy = '50'
        newmaze = MazeVisual(self.gamedimension, int(inputx), int(inputy))
        character = newmaze.create_a_maze()
        self.points_earned = ' '
        cells = pygame.sprite.Group()
        solved = False

        with open('mazepoints.txt', 'r+') as f:
            maze_points = int(f.readline())
            highscore = int(f.readline())

        # initialize sizing and location of buttons and text boxes
        base_font = pygame.font.Font(None, 25)

        xdimensions_rect = pygame.Rect(self.gamedimension + extra_space / 2 - 50, 50, 100, 20)
        ydimensions_rect = pygame.Rect(self.gamedimension + extra_space / 2 - 50, 100, 100, 20)
        create_new_maze = pygame.Rect(self.gamedimension + extra_space / 2 - 50, 150, 100, 50)
        solve_the_maze = pygame.Rect(self.gamedimension + extra_space / 2 - 50, 225, 100, 50)

        self.clock = pygame.time.Clock()
        running = True
        inxtextbox = False
        inytextbox = False
        timer = Timer()

        while running:
            # keep running this code until the game is quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('mazepoints.txt', 'w') as f:
                        f.write(str(maze_points))
                        f.write('\n')
                        f.write(str(highscore))
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        character.move('left', newmaze.maze)
                    if event.key == pygame.K_RIGHT:
                        character.move('right', newmaze.maze)
                    if event.key == pygame.K_UP:
                        character.move('up', newmaze.maze)
                    if event.key == pygame.K_DOWN:
                        character.move('down', newmaze.maze)
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
                # if the player clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if xdimensions_rect.collidepoint(event.pos):
                        inxtextbox = True  # change to entering in text box
                    else:
                        inxtextbox = False
                    if ydimensions_rect.collidepoint(event.pos):
                        inytextbox = True
                    else:
                        inytextbox = False
                    if create_new_maze.collidepoint(event.pos):  # if user clicks new maze
                        if int(inputx) < 3:
                            inputx = '3'
                        if int(inputy) < 3:
                            inputy = '3'
                        newmaze = MazeVisual(self.gamedimension, int(inputx), int(inputy))
                        character = newmaze.create_a_maze()
                        timer.reset()
                        cells.empty()
                        solved = False
                    if solve_the_maze.collidepoint(event.pos):
                        if not solved:
                            solvealgo = SolvingAlgorithm(newmaze.maze, (0, newmaze.startcell), (len(newmaze.maze) - 1, newmaze.endcell))
                            (solved, cells) = solvealgo.solve_maze(self.screen, newmaze.maze, newmaze.celldimensions, (0, newmaze.startcell),
                                                                   (len(newmaze.maze) - 1, newmaze.endcell), self.clock, solvealgo)

            newmaze.allspriteslist.remove(character)
            character = Character(c.blue, character.xmaze, character.ymaze, newmaze.celldimensions)
            newmaze.allspriteslist.add(character)

            # -- Draw everything
            # Clear screen
            self.screen.fill(c.white)
            newmaze.allspriteslist.draw(self.screen)
            if 'cells' in locals():
                cells.draw(self.screen)

            # code for boxes
            # textbox for x dimension
            pygame.draw.rect(self.screen, pygame.Color('gray'), xdimensions_rect)
            xdimbox = base_font.render(inputx, True, (255, 255, 255))
            self.screen.blit(xdimbox, (xdimensions_rect.x + 5, xdimensions_rect.y + 3))
            xdimensions_rect.w = max(100, xdimbox.get_width() + 10)

            # textbox for y dimension
            pygame.draw.rect(self.screen, pygame.Color('gray'), ydimensions_rect)
            ydimbox = base_font.render(inputy, True, (255, 255, 255))
            self.screen.blit(ydimbox, (ydimensions_rect.x + 5, ydimensions_rect.y + 3))
            ydimensions_rect.w = max(100, ydimbox.get_width() + 10)

            # button for creating a new maze
            pygame.draw.rect(self.screen, c.lightgreen, create_new_maze)
            createtext = base_font.render('NEW MAZE', True, c.black)
            self.screen.blit(createtext, (create_new_maze.x + 5, create_new_maze.y + 15))

            # button for solving the maze
            pygame.draw.rect(self.screen, pygame.Color('yellow'), solve_the_maze)
            createtext2 = base_font.render('SOLVE', True, c.black)
            self.screen.blit(createtext2, (solve_the_maze.x + 25, solve_the_maze.y + 15))

            # code for text
            # text for x dimension
            xdimension = base_font.render('Width:', True, c.black)
            self.screen.blit(xdimension, (xdimensions_rect.x + 5, xdimensions_rect.y - 20))

            # text for y dimension
            ydimension = base_font.render('Height:', True, c.black)
            self.screen.blit(ydimension, (ydimensions_rect.x + 5, ydimensions_rect.y - 20))

            # code for maze points
            fontsize = min(int(300 / len(str(maze_points))), 75)
            number_font = pygame.font.Font(None, fontsize)
            textcentering = self.gamedimension + extra_space / 2 - (6 / 35 * fontsize * len(str(maze_points)))
            mazetext = number_font.render(str(maze_points), True, c.black)
            self.screen.blit(mazetext, (textcentering, 320))
            mazepointstext = base_font.render('Points:', True, c.black)
            self.screen.blit(mazepointstext, (self.gamedimension + 75, 300))

            # code for highscore
            fontsize2 = min(int(150 / len(str(highscore))), 75)
            number_font2 = pygame.font.Font(None, fontsize2)
            textcentering2 = self.gamedimension + extra_space / 2 - (6 / 35 * fontsize2 * len(str(highscore)))
            hightext = number_font2.render(str(highscore), True, c.black)
            self.screen.blit(hightext, (textcentering2, 475))
            highscoretext = base_font.render('Highscore:', True, c.black)
            self.screen.blit(highscoretext, (self.gamedimension + 65, 450))

            # code for latestscore
            fontsize3 = min(int(150 / len(str(self.points_earned))), 100)
            number_font3 = pygame.font.Font(None, fontsize3)
            textcentering3 = self.gamedimension + extra_space / 2 - (6 / 35 * fontsize3 * len(str(self.points_earned)))
            latesttext = number_font3.render(str(self.points_earned), True, c.black)
            self.screen.blit(latesttext, (textcentering3, 550))
            latestpointstext = base_font.render('Last Score:', True, c.black)
            self.screen.blit(latestpointstext, (self.gamedimension + 60, 525))

            # code for timer
            timerfont = pygame.font.Font(None, 50)
            timertext = base_font.render('Time:', True, c.black)
            self.screen.blit(timertext, (self.gamedimension + 80, 375))
            timernumbs = timerfont.render(str(timer.time())[:7], True, c.black)
            self.screen.blit(timernumbs, (self.gamedimension + 50, 400))

            # Flip screen? apparently this is necessary
            pygame.display.flip()

            if (character.ymaze, character.xmaze) == (len(newmaze.maze), newmaze.endcell + 1):
                self.points_earned = (len(newmaze.maze) * len(newmaze.maze[0])) // max(timer.time_in_secs(), 1)
                if highscore < self.points_earned:
                    highscore = self.points_earned
                maze_points += self.points_earned
                newmaze = MazeVisual(self.gamedimension, int(inputx), int(inputy))
                character = newmaze.create_a_maze()
                timer.reset()
                cells.empty()
                solved = False

            # Pause
            self.clock.tick(100)
