import pygame
from objects.button import Button

def draw_objects(window, WIDTH, HEIGHT, font):
    # Initiating all properties of each button for the main menu
    play = Button(font, "Play", (112, 137, 156), "white", 20, 30, 400, 80, "white", (180, 103, 120))
    settings = Button(font, "Settings", (112, 137, 156), "white",  20, 150, 400, 80, "white", (180, 103, 120))
    quit = Button(font, "Quit", (112, 137, 156), "white", 20, 330, 400, 80, "white", (180, 103, 120))

    play.draw_button(window)
    settings.draw_button(window)
    quit.draw_button(window)
    
    return play, settings, quit

class Menu:
    def __init__(self, window, GameStateManager, WIDTH, HEIGHT):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = WIDTH
        self.height = HEIGHT
        
    def run(self):
        font = pygame.font.SysFont("Calibri", 70) # Font for text and buttons
        
        self.window.fill((23, 27, 32)) # Background colour of the program
        self.play_button, self.settings_button, self.quit_button = draw_objects(self.window, self.width, self.height, font)
        
        pos = pygame.mouse.get_pos()

        # Update hover effect for buttons
        self.play_button.button_hover(pos)
        self.settings_button.button_hover(pos)
        self.quit_button.button_hover(pos)

        # Redraw buttons with hover effect
        self.play_button.draw_button(self.window)
        self.settings_button.draw_button(self.window)
        self.quit_button.draw_button(self.window)