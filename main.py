import pygame
import wx
from Tools.gameStateManager import GameStateManager
from Menus.menuMain import Menu
from Menus.menuSettings import Settings
from Menus.menuPlay import Play
from Sound.audio import Sound
from Menus.mazeGenerate import Generate
from Menus.mazeSolve import Solve

pygame.init() # Initialisation of all pygame functions so errors do not occur

app = wx.App(False) # Initialisation of the wx library
width, height = 1645.714 / 1.25, 925.714 / 1.25 # int(wx.DisplaySize()[0]), int(wx.DisplaySize()[1]) # Taking the native resolution of the users computer # The default width and height of the window which can be changed in the settings
FPS = 60 # Constant value for the fps so that it never changes
logo = pygame.image.load("Images/logo.png") # loading the logo image from the images folder
font = pygame.font.SysFont("Calibri", int(100 / (width/ height)), True) # Font for text and buttons

class Program: # Main class from where the program will run once called upon
    def __init__(self): # Setting the attributes of the class 
         self.window = pygame.display.set_mode((width, height)) ### pygame.FULLSCREEN ### # Creating the main program window with the associated width and height and making it by default full screen.
         pygame.display.set_caption("Maze Craze") # Naming the window
         pygame.display.set_icon(logo) # Adding a custom maze image for the window
         self.clock = pygame.time.Clock() # Set a tick rate which will be used to maintain fps
         sound = Sound() # Play the background music by default
         sound.play_music()
         
         self.GameStateManager = GameStateManager("menuMain") # Set the default program state to menuMain
         
         # Initiating all the different menus and stages of the program so that they can be called upon later
         self.menuMain = Menu(self.window, self.GameStateManager, width, height, font, sound)
         self.menuSettings = Settings(self.window, self.GameStateManager, width, height, font, sound)
         self.menuPlay = Play(self.window, self.GameStateManager, width, height, font, sound)
         self.mazeGenerate = Generate(self.window, self.GameStateManager, width, height, font, sound)
         self.mazeSolve = Solve(self.window, self.GameStateManager, width, height, font, sound)
         
    def run(self): # Called to run the program
        while True: # The game loop, once ended stops the program and keeps checking for state changes
            current_state = self.GameStateManager.get_state() # Check if the state of the program has changed (menu change, etc)
            
            for event in pygame.event.get(): # The event loop checks for any inputs made by the user which will be used in the program
                if event.type == pygame.QUIT: # If the window quit button is pressed pygame and the program are terminated
                    pygame.quit()
                    exit()
                # If the user clicks the mouse button down the click function is handled in the current state file
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if current_state == "menuMain":
                        self.menuMain.click(event.pos)
                    elif current_state == "menuSettings":
                        self.menuSettings.click(event.pos)
                    elif current_state == "menuPlay":
                        self.menuPlay.click(event.pos)
                    elif current_state == "mazeGenerate":
                        self.mazeGenerate.click(event.pos)
                    elif current_state == "mazeSolve":
                        self.mazeSolve.click()
            
            # The program will run the code of the file that correponds to the current state
            if current_state == "menuMain":
                self.menuMain.run()
            elif current_state == "menuSettings":
                self.menuSettings.run()
            elif current_state == "menuPlay":
                self.menuPlay.run()
            elif current_state == "mazeGenerate":
                self.mazeGenerate.run()
            elif current_state == "mazeSolve":
                self.mazeSolve.run()
                
            pygame.display.update() # Update the window so that any changes made are output to the user
            self.clock.tick(FPS) # Setting the tick rate to the amount of frames per second (60) for the program to check for changes
    
if __name__ == "__main__": # If the main.py file has been run then the Program is run. To prevent unnecessary errors
    program = Program() # Initialise the program
    program.run() # Run the program