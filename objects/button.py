import pygame
from colours import Colours
from objects.box import draw_box
from scale import pos, size

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
            
class ButtonImg: # Class for creating a new button that is an image
    def __init__(self, img, x, y, hoverImg, w, h):
        self.img = pygame.transform.smoothscale(pygame.image.load(f"images/{img}").convert_alpha(), (w, h)) # Regular image when not hovered 
        self.hoverImg = pygame.transform.smoothscale(pygame.image.load(f"images/{hoverImg}").convert_alpha(), (w, h)) # Image when hovered
        self.imgMask = pygame.mask.from_surface(self.img)
        self.imgHoverMask = pygame.mask.from_surface(self.hoverImg)
        self.x = x
        self.y = y
    
    def draw_image(self, window, width, height):
        draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
        window.blit(self.img, (self.x, self.y))
        
    def img_hover(self, pos, window):
        imgRect = self.img.get_rect(topleft=(self.x, self.y))
        x = pos[0] - self.x
        y = pos[1] - self.y
        if 0 <= x < imgRect.width and 0 <= y < imgRect.height:
            if self.imgMask.get_at((x, y)):
                self.img = self.hoverImg
                
    def img_click(self, pos):
        imgRect = self.img.get_rect(topleft=(self.x, self.y))
        x = pos[0] - self.x
        y = pos[1] - self.y
        if 0 <= x < imgRect.width and 0 <= y < imgRect.height:
            if self.imgMask.get_at((x, y)):
                return True