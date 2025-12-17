import pygame
from Tools.colours import Colours
from Objects.button import ButtonImg
from Objects.button import Button
from Objects.box import draw_box
from Tools.scale import size, pos
from MazeAlgorithms.RDFS import MazeGenerator

def draw_objects(window, width, height, font, mazeSize, sizeBorderColour, themeBorderColour):
    
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)
    
    gen_w, gen_h = size(width, height, 36, 11)
    gen_x, gen_y = pos(width, height, 78.7, 14.5, gen_w, gen_h)
    gen = Button(font, "        Generate", Colours.BLUE, "white", gen_x, gen_y, gen_w, gen_h, Colours.GREY, Colours.GREY, 50)
    
    size_w, size_h = size(width, height, 26, 6)
    size_x, size_y = pos(width, height, 28, 15, size_w, size_h)
    maze_size = Button(font, f"Size : {mazeSize}", Colours.BLUE, "white", size_x, size_y, size_w, size_h, (sizeBorderColour), Colours.GREY, 0)
    
    theme_w, theme_h = size(width, height, 17, 6)
    theme_x, theme_y = pos(width, height, 51, 15, theme_w, theme_h)
    theme = Button(font, " Theme", Colours.BLUE, "white", theme_x, theme_y, theme_w, theme_h, (themeBorderColour), Colours.GREY, 0)

    back.draw_image(window, width, height)
    gen.draw_button(window)
    maze_size.draw_button(window)
    theme.draw_button(window)
    
    return back, gen, maze_size, theme

def gen_maze(window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour):
     # Initialise the maze generator attributes and methods
    maze = MazeGenerator(window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour)
    return maze # run one step of the maze generation proccess

class Generate:
    def __init__(self, window, GameStateManager, width, height, font, sound):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width, self.height = width, height
        self.maze_w, self.maze_h = width - 35 * 2, height - 100 * 2 # Maze size relative to screen
        self.maze_x, self.maze_y = pos(width, height, 5, 32.2, 35, 100) # Where the maze is positioned
        self.font = font
        self.sound = sound
        self.size = 40 # The default size of each cell
        self.x, self.y = 0, 0 # Starting coordinates
        self.sizeBorderColour = Colours.GREEN
        self.themeBorderColour = Colours.GREY
        self.visitColour = Colours.LIGHTGREY
        self.wallColour = Colours.GREY
        self.currentColour = Colours.BLUE
        self.mazeSize = "Small" # Default maze size
        self.generate = False 
        self.maze_generated = False
        self.maze = None
        self.theme = "Original"
        self.mazeColour = Colours.LIGHTGREY
        
    def run(self):
        draw_box(self.window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        
        self.back_button, self.gen_button, self.maze_size_button, self.theme_button = draw_objects(self.window, self.width, self.height, self.font, self.mazeSize, self.sizeBorderColour, self.themeBorderColour)
        
        pos = pygame.mouse.get_pos()

        self.back_button.img_hover(pos)
        self.gen_button.button_hover(pos)
        self.maze_size_button.button_hover(pos)
        self.theme_button.button_hover(pos)
        
        self.back_button.draw_image(self.window, self.width, self.height)
        self.gen_button.draw_button(self.window)
        self.maze_size_button.draw_button(self.window)
        self.theme_button.draw_button(self.window)
        
        self.clicked = self.back_button.img_click(pos)
        
        if self.maze_generated and self.maze: # If a maze has been generated
            self.maze.run() # Keep drawing the maze that has already been generated
        elif self.generate: # If a maze needs to be generated
            # Create a new maze
            self.maze = gen_maze(self.window, self.maze_w, self.maze_h, self.size, self.visitColour, self.wallColour, self.x, self.y, self.currentColour, self.maze_x, self.maze_y, self.mazeColour)
            self.maze.run()
            self.maze_generated = True # The maze has now been generated
            self.generate = False # No longer generate a new maze
        
    def click(self, pos):
        if self.clicked:
            self.sound.play_click()
            self.reset_maze()
            self.GameStateManager.set_state("menuPlay")
        elif self.gen_button.rect.collidepoint(pos):
            self.sound.play_click()
            self.reset_maze() # Clear any previous maze
            self.generate = True # Set the generate value to True to start the generation process
        elif self.maze_size_button.rect.collidepoint(pos):
            self.sound.play_click()
            # For each click of the button, the size text, border colour and maze size will change
            # Each state of the button makes the maze density greater by changing the size variable to be smaller
            # The button will cycle through each size in a circle for every click.
            if self.mazeSize == "Small":
                self.size = 35
                self.mazeSize = "Medium"
                self.sizeBorderColour = Colours.ORANGE
            elif self.mazeSize == "Medium":
                self.size = 25
                self.mazeSize = "Large"
                self.sizeBorderColour = Colours.RED
            elif self.mazeSize == "Large":
                self.size = 40
                self.mazeSize = "Small"
                self.sizeBorderColour = Colours.GREEN
        elif self.theme_button.rect.collidepoint(pos):
            self.sound.play_click()
            # For each click of the button, both the border colour and theme will change
            # Each theme will change the background, border, visited, and leading cell of the maze generation
            # The button will cycle through each theme in a circle when clicked
            if self.theme == "Original":
                self.themeBorderColour = Colours.BLACK
                self.theme = "Dark"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.WHITE, Colours.BLACK, Colours.BLUE
            elif self.theme == "Dark":
                self.themeBorderColour = Colours.WHITE
                self.theme = "Light"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.BLACK, Colours.WHITE, Colours.BLUE
            elif self.theme == "Light":
                self.themeBorderColour = Colours.NEONRED
                self.theme = "Red and black"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.WHITE, Colours.BLOODRED, Colours.NEONBLUE
            elif self.theme == "Red and black":
                self.themeBorderColour = Colours.NEONPINK
                self.theme = "Neon pink"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.NEONBLUE, Colours.NEONPINK, Colours.NEONYELLOW
            elif self.theme == "Neon pink":
                self.themeBorderColour = Colours.NEONBLUE
                self.theme = "Neon blue"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.NEONYELLOW, Colours.NEONBLUE, Colours.NEONPINK
            elif self.theme == "Neon blue":
                self.themeBorderColour = Colours.NEONYELLOW
                self.theme = "Neon yellow"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.NEONGREEN, Colours.NEONYELLOW, Colours.NEONBLUE
            elif self.theme == "Neon yellow":
                self.themeBorderColour = Colours.GREY
                self.theme = "Inverted"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.GREY, Colours.LIGHTGREY, Colours.NEONRED
            elif self.theme == "Inverted":
                self.themeBorderColour = Colours.GREY
                self.theme = "Original"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.LIGHTGREY, Colours.LIGHTGREY, Colours.GREY, Colours.BLUE
            
    def reset_maze(self):
        # Clear the previouos maze when leaving menu or resetting
        self.maze = None # Remove any current maze object
        self.maze_generated = False # Prevent a maze from being generated
        self.generate = False # Stop generating a maze