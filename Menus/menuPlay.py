import pygame
from Tools.colours import Colours
from Objects.button import Button, ButtonImg
from Objects.box import draw_box
from Tools.scale import size, pos
from Objects.image import Image

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    # Button image, image file name, button x and y position, hover image file name, button width and height
    # Size, window width and height, object width and height
    # Position, window width and height, object x and y position, scaled object width and height
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)

    # Initiating all properties of each button for the play menu
    # Button, font, background colour, text colour, button x and y position, button width and height, border colour, hover colour
    # Size, window width and height, object width and height
    # Position, window width and height, object x and y position, scaled object width and height
    customise_w, customise_h = size(width, height, 20, 40)
    customise_x, customise_y = pos(width, height, 35, 50, customise_w, customise_h)
    customise = Button(font, " Generate", Colours.BLUE, "white", customise_x, customise_y , customise_w, customise_h, Colours.GREY, Colours.GREY, 40)
    
    solve_w, solve_h = size(width, height, 20, 40)
    solve_x, solve_y = pos(width, height, 65, 50, solve_w, solve_h)
    solve = Button(font, "    Solve", Colours.BLUE, "white", solve_x, solve_y , solve_w, solve_h, Colours.GREY, Colours.GREY, 40)
    
    # Initiating all properties of the images for the play menu
    # For the image, image file name, x and y position, width and height
    mazeImg_w, mazeImg_h = size(width, height, 19, 19)
    mazeImg_x, mazeImg_y = pos(width, height, 35, 50, mazeImg_w, mazeImg_h)
    mazeImg = Image("solve.png", mazeImg_x, mazeImg_y, mazeImg_w, mazeImg_h)
    
    solveImg_w, solveImg_h = size(width, height, 20, 20)
    solveImg_x, solveImg_y = pos(width, height, 65, 50, solveImg_w, solveImg_h)
    solveImg = Image("maze.png", solveImg_x, solveImg_y, solveImg_w, solveImg_h)

    
    return back, customise, solve, mazeImg, solveImg # Return all of the buttons so that they can be interacted with later

class Play:
    def __init__(self, window, GameStateManager, width, height, font, sound): # All parameters needed for establishing the play menu
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.sound = sound
        
    def run(self): # Handle any changes within the menu
        # Draw all of the objects to establish the main menu, including the buttons which are taken as variables
        self.back_button, self.customise_button, self.solve_button, self.mazeImg, self.solveImg = draw_objects(self.window, self.width, self.height, self.font)
        
        pos = pygame.mouse.get_pos() # Getting the mouse postition

        # Calling all of the hover functions for the buttons to check for updates
        self.back_button.img_hover(pos)
        self.customise_button.button_hover(pos)
        self.solve_button.button_hover(pos)
        
        # Redrawing the buttons, also to update when it is hovered over
        self.back_button.draw_image(self.window, self.width, self.height)
        self.customise_button.draw_button(self.window)
        self.solve_button.draw_button(self.window)
        
        # Redrawing the images
        self.mazeImg.draw_image(self.window)
        self.solveImg.draw_image(self.window)
        
        self.clicked = self.back_button.img_click(pos) # Define the back button click funtion for later use 

        
    def click(self, pos):
        if self.clicked: # If the back button click function returns true
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("menuMain") # Switch game states to go back to the main menu
        elif self.customise_button.rect.collidepoint(pos): # If the mouse is on the button
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("mazeGenerate")
        elif self.solve_button.rect.collidepoint(pos):
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("mazeSolve")