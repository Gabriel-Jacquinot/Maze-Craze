import pygame
from scale import size, pos

def draw_box(window, x, y, w, h, border, colour, border_colour, width, height):
    w, h = size(width, height, w, h)
    x, y = pos(width, height, x, y, w, h)
    pygame.draw.rect(window, colour, (x, y, w, h))
    pygame.draw.rect(window, border_colour, (x, y, w, h), border)