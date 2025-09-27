import pygame
from colours import Colours
from objects.button import Button

def draw_objects(window, width, height, font):
    # Initiating all properties of each button for the main menu
    play = Button(font, "Play", Colours.BLUE, "white", 20, 30, 400, 80, "white", Colours.GREY)
    settings = Button(font, "Settings", Colours.BLUE, "white",  20, 150, 400, 80, "white", Colours.GREY)
    quit = Button(font, "Quit", Colours.BLUE, "white", 20, 330, 400, 80, "white", Colours.GREY)

    play.draw_button(window)
    settings.draw_button(window)
    quit.draw_button(window)
    
    return play, settings, quit

class Menu:
    def __init__(self, window, GameStateManager, width, height, font):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        
    def run(self):        
        self.window.fill(Colours.LIGHTGREY) # Background colour of the program and cover up old objects
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
            pygame.quit()
            exit()
        elif self.settings_button.rect.collidepoint(pos):
            self.GameStateManager.set_state("menuSettings")
        elif self.play_button.rect.collidepoint(pos):
            self.GameStateManager.set_state("menuPlay")