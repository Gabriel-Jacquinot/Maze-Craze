import pygame
from colours import Colours
from objects.button import Button, ButtonImg 

def draw_objects(window, width, height):
    back = ButtonImg("back1.png", 20, 30, "back2.png")
    # resolution = Slider(font, "Play", (112, 137, 156), "white", 20, 30, 400, 80, "white", (180, 103, 120))
    #  = Button(font, "Settings", (112, 137, 156), "white",  20, 150, 400, 80, "white", (180, 103, 120))

    back.draw_image(window)
    
    return back

class Settings:
    def __init__(self, window, GameStateManager, width, height, font):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        
    def run(self):
        self.window.fill(Colours.LIGHTGREY) # Cover up old objects
        self.back_button = draw_objects(self.window, self.width, self.height)
        
        pos = pygame.mouse.get_pos()
        
        self.back_button.img_hover(pos, self.window)
        
        self.back_button.draw_image(self.window)
        
        self.clicked = self.back_button.img_click(pos)
        
    def click(self):
        if self.clicked:
            self.GameStateManager.set_state("menuMain")