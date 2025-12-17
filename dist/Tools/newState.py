import pygame
from Tools.colours import Colours
from Objects.button import ButtonImg
from Objects.box import draw_box
from Tools.scale import size, pos

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)

    back.draw_image(window, width, height)
    
    return back

class Generate:
    def __init__(self, window, GameStateManager, width, height, font, sound):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.sound = sound
        
    def run(self):
        self.back_button = draw_objects(self.window, self.width, self.height, self.font)
        
        pos = pygame.mouse.get_pos()

        self.back_button.img_hover(pos)
        
        self.back_button.draw_image(self.window, self.width, self.height)
        
        self.clicked = self.back_button.img_click(pos)
        
    def click(self):
        if self.clicked:
            self.sound.play_click()
            self.GameStateManager.set_state("menuPlay")