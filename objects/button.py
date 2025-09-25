import pygame

class Button: # class that can be accessed to make any new button
    def __init__(self, font, text, bgColour, textColour, x, y, length, width, borderColour, hoverColour): # a placehodlder for all of the parameters associated with making a new button
        self.font = font # setting the font of the button
        self.textColour = pygame.Color(textColour) # setting the text colour of the button
        self.rect = pygame.Rect(int(x), int(y), int(length), int(width)) # setting the box of the button
        self.bgColour = pygame.Color(bgColour)
        self.borderColour = pygame.Color(borderColour)
        self.hoverColour = pygame.Color(hoverColour)
        self.text = self.font.render(text, True, pygame.Color(textColour)) # Could be an error here, reference other
        
    def draw_button(self, window):
        pygame.draw.rect(window, self.bgColour, self.rect) # outside rectange and its properties
        pygame.draw.rect(window, self.borderColour, self.rect, width = 3) # inside rectange and its properties (the one that gets clicked)
        window.blit(self.text, (self.rect.x + 10, self.rect.y + 10)) # combining both rectangles into one object to make it a button
        
    def button_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.bgColour = self.hoverColour
        else:
            self.bgColour = self.bgColour 
        
        
        