import pygame
from Tools.colours import Colours
from Objects.button import ButtonImg
from Objects.button import Button
from Objects.box import draw_box
from Tools.scale import size, pos
from MazeAlgorithms.RDFS import MazeGenerator

def draw_objects(window, width, height, font):
    
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)
    
    gen_w, gen_h = size(width, height, 36, 11)
    gen_x, gen_y = pos(width, height, 78.7, 15, gen_w, gen_h)
    gen = Button(font, "        Generate", Colours.BLUE, "white", gen_x, gen_y, gen_w, gen_h, Colours.GREY, Colours.GREY, 50)
    
    size_w, size_h = size(width, height, 17, 8)
    size_x, size_y = pos(width, height, 27, 15, size_w, size_h)
    maze_size = Button(font, "    Size", Colours.BLUE, "white", size_x, size_y, size_w, size_h, Colours.GREY, Colours.GREY, 0)
    
    theme_w, theme_h = size(width, height, 17, 8)
    theme_x, theme_y = pos(width, height, 47, 15, theme_w, theme_h)
    theme = Button(font, " Theme", Colours.BLUE, "white", theme_x, theme_y, theme_w, theme_h, Colours.GREY, Colours.GREY, 0)

    back.draw_image(window, width, height)
    gen.draw_button(window)
    maze_size.draw_button(window)
    theme.draw_button(window)
    
    return back, gen, maze_size, theme

def gen_maze(window, width, height, size, visitColour, wallColour, x, y, currentColour):
    maze = MazeGenerator(window, width, height, size, visitColour, wallColour, x, y, currentColour)
    maze.run() # Whatever the make maze funtion is (unqiue to my program)

class Generate:
    def __init__(self, window, GameStateManager, width, height, font, sound):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width, self.height = width, height
        self.maze_w, self.maze_h = 35, 100
        self.maze_x, self.maze_y = pos(width, height, 5.6, 34, self.maze_w, self.maze_h) # Where the maze is positioned
        self.font = font
        self.sound = sound
        self.size = 50
        self.x, self.y = 0, 0
        self.vistColour = Colours.LIGHTGREY
        self.wallColour = Colours.GREY
        self.currentColour = Colours.BLUE
        self.generate = False
        self.maze_generated = False
        self.maze = None
        
    def run(self):
        draw_box(self.window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        
        self.back_button, self.gen_button, self.maze_size_button, self.theme_button = draw_objects(self.window, self.width, self.height, self.font)
        
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
        
        if self.maze_generated and self.maze:
            self.maze.run() 
        elif self.generate:
            self.maze = MazeGenerator(self.window, self.width - self.maze_w * 2, self.height - self.maze_h * 2, self.size, self.vistColour, self.wallColour, self.x, self.y, self.currentColour, self.maze_x, self.maze_y)
            self.maze.run()
            self.maze_generated = True
            self.generate = False
        
    def click(self, pos):
        if self.clicked:
            self.sound.play_click()
            self.reset_maze()
            self.GameStateManager.set_state("menuPlay")
        elif self.gen_button.rect.collidepoint(pos):
            self.sound.play_click()
            self.reset_maze()
            self.generate = True
        elif self.maze_size_button.rect.collidepoint(pos):
            self.sound.play_click()
            self.size = 25
        elif self.theme_button.rect.collidepoint(pos):
            self.sound.play_click()
            self.theme = 1
            
    def reset_maze(self):
        """Clear maze when leaving menu or resetting"""
        self.maze = None
        self.maze_generated = False
        self.generate = False