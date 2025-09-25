import pygame
from gameStateManager import GameStateManager
from menuMain import Menu

pygame.init() # Initialsion of all pygame functions so errors do not occur.

WIDTH, HEIGHT = 960, 540 # Constant values for the width and height of the widnow so that it never changes
FPS = 60 # Constant value for the fps so that it never changes.
logo = pygame.image.load("images/logo.png") # loading the logo image from the images folder

class Program: # Main class from where the program will run once called upon
    def __init__(self): # Setting the attributes of the class 
         self.window = pygame.display.set_mode((WIDTH, HEIGHT)) # Creating the main program window with the associated width and height
         pygame.display.set_caption("Maze Craze") # Naming the window
         pygame.display.set_icon(logo) # Adding a custom maze image for the window
         self.clock = pygame.time.Clock() # Set a tick rate which will be used to maintain fps
         
         self.GameStateManager = GameStateManager("menuMain") # Set the default program state to menuMain
         
         self.menuMain = Menu(self.window, self.GameStateManager, WIDTH, HEIGHT)
         
    def run(self): # Called to run the program
        while True: # The game loop, once ended stops the program and keeps checking for state changes
            current_state = self.GameStateManager.get_state() # Check if the state of the program has change (menu change, etc)

            for event in pygame.event.get(): # The event loop checks for any inputs made by the user which will be used in the program
                if event.type == pygame.QUIT: # If the window quit button is pressed pygame and the program are terminated.
                    pygame.quit()
                    exit()
                    
            if current_state == "menuMain":
                self.menuMain.run()
                
            pygame.display.update()
            self.clock.tick(FPS)
    
if __name__ == "__main__":
    program = Program()
    program.run()
