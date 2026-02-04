import pygame
from Tools.colours import Colours
from Objects.button import ButtonImg
from Objects.button import Button
from Objects.box import draw_box
from Tools.scale import size, pos
from MazeAlgorithms.RDFS import MazeGenerator

def draw_objects(window, width, height, font, mazeSize, sizeBorderColour, themeBorderColour, themeText, speedBorderColour, speedText, pauseText, pauseBorderColour, pauseBgColour, solveBgColour):
    
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)
    
    gen_w, gen_h = size(width, height, 24, 6)
    gen_x, gen_y = pos(width, height, 85.6, 8, gen_w, gen_h)
    gen = Button(font, "   Generate", Colours.GOGREEN, "white", gen_x, gen_y, gen_w, gen_h, Colours.GREY, Colours.GREY, 50)
    
    pause_w, pause_h = size(width, height, 24, 6)
    pause_x, pause_y = pos(width, height, 85.6, 19.5, pause_w, pause_h)
    pause = Button(font, f"      {pauseText}", (pauseBgColour), "white", pause_x, pause_y, pause_w, pause_h, (pauseBorderColour), Colours.GREY, 50)
    
    solve_w, solve_h = size(width, height, 24, 6)
    solve_x, solve_y = pos(width, height, 60.5, 19.5, solve_w, solve_h)
    solve = Button(font, "       Solve", (solveBgColour), "white", solve_x, solve_y, solve_w, solve_h, Colours.GREY, Colours.GREY, 50)
    
    size_w, size_h = size(width, height, 29.5, 6)
    size_x, size_y = pos(width, height, 32.5, 19.5, size_w, size_h)
    maze_size = Button(font, f"Size : {mazeSize}", Colours.BLUE, "white", size_x, size_y, size_w, size_h, (sizeBorderColour), Colours.GREY, 0)
    
    theme_w, theme_h = size(width, height, 29.5, 6)
    theme_x, theme_y = pos(width, height, 32.5, 8, theme_w, theme_h)
    theme = Button(font, f"Theme : {themeText}", Colours.BLUE, "white", theme_x, theme_y, theme_w, theme_h, (themeBorderColour), Colours.GREY, 0)
    
    speed_w, speed_h = size(width, height, 24, 6)
    speed_x, speed_y = pos(width, height, 60.5, 8, speed_w, speed_h)
    speed = Button(font, f"Speed : {speedText}", Colours.BLUE, "white", speed_x, speed_y, speed_w, speed_h, (speedBorderColour), Colours.GREY, 0)
    
    # pause_w, pause_h = size(width, height, 24, 6)
    # pause_x, pause_y = pos(width, height, 85.6, 16, pause_w, pause_h)
    # pause = Button(font, "Pause/Play", Colours.BLUE, "white", pause_x, pause_y, pause_w, pause_h, Colours.GREY, Colours.GREY, 50)
    
    return back, gen, maze_size, theme, speed, pause, solve

def gen_maze(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour):
     # Initialise the maze generator attributes and methods
    maze = MazeGenerator(window, GameStateManager, width, height,  size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour)
    return maze # run one step of the maze generation process

def gen_grid(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour):
     # Initialise the maze generator attributes and methods
    grid = MazeGenerator(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour)
    return grid # run one step of the maze generation process

class Generate:
    def __init__(self, window, GameStateManager, fps, width, height, font, sound):
        self.window = window
        self.GameStateManager = GameStateManager
        self.fps = fps
        self.width, self.height = width, height
        self.maze_w, self.maze_h = width - 35 * 2, height - 100 * 2 # Maze size relative to screen
        self.maze_x, self.maze_y = pos(width, height, 5, 32.2, 35, 100) # Where the maze is positioned
        self.font = font
        self.sound = sound
        self.size = 40 # The default size of each cell
        self.x, self.y = 0, 0 # Starting coordinates
        self.sizeBorderColour = Colours.GREEN
        self.themeBorderColour = Colours.GREY
        self.speedBorderColour = Colours.RED
        self.visitColour = Colours.LIGHTGREY
        self.wallColour = Colours.GREY
        self.currentColour = Colours.BLUE
        self.mazeSize = "   Small" # Default maze size
        self.generate = False 
        self.maze_generated = False
        self.maze = None
        self.theme = "Original"
        self.mazeColour = Colours.LIGHTGREY
        self.scale = 3.5
        self.fin_x, self.fin_y = 96.7, 93.1
        self.themeText = "Classic"
        self.speedText = "Fast"
        self.pauseText = "Pause"
        self.paused = False
        self.pauseBorderColour = Colours.GREEN
        self.pauseBgColour = Colours.GREY
        self.solveBgColour = Colours.GREY
        self.solutionColour = Colours.BLUE
        
    def run(self):
        draw_box(self.window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        
        self.back_button, self.gen_button, self.maze_size_button, self.theme_button, self.speed_button, self.pause_button, self.solve_button = draw_objects(self.window, self.width, self.height, self.font, self.mazeSize, self.sizeBorderColour, self.themeBorderColour, self.themeText, self.speedBorderColour, self.speedText, self.pauseText, self.pauseBorderColour, self.pauseBgColour, self.solveBgColour)
        
        pos = pygame.mouse.get_pos()
        
        self.back_button.img_hover(pos)
        self.pause_button.button_hover(pos)
        self.solve_button.button_hover(pos)
        self.gen_button.button_hover(pos)
        self.maze_size_button.button_hover(pos)
        self.theme_button.button_hover(pos)
        self.speed_button.button_hover(pos)

        self.back_button.draw_image(self.window)
        self.pause_button.draw_button(self.window)
        self.solve_button.draw_button(self.window)
        self.gen_button.draw_button(self.window)
        self.maze_size_button.draw_button(self.window)
        self.theme_button.draw_button(self.window)
        self.speed_button.draw_button(self.window)
        
        self.back_clicked = self.back_button.img_click(pos)
        
        if not self.paused:
            if self.maze_generated and self.maze: # If a maze has been generated
                self.maze.run() # Keep drawing the maze that has already been generated
            elif self.generate: # If a maze needs to be generated
                # Create a new maze
                self.maze = gen_maze(self.window, self.GameStateManager, self.maze_w, self.maze_h, self.size, self.visitColour, self.wallColour, self.x, self.y, self.currentColour, self.maze_x, self.maze_y, self.mazeColour, self.scale, self.fin_x, self.fin_y, self.solutionColour)
                self.maze.run()
                self.maze_generated = True # The maze has now been generated
                self.generate = False # No longer generate a new maze
            
        elif self.maze and self.paused: # If there is a maze and it is paused, draw the current maze state with current cell
            self.maze.draw_grid()
            self.maze.draw_current()
            self.maze.redraw() # Redraw the checkered box
            
        if self.maze is None: # If there is no maze drawn
            # Create an empty grid (Updates each cycle to keep up with any changes made)
            self.grid = gen_grid(self.window, self.GameStateManager, self.maze_w, self.maze_h, self.size, self.visitColour, self.wallColour, self.x, self.y, self.currentColour, self.maze_x, self.maze_y, self.mazeColour, self.scale, self.fin_x, self.fin_y, self.solutionColour)
            self.grid.draw_grid() # Draw the empty grid
            self.pauseBgColour = Colours.GREY # Change the bg colour of the button to grey to signify not being clickable
            self.solveColour = Colours.GREY
            
        if self.maze:
            if self.maze.done():
                self.solveBgColour = Colours.BLUE
                
            if self.maze.find_solution:
                self.solveBgColour = Colours.GREY

    def click(self, pos):
        if self.back_clicked:
            self.sound.play_click()
            self.reset_maze()
            self.fps.new_fps(60)
            self.GameStateManager.set_state("menuPlay")
            self.speedBorderColour = Colours.RED
            self.speedText = "Fast"
            self.pauseText = "Pause"
            self.pauseBorderColour = Colours.GREEN
            
        elif self.pause_button.rect.collidepoint(pos):
            self.sound.play_click()
            if self.pauseText == "Pause" and self.maze: # If currently generating and there is a maze then pause it and change button
                self.pauseText = "  Play"
                self.pauseBorderColour = Colours.RED
                self.paused = True
            elif self.pauseText == "  Play" and self.maze: # If not currently generating then play it and change button
                self.pauseText = "Pause"
                self.pauseBorderColour = Colours.GREEN
                self.paused = False
            
        elif self.gen_button.rect.collidepoint(pos):
            self.sound.play_click()
            self.reset_maze() # Clear any previous maze
            if self.mazeSize == "   Small":
                self.scale = 3.1
            elif self.mazeSize == " Medium":
                self.scale = 2.65
            elif self.mazeSize == "   Large":
                self.scale = 1.9
            self.paused = False
            self.pauseText = "Pause"
            self.pauseBorderColour = Colours.GREEN
            self.pauseBgColour = Colours.BLUE
            self.solveBgColour = Colours.GREY
            self.generate = True # Set the generate value to True to start the generation process
            
        elif self.maze_size_button.rect.collidepoint(pos):
            self.sound.play_click()
            # For each click of the button, the size text, border colour and maze size will change
            # Each state of the button makes the maze density greater by changing the size variable to be smaller
            # The button will cycle through each size in a circle for every click.
            if self.mazeSize == "   Small":
                self.size = 35
                self.scale = 2.65
                self.mazeSize = " Medium"
                self.sizeBorderColour = Colours.ORANGE
            elif self.mazeSize == " Medium":
                self.size = 25
                self.scale = 1.9
                self.mazeSize = "   Large"
                self.sizeBorderColour = Colours.RED
            elif self.mazeSize == "   Large":
                self.size = 40
                self.scale = 3.1
                self.mazeSize = "   Small"
                self.sizeBorderColour = Colours.GREEN
                
            self.maze = None
            self.paused = False
            self.pauseText = "Pause"
            self.pauseBorderColour = Colours.GREEN
            self.pauseBgColour = Colours.GREY
            self.solveBgColour = Colours.GREY
            self.maze = None
            
        elif self.solve_button.rect.collidepoint(pos):
            if self.maze and self.maze.done(): # If there is a maze and it has finished solving
                self.sound.play_click()
                self.maze.find_solution = True # Allow the solution path to be drawn

        elif self.theme_button.rect.collidepoint(pos):
            self.sound.play_click()
            if self.mazeSize == "   Small":
                self.scale = 3.1
            elif self.mazeSize == " Medium":
                self.scale = 2.65
            elif self.mazeSize == "   Large":
                self.scale = 1.9
                
            self.maze = None
            self.paused = False
            self.pauseText = "Pause"
            self.pauseBorderColour = Colours.GREEN
            self.pauseBgColour = Colours.GREY
            self.solveBgColour = Colours.GREY
            self.maze = None
            # For each click of the button, both the border colour and theme will change
            # Each theme will change the background, border, visited, and leading cell of the maze generation
            # The button will cycle through each theme in a circle when clicked
            if self.theme == "Original":
                self.themeBorderColour = Colours.WHITE
                self.theme = "Light"
                self.themeText = "Light"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.WHITE, Colours.BLACK, Colours.BLUE
                self.solutionColour = self.currentColour
            elif self.theme == "Light":
                self.themeBorderColour = Colours.BLACK
                self.theme = "Dark"
                self.themeText = "Dark"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.BLACK, Colours.WHITE, Colours.BLUE
                self.solutionColour = self.currentColour
            elif self.theme == "Dark":
                self.themeBorderColour = Colours.RED
                self.theme = "Red and black"
                self.themeText = "Red"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.RED, Colours.NEONBLUE, Colours.NEONGREEN
                self.solutionColour = self.currentColour
            elif self.theme == "Red and black":
                self.themeBorderColour = Colours.LIGHTPINK
                self.theme = "Neon pink"
                self.themeText = "Pink" 
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.LIGHTPINK, Colours.WHITE, Colours.NEONYELLOW
                self.solutionColour = self.currentColour
            elif self.theme == "Neon pink":
                self.themeBorderColour = Colours.NEONYELLOW
                self.theme = "Neon blue"
                self.themeText = "Yellow"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.NEONYELLOW, Colours.NEONBLUE, Colours.NEONPINK
                self.solutionColour = self.currentColour
            elif self.theme == "Neon blue":
                self.themeBorderColour = Colours.GOLD
                self.theme = "Gold"
                self.themeText = "Gold"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.BLACK, Colours.GOLD, Colours.BLOODRED
                self.solutionColour = self.currentColour
            elif self.theme == "Gold":
                self.themeBorderColour = Colours.NEONBLUE
                self.theme = "Blue"
                self.themeText = "Blue"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.BLUE, Colours.NEONPINK, Colours.NEONORANGE
                self.solutionColour = self.currentColour
            elif self.theme == "Blue":
                self.themeBorderColour = Colours.RED
                self.theme = "Inverted"
                self.themeText = "Inverse"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.GREY, Colours.WHITE, Colours.RED
                self.solutionColour = self.currentColour
            elif self.theme == "Inverted":
                self.themeBorderColour = Colours.GREY
                self.theme = "Original"
                self.themeText = "Classic"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.LIGHTGREY, Colours.LIGHTGREY, Colours.GREY, Colours.BLUE
                self.solutionColour = self.currentColour
            
            self.solveBgColour = Colours.GREY
        
        elif self.speed_button.rect.collidepoint(pos):
            self.sound.play_click()
            if self.speedText == "Mid":
                self.fps.new_fps(200) # Change the speed to 200
                self.speedBorderColour = Colours.RED
                self.speedText = "Fast"
            elif self.speedText == "Fast":
                self.fps.new_fps(10) # Change the speed to 10
                self.speedBorderColour = Colours.GREEN
                self.speedText = "Slow"
            elif self.speedText == "Slow":
                self.fps.new_fps(30) # Change the speed to 30
                self.speedBorderColour = Colours.ORANGE
                self.speedText = "Mid"
            
    def reset_maze(self):
        # Clear the previouos maze when leaving menu or resetting
        self.maze = None # Remove any current maze object
        self.maze_generated = False # Prevent a maze from being generated
        self.generate = False # Stop generating a maze