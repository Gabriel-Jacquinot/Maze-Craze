import pygame
from objects.button import Button

def draw_objects(window, width, height, font):
    # Initiating all properties of each button for the main menu
    play = Button(font, "Play", (112, 137, 156), "white", 20, 30, 400, 80, "white", (180, 103, 120))
    settings = Button(font, "Settings", (112, 137, 156), "white",  20, 150, 400, 80, "white", (180, 103, 120))
    quit = Button(font, "Quit", (112, 137, 156), "white", 20, 330, 400, 80, "white", (180, 103, 120))

    play.draw_button(window)
    settings.draw_button(window)
    quit.draw_button(window)
    
    return play, settings, quit

class Menu:
    def __init__(self, window, GameStateManager, width, height):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        
    def run(self):
        font = pygame.font.SysFont("Calibri", 60, True) # Font for text and buttons
        
        self.window.fill((23, 27, 32)) # Background colour of the program
        self.play_button, self.settings_button, self.quit_button = draw_objects(self.window, self.width, self.height, font)
        
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
            print("Entering Settings Menu")
        elif self.play_button.rect.collidepoint(pos):
            self.GameStateManager.set_state("menuPlay")
            print("Entering Play Menu")