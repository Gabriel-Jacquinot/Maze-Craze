import pygame
from Tools.colours import Colours
from Objects.button import Button, ButtonImg
from Objects.box import draw_box
from Tools.scale import size, pos
# from Objects.slider import Slider
# from Objects.text import draw_text

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)
    
    sound_w, sound_h = size(width, height, 25, 5.5)
    sound_x, sound_y = pos(width, height, 50, 20, sound_w, sound_h)
    sound = Button(font, "Sound Effects", Colours.BLUE, "white", sound_x, sound_y , sound_w, sound_h, Colours.GREY, Colours.GREY, 0)
    
    # SFX_w, SFX_h = size(width, height, 20, 5)
    # SFX_x, SFX_y = pos(width, height, 50, 27, SFX_w, SFX_h)
    # volumeSFX = Slider(SFX_x, SFX_y, SFX_w, SFX_h, Colours.BLUE, Colours.GREY, 0, 100)
    # draw_text(window, str(volumeSFX), Colours.GREY, font, 20, 25, width, height)

    back.draw_image(window, width, height)
    sound.draw_button(window)

    # volumeSFXSlider = volumeSFX.draw_slider(window)
    
    # volumeSFX.slide(window, width, volumeSFXSlider)
    
    return back, sound

class Settings:
    def __init__(self, window, GameStateManager, width, height, font, clickSFX):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.clickSFX = clickSFX
        
    def run(self):
        self.back_button, self.sound_button = draw_objects(self.window, self.width, self.height, self.font, )
        
        pos = pygame.mouse.get_pos()

        self.back_button.img_hover(pos)
        self.sound_button.button_hover(pos)
        
        self.back_button.draw_image(self.window, self.width, self.height)
        self.sound_button.draw_button(self.window)
        
        self.clicked = self.back_button.img_click(pos)
        
    def click(self, pos):
        if self.clicked:
            self.clickSFX.play()
            self.GameStateManager.set_state("menuMain")
        elif self.sound_button.rect.collidepoint(pos):
            if pygame.mixer.Sound.get_volume(self.clickSFX) > 0:
                pygame.mixer.Sound.set_volume(self.clickSFX, 0)
            else:
                pygame.mixer.Sound.set_volume(self.clickSFX, 100)
            self.clickSFX.play()
            