import pygame
from Tools.colours import Colours
from Objects.button import Button
from Objects.image import Image
from Tools.scale import pos, size
from Objects.box import draw_box
from Objects.text import draw_text
import time

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    draw_text(window, "Maze Craze", Colours.GREY, font, 20, 23, width, height)
    
    # Initiating all properties of each button for the main menu
    play_w, play_h = size(width, height, 9, 5.5)
    play_x, play_y = pos(width, height, 14.8, 38, play_w, play_h)
    play = Button(font, "Play", Colours.BLUE, "white", play_x, play_y , play_w, play_h, Colours.GREY, Colours.GREY)
    
    settings_w, settings_h = size(width, height, 16, 5.5)
    settings_x, plasettings_y = pos(width, height, 18.3, 50, settings_w, settings_h)
    settings = Button(font, "Settings", Colours.BLUE, "white", settings_x, plasettings_y, settings_w, settings_h, Colours.GREY, Colours.GREY)
    
    quit_w, quit_h = size(width, height, 9.5, 5.5)
    quit_x, quit_y = pos(width, height, 15, 62, quit_w, quit_h)
    quit = Button(font, "Quit", Colours.BLUE, "white", quit_x, quit_y, quit_w, quit_h, Colours.GREY, Colours.GREY)
    
    menuImg_w, menuImg_h = size(width, height, 50, 50)
    menuImg_x, menuImg_y = pos(width, height, 70, 50, menuImg_w, menuImg_h)
    menuImg = Image("logo.png", menuImg_x, menuImg_y, menuImg_w, menuImg_h) # Initiating all the properties for the main menu image

    # Make the buttons by blitting them to the window
    play.draw_button(window) 
    settings.draw_button(window)
    quit.draw_button(window)
    
    menuImg.draw_image(window) # Blit the image to the window
    
    return play, settings, quit

class Menu:
    def __init__(self, window, GameStateManager, width, height, font, clickSFX):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.clickSFX = clickSFX
        
    def run(self):
        self.play_button, self.settings_button, self.quit_button = draw_objects(self.window, self.width, self.height, self.font)
        
        pos = pygame.mouse.get_pos()

        # Check if a button is hovered over and change the background colour of the button 
        self.play_button.button_hover(pos)
        self.settings_button.button_hover(pos)
        self.quit_button.button_hover(pos)

        # Redraw buttons with hover effect
        self.play_button.draw_button(self.window)
        self.settings_button.draw_button(self.window)
        self.quit_button.draw_button(self.window)
        
    def click(self, pos):
        if self.quit_button.rect.collidepoint(pos):
            self.clickSFX.play()
            time.sleep(0.22)
            pygame.quit()
            exit()
        elif self.settings_button.rect.collidepoint(pos):
            self.clickSFX.play()
            self.GameStateManager.set_state("menuSettings")
        elif self.play_button.rect.collidepoint(pos):
            self.clickSFX.play()
            self.GameStateManager.set_state("menuPlay")