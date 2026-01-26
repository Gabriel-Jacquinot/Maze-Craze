import pygame
from Tools.colours import Colours
from Objects.box import draw_box

class Button: # Class that can be accessed to make any new button
    def __init__(self, font, text, bgColour, textColour, x, y, length, width, borderColour, hoverColour, radius): # A placeholder for all of the parameters associated with making a new button
        self.font = font # Setting the font of the button
        self.textColour = pygame.Color(textColour) # Setting the text colour of the button
        self.rect = pygame.Rect(int(x), int(y), int(length), int(width)) # Setting the box of the button
        self.bgColour = pygame.Color(bgColour) # Setting the background colour of the button
        self.borderColour = pygame.Color(borderColour) # Setting the colour of the border of the button
        self.hoverColour = pygame.Color(hoverColour) # Setting the colour of the button when it is hovered over with the mouse
        self.text = self.font.render(text, True, pygame.Color(textColour)) # Render in the font with given properties
        self.radius = radius # Setting the radius of the border of the button (0 if no border)
        
    def draw_button(self, window):
        pygame.draw.rect(window, self.bgColour, self.rect, 0, self.radius) # Outside rectange and its properties
        pygame.draw.rect(window, self.borderColour, self.rect, 3, self.radius) # Inside rectange and its properties (the one that gets clicked)
        window.blit(self.text, (self.rect.x + 10, self.rect.y + 10)) # Drawing the text onto the button by combing the objects and settting its position
        
    def button_hover(self, pos):
        if self.rect.collidepoint(pos): # Checks if the mouse position is equal to the buttons position
            self.bgColour = self.hoverColour # Change the background colour
        else:
            self.bgColour = self.bgColour # Change back to the regular background colour
            
class ButtonImg: # Class for creating a new button that is an image
    def __init__(self, img, x, y, hoverImg, w, h):
        self.img = pygame.transform.smoothscale(pygame.image.load(f"Images/{img}").convert_alpha(), (w, h)) # Regular image when not hovered 
        self.hoverImg = pygame.transform.smoothscale(pygame.image.load(f"Images/{hoverImg}").convert_alpha(), (w, h)) # Image when hovered
        self.imgMask = pygame.mask.from_surface(self.img) # Creating a custom shape of the buttons area
        self.imgHoverMask = pygame.mask.from_surface(self.hoverImg) # Creating a custom shape of the buttons area when hovered
        self.x = x
        self.y = y
    
    def draw_image(self, window):
        window.blit(self.img, (self.x, self.y))
        
    def img_hover(self, pos): # Creating a rectangle which has the same width and height as the image to act as its boundaries
        imgRect = self.img.get_rect(topleft = (self.x, self.y))
        x = pos[0] - self.x # the x position of the mouse is converted into the coordinates of the image (0, 0 is the top left of the image)
        y = pos[1] - self.y # the y position of the mouse is converted into the coordinates of the image (0, 0 is the top left of the image)
        if 0 <= x < imgRect.width and 0 <= y < imgRect.height: # If the mouse position is within the rectangle boundary of the image
            self.img = self.hoverImg # Change the image to the hover image (change of colour)
                
    def img_click(self, pos):
        imgRect = self.img.get_rect(topleft = (self.x, self.y)) # Creating a rectangle which has the same width and height as the image to act as its boundaries
        x = pos[0] - self.x # the x position of the mouse is converted into the coordinates of the image (0, 0 is the top left of the image)
        y = pos[1] - self.y # the y position of the mouse is converted into the coordinates of the image (0, 0 is the top left of the image)
        if 0 <= x < imgRect.width and 0 <= y < imgRect.height: # If the mouse position is within the rectangle boundary of the image
            return True # Output the button has been clicked