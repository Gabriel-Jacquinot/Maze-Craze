import pygame
from Tools.colours import Colours
from Objects.button import Button
from Objects.image import Image
from Tools.scale import pos, size
from Objects.box import draw_box
from Objects.text import draw_text
import time
import sys

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height) # Draw the background as a box so that a border can be added
    draw_text(window, "Ma     Cra  ", Colours.GREY, font, 19.5, 23, width, height) # Draw the Ma and Cra of Maze Craze with space for the other letters
    draw_text(window, "z", Colours.BLUE, font, 16.8, 23, width, height) # Draw the blue z of maze
    draw_text(window, "z", Colours.BLUE, font, 27.5, 23, width, height) # Draw the blue z of craze
    draw_text(window, "e", Colours.GREY, font, 18.7, 23, width, height) # Draw the grey e of maze
    draw_text(window, "e", Colours.GREY, font, 29.4, 23, width, height) # Draw the grey e of craze
    
    # Initiating all properties of each button for the main menu
    # Button, font, background colour, text colour, button x and y position, button width and height, border colour, hover colour
    # Size, window width and height, object width and height
    # Position, window width and height, object x and y position, scaled object width and height
    play_w, play_h = size(width, height, 9, 5.5) 
    play_x, play_y = pos(width, height, 14.8, 38, play_w, play_h)
    play = Button(font, "Play", Colours.BLUE, "white", play_x, play_y , play_w, play_h, Colours.GREY, Colours.GREY, 0)
    
    settings_w, settings_h = size(width, height, 16, 5.5)
    settings_x, plasettings_y = pos(width, height, 18.3, 50, settings_w, settings_h)
    settings = Button(font, "Settings", Colours.BLUE, "white", settings_x, plasettings_y, settings_w, settings_h, Colours.GREY, Colours.GREY, 0)
    
    quit_w, quit_h = size(width, height, 9.5, 5.5)
    quit_x, quit_y = pos(width, height, 15, 62, quit_w, quit_h)
    quit = Button(font, "Quit", Colours.BLUE, "white", quit_x, quit_y, quit_w, quit_h, Colours.GREY, Colours.GREY, 0)
    
    # Initiating all properties of the image for the main menu
    # For the image, image file name, x and y position, width and height
    menuImg_w, menuImg_h = size(width, height, 50, 50)
    menuImg_x, menuImg_y = pos(width, height, 70, 50, menuImg_w, menuImg_h)
    menuImg = Image("logo.png", menuImg_x, menuImg_y, menuImg_w, menuImg_h)
    
    menuImg.draw_image(window) # Blit the image to the window
    
    return play, settings, quit # Return all of the buttons so that they can be interacted with later

class Menu:
    def __init__(self, window, GameStateManager, width, height, font, sound): # All parameters needed for establishing the main menu
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.sound = sound
        
    def run(self): # Handle any changes within the menu 
        # Draw all of the objects to establish the main menu, including the buttons which are taken as variables
        self.play_button, self.settings_button, self.quit_button = draw_objects(self.window, self.width, self.height, self.font)
        
        pos = pygame.mouse.get_pos() # Get mouse position

        # Check if a button is hovered over and change the background colour of the button 
        self.play_button.button_hover(pos)
        self.settings_button.button_hover(pos)
        self.quit_button.button_hover(pos)

        # Redraw buttons with hover effect
        self.play_button.draw_button(self.window)
        self.settings_button.draw_button(self.window)
        self.quit_button.draw_button(self.window)
        
    def click(self, pos): # Every time mouse button down is input
        if self.quit_button.rect.collidepoint(pos): # If the mouse is on the button
            self.sound.play_click() # Play the click sound effect
            time.sleep(0.22) # Allow time for the sound effect to play before quitting
            pygame.quit() # Delete all pygame objects
            sys.exit() # Exit the program
        elif self.settings_button.rect.collidepoint(pos): # If the mouse is on the button
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("menuSettings") # Change game state to the settings menu
        elif self.play_button.rect.collidepoint(pos): # If the mouse is on the button
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("menuPlay") # Change game state to the settings menu