import pygame
from Tools.colours import Colours
from Objects.button import Button, ButtonImg
from Objects.box import draw_box
from Tools.scale import size, pos
from Objects.text import draw_text
# from Objects.slider import Slider
# from Objects.text import draw_text

def draw_objects(window, width, height, font, sfxButtonBgColour, musicButtonBgColour, sfxText, musicText):
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
    sound_w, sound_h = size(width, height, 25, 5.5)
    sound_x, sound_y = pos(width, height, 56, 30, sound_w, sound_h)
    sound = Button(font, "Sound Effects", sfxButtonBgColour, "white", sound_x, sound_y , sound_w, sound_h, Colours.GREY, Colours.GREY, 0)
    
    music_w, music_h = size(width, height, 12.5, 5.5)
    music_x, music_y = pos(width, height, 49.8, 42, music_w, music_h)
    music = Button(font, "Music", musicButtonBgColour, "white", music_x, music_y , music_w, music_h, Colours.GREY, Colours.GREY, 0)
    
    box1_w, box1_h = size(width, height, 6.5, 5.5)
    box1_x, box1_y = pos(width, height, 40.6, 30, box1_w, box1_h)
    box1 = Button(font, "", Colours.LIGHTGREY, "white", box1_x, box1_y , box1_w, box1_h, Colours.GREY, Colours.GREY, 0)
    
    box2_w, box2_h = size(width, height, 6.5, 5.5)
    box2_x, box2_y = pos(width, height, 40.6, 42, box2_w, box2_h)
    box2 = Button(font, "", Colours.LIGHTGREY, "white", box2_x, box2_y , box2_w, box2_h, Colours.GREY, Colours.GREY, 0)
    
    # SFX_w, SFX_h = size(width, height, 20, 5)
    # SFX_x, SFX_y = pos(width, height, 50, 27, SFX_w, SFX_h)
    # volumeSFX = Slider(SFX_x, SFX_y, SFX_w, SFX_h, Colours.BLUE, Colours.GREY, 0, 100)
    # draw_text(window, str(volumeSFX), Colours.GREY, font, 20, 25, width, height)
    
    # volumeSFXSlider = volumeSFX.draw_slider(window)
    
    # volumeSFX.slide(window, width, volumeSFXSlider)
    
    return back, sound, music, box1, box2 # Return all of the buttons so that they can be interacted with later

class Settings:
    def __init__(self, window, GameStateManager, width, height, font, sound): # All parameters needed for establishing the main menu
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.sound = sound
        self.sfxButtonBgColour = Colours.BLUE
        self.musicButtonBgColour = Colours.BLUE
        self.sfxText = "On"
        self.musicText = "On"
        
    def run(self): # Handle any changes within the menu
        # Draw all of the objects to establish the main menu, including the buttons which are taken as variables
        self.back_button, self.sound_button, self.music_button, self.box1, self.box2 = draw_objects(self.window, self.width, self.height, self.font, self.sfxButtonBgColour, self.musicButtonBgColour, self.sfxText, self.musicText)
        
        pos = pygame.mouse.get_pos() # Getting the mouse position

        # Calling all of the hover functions for the buttons to check for updates
        self.back_button.img_hover(pos)
        self.sound_button.button_hover(pos)
        self.music_button.button_hover(pos)
        
        # Redrawing the buttons and images, also to update when it is hovered over
        self.back_button.draw_image(self.window)
        self.sound_button.draw_button(self.window)
        self.music_button.draw_button(self.window)
        
        self.box1.draw_button(self.window)
        self.box2.draw_button(self.window)
        
        self.clicked = self.back_button.img_click(pos) # Define the back button click function for later use
        
        # Must draw text after back button as it refreshes page with draw_box
        draw_text(self.window, "Settings", Colours.GREY, self.font, 50.5, 14.2, self.width, self.height)
        draw_text(self.window, f"{self.sfxText}", Colours.GREY, self.font, 40.5, 30.2, self.width, self.height)
        draw_text(self.window, f"{self.musicText}", Colours.GREY, self.font, 40.5, 42.2, self.width, self.height)
        
        
        
    def click(self, pos):
        if self.clicked: # If the back button click function returns true
            self.sound.play_click() # Play the click sound effect
            self.GameStateManager.set_state("menuMain") # Switch game states to go back to the main menu
        elif self.sound_button.rect.collidepoint(pos): # If the mouse is on the button
            self.sound.play_click() # Play the click sound effect
            self.sound.toggle_click() # Turn the sound effects on or off
            if self.sfxButtonBgColour == Colours.BLUE:
                self.sfxButtonBgColour = Colours.RED # Change to red
                self.sfxText = "Off" # Change text to off
            else:
                self.sfxButtonBgColour = Colours.BLUE # Change back to blue
                self.sfxText = "On" # Change text back to On
                
            
        elif self.music_button.rect.collidepoint(pos):
            self.sound.play_click() # Play the click sound effect
            self.sound.toggle_music() # Turn the music on or off
            if self.musicButtonBgColour == Colours.BLUE:
                self.musicButtonBgColour = Colours.RED # Change to red
                self.musicText = "Off" # Change text to off
            else:
                self.musicButtonBgColour = Colours.BLUE # Change back to blue
                self.musicText = "On" # Change text back to On