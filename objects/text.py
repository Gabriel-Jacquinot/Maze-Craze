import pygame
from colours import Colours
from scale import pos

def draw_text(window, text, colour, font, x, y, width, height):
    x, y = pos(width, height, x, y, 0, 0)
    text = font.render(text, Colours.LIGHTGREY, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    window.blit(text, textRect)
    