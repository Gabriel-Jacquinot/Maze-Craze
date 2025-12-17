import pygame

class Slider: # class that can be accessed to make any new button
    def __init__(self, x, y, width, height, fillColour, bgColour, minValue, maxValue): # a placehodlder for all of the parameters associated with making a new button
        self.rectFill = pygame.Rect(int(x), int(y), int(width), int(height))
        self.fillColour = pygame.Color(fillColour)
        self.bgColour = pygame.Color(bgColour)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minValue = minValue
        self.maxValue = maxValue
        self.value = minValue
        
        self.bg_rect = pygame.Rect(x, y, width, height)
        
    def draw_slider(self, window):
        pygame.draw.rect(window, self.bgColour, self.bg_rect, border_radius=self.height // 2) # outside rectange and its properties

        fill_width = int((self.value - self.minValue) / (self.maxValue - self.minValue) * self.width)
        fill_rect = pygame.Rect(self.x, self.y, fill_width, self.height)
        pygame.draw.rect(window, self.fillColour, fill_rect, border_radius=self.height // 2)        
    
    # def slide(self, window, slider, pos):
    #     rel_x = max(self.x, min(mx, self.x + self.width))
    #     percent = (rel_x - self.x) / self.width
    #     self.value = int(self.min_val + percent * (self.max_val - self.min_val))