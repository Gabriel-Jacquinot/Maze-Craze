import pygame

class Image:
    def __init__(self, img, x, y, width, height):
        self.img = pygame.transform.smoothscale(pygame.image.load(f"images/{img}").convert_alpha(), (width, height))
        self.x = x
        self.y = y

    def draw_image(self, window):
        window.blit(self.img, (self.x, self.y))