import pygame
from Tools.colours import Colours
from Objects.button import ButtonImg
from Objects.box import draw_box
from Tools.scale import size, pos
from Objects.image import Image
from Objects.text import draw_text

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    # Button image, image file name, button x and y position, hover image file name, button width and height
    # Size, window width and height, object width and height
    # Position, window width and height, object x and y position, scaled object width and height
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)
    
    RDFS_info_w, RDFS_info_h = size(width, height, 72.34, 20) # Size of the image calculated in accordance to ratios of the image resolution
    RDFS_info_x, RDFS_info_y = pos(width, height, 50, 40, RDFS_info_w, RDFS_info_h)
    RDFS_info = Image("RDFS.png", RDFS_info_x, RDFS_info_y, RDFS_info_w, RDFS_info_h)
    
    backtrack_w, backtrack_h = size(width, height, 28.42, 20) # Size of the image calculated in accordance to ratios of the image resolution
    backtrack_x, backtrack_y = pos(width, height, 50, 77, backtrack_w, backtrack_h)
    backtrack = Image("backtrackingImg.png", backtrack_x, backtrack_y, backtrack_w, backtrack_h)
    
    return back, RDFS_info, backtrack # Return all of the buttons so that they can be interacted with later

class Info:
    def __init__(self, window, GameStateManager, width, height, font, sound): # All parameters needed for establishing the play menu
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.sound = sound
        
    def run(self): # Handle any changes within the menu     
        # Draw all of the objects to establish the main menu, including the buttons which are taken as variables
        self.back_button, RDFS_info_img, backtrack_Img = draw_objects(self.window, self.width, self.height, self.font) 
        
        pos = pygame.mouse.get_pos() # Get mouse position
        
        RDFS_info_img.draw_image(self.window) # Text block
        backtrack_Img.draw_image(self.window) # Diagram
        
        # Title of the page
        draw_text(self.window, "How the maze generation works", Colours.GREY, self.font, 50, 13, self.width, self.height)
        
        # Calling all of the hover functions for the buttons to check for updates
        self.back_button.img_hover(pos)        
        self.back_button.draw_image(self.window)
        
        self.clicked = self.back_button.img_click(pos) # Define the back button click funtion for later use 
        
    def click(self, pos):
        if self.clicked: # If the back button click function returns true
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("menuMain") # Switch game states to go back to the main menu