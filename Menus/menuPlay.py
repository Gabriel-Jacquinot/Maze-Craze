import pygame
from Tools.colours import Colours
from Objects.button import Button, ButtonImg
from Objects.box import draw_box
from Tools.scale import size, pos
from Objects.image import Image

def draw_objects(window, width, height, font):
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)

    customise_w, customise_h = size(width, height, 20, 40)
    customise_x, customise_y = pos(width, height, 35, 50, customise_w, customise_h)
    customise = Button(font, " Generate", Colours.BLUE, "white", customise_x, customise_y , customise_w, customise_h, Colours.GREY, Colours.GREY)
    
    solve_w, solve_h = size(width, height, 20, 40)
    solve_x, solve_y = pos(width, height, 65, 50, solve_w, solve_h)
    solve = Button(font, "    Solve", Colours.BLUE, "white", solve_x, solve_y , solve_w, solve_h, Colours.GREY, Colours.GREY)
    
    mazeImg_w, mazeImg_h = size(width, height, 19, 19)
    mazeImg_x, mazeImg_y = pos(width, height, 35, 50, mazeImg_w, mazeImg_h)
    mazeImg = Image("solve.png", mazeImg_x, mazeImg_y, mazeImg_w, mazeImg_h)
    
    solveImg_w, solveImg_h = size(width, height, 20, 20)
    solveImg_x, solveImg_y = pos(width, height, 65, 50, solveImg_w, solveImg_h)
    solveImg = Image("maze.png", solveImg_x, solveImg_y, solveImg_w, solveImg_h)

    back.draw_image(window, width, height)
    customise.draw_button(window)
    solve.draw_button(window)
    
    mazeImg.draw_image(window)
    solveImg.draw_image(window)
    
    return back, customise, solve, mazeImg, solveImg

class Play:
    def __init__(self, window, GameStateManager, width, height, font, clickSFX):
        self.window = window
        self.GameStateManager = GameStateManager
        self.width = width
        self.height = height
        self.font = font
        self.clickSFX = clickSFX
        
    def run(self):
        self.back_button, self.customise_button, self.solve_button, self.mazeImg, self.solveImg = draw_objects(self.window, self.width, self.height, self.font)
        
        pos = pygame.mouse.get_pos()

        self.back_button.img_hover(pos)
        self.customise_button.button_hover(pos)
        self.solve_button.button_hover(pos)
        
        self.back_button.draw_image(self.window, self.width, self.height)
        self.customise_button.draw_button(self.window)
        self.solve_button.draw_button(self.window)
        
        self.mazeImg.draw_image(self.window)
        self.solveImg.draw_image(self.window)
        
        self.clicked = self.back_button.img_click(pos)

        
    def click(self, pos):
        if self.clicked:
            self.clickSFX.play()
            self.GameStateManager.set_state("menuMain")
        elif self.customise_button.rect.collidepoint(pos):
            self.clickSFX.play()
            print("switching states")
            # self.GameStateManager.set_state("mazeCustomise")
        elif self.solve_button.rect.collidepoint(pos):
            self.clickSFX.play()
            print("switching states")
            # self.GameStateManager.set_state("mazeCustomise")