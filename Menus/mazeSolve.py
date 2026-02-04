import pygame
import time
from Tools.colours import Colours
from Objects.button import ButtonImg
from Objects.button import Button
from Objects.box import draw_box
from Objects.text import draw_text
from Tools.scale import size, pos
from MazeAlgorithms.RDFS import MazeGenerator

def draw_objects(window, width, height, font, mazeSize, sizeBorderColour, themeBorderColour, themeText, difficultyBorderColour, difficultyText, playBgColour, difficultyBgColour):
    
    draw_box(window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, width, height)
    
    box_w, box_h = size(width, height, 30, 6)
    box_x, box_y = pos(width, height, 77.5, 19.5, box_w, box_h)
    box = Button(font, "", Colours.LIGHTGREY, "white", box_x, box_y , box_w, box_h, Colours.GREY, Colours.GREY, 0)
    
    back_w, back_h = size(width, height, 10, 10)
    back_x, back_y = pos(width, height, 8, 13, back_w, back_h)
    back = ButtonImg("back1.png", back_x, back_y, "back2.png",  back_w, back_h)
    
    gen_w, gen_h = size(width, height, 24, 6)
    gen_x, gen_y = pos(width, height, 85.6, 8, gen_w, gen_h)
    gen = Button(font, "   Generate", Colours.GOGREEN, "white", gen_x, gen_y, gen_w, gen_h, Colours.GREY, Colours.GREY, 50)
    
    play_w, play_h = size(width, height, 24, 6)
    play_x, play_y = pos(width, height, 50, 59, play_w, play_h)
    play = Button(font, "       Play", (playBgColour), "white", play_x, play_y, play_w, play_h, Colours.GREY, Colours.GREY, 50)
    
    size_w, size_h = size(width, height, 26, 6)
    size_x, size_y = pos(width, height, 60, 8, size_w, size_h)
    maze_size = Button(font, f"Size : {mazeSize}", Colours.BLUE, "white", size_x, size_y, size_w, size_h, (sizeBorderColour), Colours.GREY, 0)
    
    theme_w, theme_h = size(width, height, 29.5, 6)
    theme_x, theme_y = pos(width, height, 31.5, 8, theme_w, theme_h)
    theme = Button(font, f"Theme : {themeText}", Colours.BLUE, "white", theme_x, theme_y, theme_w, theme_h, (themeBorderColour), Colours.GREY, 0)
    
    difficulty_w, difficulty_h = size(width, height, 39.5, 6)
    difficulty_x, difficulty_y = pos(width, height, 36.5, 19.5, difficulty_w, difficulty_h)
    difficulty = Button(font, f"Difficulty : {difficultyText}", (difficultyBgColour), "white", difficulty_x, difficulty_y, difficulty_w, difficulty_h, (difficultyBorderColour), Colours.GREY, 0)
    
    playA_w, playA_h = size(width, height, 24, 6)
    playA_x, playA_y = pos(width, height, 50, 70, play_w, play_h)
    playAgain = Button(font, "  Play Again", Colours.BLUE, "white", playA_x, playA_y, playA_w, playA_h, Colours.GREY, Colours.GREY, 50)
    
    return back, gen, maze_size, theme, difficulty, play, box, playAgain

def gen_maze(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour):
     # Initialise the maze generator attributes and methods
    maze = MazeGenerator(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour)
    return maze # run one step of the maze generation process

def gen_grid(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour):
     # Initialise the maze generator attributes and methods
    grid = MazeGenerator(window, GameStateManager, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y, solutionColour)
    return grid # run one step of the maze generation process

class Solve:
    def __init__(self, window, GameStateManager, fps, width, height, font, sound):
        self.window = window
        self.GameStateManager = GameStateManager
        self.fps = fps
        self.width, self.height = width, height
        self.maze_w, self.maze_h = width - 35 * 2, height - 100 * 2 # Maze size relative to screen
        self.maze_x, self.maze_y = pos(width, height, 5, 32.2, 35, 100) # Where the maze is positioned
        self.font = font
        self.sound = sound
        self.size = 40 # The default size of each cell
        self.x, self.y = 0, 0 # Starting coordinates
        self.sizeBorderColour = Colours.GREEN
        self.themeBorderColour = Colours.GREY
        self.difficultyBorderColour = Colours.GREEN
        self.visitColour = Colours.LIGHTGREY
        self.wallColour = Colours.GREY
        self.currentColour = Colours.BLUE
        self.mazeSize = "  Small" # Default maze size
        self.generate = False 
        self.maze_generated = False
        self.maze = None
        self.theme = "Original"
        self.mazeColour = Colours.LIGHTGREY
        self.scale = 3.1
        self.fin_x, self.fin_y = 96.7, 93.1
        self.themeText = "Classic"
        self.difficultyText = "     Easy"
        self.playBgColour = Colours.GREY
        self.solutionColour = Colours.BLUE
        self.finished = False
        self.showMaze = False
        self.generating = False
        self.progress = ""
        self.old_time = time.time()
        self.timer = "1:30"
        self.real_time = 120
        self.difficultyBgColour = Colours.BLUE
        self.frame_count = 0
        self.fps = 60
        self.allow_movement = False
        self.dx, self.dy = 0, 0
        self.won = False
        self.lost = True
        self.no_movement = False
        self.time_out = True
        
    def run(self):
        draw_box(self.window, 50, 50, 100, 56.3, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        
        self.back_button, self.gen_button, self.maze_size_button, self.theme_button, self.difficulty_button, self.play_button, self.box, self.playAgain_button = draw_objects(self.window, self.width, self.height, self.font, self.mazeSize, self.sizeBorderColour, self.themeBorderColour, self.themeText, self.difficultyBorderColour, self.difficultyText, self.playBgColour, self.difficultyBgColour)
        
        pos = pygame.mouse.get_pos()
        self.back_button.img_hover(pos)
        self.play_button.button_hover(pos)
        self.gen_button.button_hover(pos)
        self.maze_size_button.button_hover(pos)
        self.theme_button.button_hover(pos)
        self.difficulty_button.button_hover(pos)
        self.playAgain_button.button_hover(pos)

        self.back_button.draw_image(self.window)
        self.box.draw_button(self.window)
        self.gen_button.draw_button(self.window)
        self.maze_size_button.draw_button(self.window)
        self.theme_button.draw_button(self.window)
        self.difficulty_button.draw_button(self.window)
        
        self.back_clicked = self.back_button.img_click(pos)
        
        # Using an f string to relay the change of time to the user
        draw_text(self.window, f"Time Left : {self.timer}", Colours.GREY, self.font, 77.5, 19.5, self.width, self.height)
        
        if self.generate:
            if self.maze is None:
                self.maze = gen_maze(self.window, self.GameStateManager, self.maze_w, self.maze_h, self.size, self.visitColour, self.wallColour, self.x, self.y, self.currentColour, self.maze_x, self.maze_y, self.mazeColour, self.scale, self.fin_x, self.fin_y, self.solutionColour)
                self.maze.find_solution = False

            if not self.showMaze:   
                self.maze.run()
                if not self.maze.done():
                    self.wait_screen() # Screen telling the player to wait for new maze
                    if time.time() - self.old_time >= 0.25: # Only happen every quarter of a second
                        if self.progress == ".................": # Maximum length
                            self.progress = "" # Reset length
                        else: # Add one dot a time and set a new time
                            self.progress = str(self.progress) + "." 
                            self.old_time = time.time()
                else:
                    self.play_screen() # Screen that displays the play button
                    self.play_button.draw_button(self.window)
                    
            else:
                self.generate = False
                self.maze_generated = True

        if self.maze and self.showMaze: # Draw an empty maze
            self.maze.draw_grid()
            self.maze.draw_current()
            self.maze.redraw()
            
        if self.maze is None: # If there is no maze drawn
            # Create an empty grid (Updates each cycle to keep up with any changes made)
            self.grid = gen_grid(self.window, self.GameStateManager, self.maze_w, self.maze_h, self.size, self.visitColour, self.wallColour, self.x, self.y, self.currentColour, self.maze_x, self.maze_y, self.mazeColour, self.scale, self.fin_x, self.fin_y, self.solutionColour)
            self.grid.draw_grid() # Draw the empty grid
            self.playColour = Colours.GREY

        if self.maze:
            if self.maze.done():
                self.playBgColour = Colours.BLUE
                
            if self.finished: # When the user presses play
                # If the user has completed the maze
                if self.maze.current_cell == self.maze.grid[(self.maze.cols - 1) + (self.maze.rows - 1) * self.maze.cols]:
                    self.won = True 
                    self.difficultyBgColour = Colours.BLUE
                    self.allow_movement = False # Stop the user from moving
                    self.win() # Display win screen
                    self.playAgain_button.draw_button(self.window)
                    
                if not self.won and not self.lost: # When the maze has not been solved by the user
                    self.time_out = False # By default the user hasn't run out of time
                    # Time left in accordance to the difficulty and converting frames to seconds
                    remaining_secs = self.real_time - (self.frame_count // self.fps) 
                    if remaining_secs < 0: # When the user runs out of time
                        remaining_secs = 0 # Make sure the displayed time is not negative
                        self.lost = True # The user has lost
                        self.difficultyBgColour = Colours.BLUE # Allow difficulty to change
                        self.time_out = True # Ran out of time
                        self.no_movement = True # Prevent the user from moving
                    minutes = remaining_secs // 60 # Convert seconds to minutes with no remainder (DIV)
                    seconds = remaining_secs % 60 # Get remaining seconds after the minutes are removed (MOD)
                    self.timer = "{0}:{1:02}".format(minutes, seconds) # This is what formats the timer to show minutes and seconds 
                    self.frame_count += 1 # Add one frame every tick to allow for time to 'pass'
                    
                    self.allow_movement = True # Allow the user to move as there is time left
                    
                    if self.no_movement: # If there is no time time left
                        self.allow_movement = False # Don't allow movement
                        
                if self.time_out: # When the time has ran out display the no time screen and play again button
                    self.no_time()
                    self.playAgain_button.draw_button(self.window)

    def movement(self, direction):
        if self.allow_movement:
            self.sound.play_click() # Play sound for each movement
            # If the direction is up, right, down, left
            # And the directional wall is not true
            # Find the cell that is in that direction and make it the current cell
            # Then redraw the current cell to update its position

            # And if the cell is not the starting cell (grid[0], which has a gap)
            if direction == "up" and not self.maze.current_cell.walls["top"] and not self.maze.current_cell == self.maze.grid[0]:
                next_cell = self.maze.grid[self.maze.current_cell.find_index(self.maze.current_cell.x, self.maze.current_cell.y - 1)]
                self.maze.current_cell = next_cell
                self.maze.draw_current()
            elif direction == "right" and not self.maze.current_cell.walls["right"]:
                next_cell = self.maze.grid[self.maze.current_cell.find_index(self.maze.current_cell.x + 1, self.maze.current_cell.y)]
                self.maze.current_cell = next_cell
                self.maze.draw_current()
            elif direction == "down" and not self.maze.current_cell.walls["bottom"]:
                next_cell = self.maze.grid[self.maze.current_cell.find_index(self.maze.current_cell.x, self.maze.current_cell.y + 1)]
                self.maze.current_cell = next_cell
                self.maze.draw_current()
            elif direction == "left" and not self.maze.current_cell.walls["left"]:
                next_cell = self.maze.grid[self.maze.current_cell.find_index(self.maze.current_cell.x - 1, self.maze.current_cell.y)]
                self.maze.current_cell = next_cell
                self.maze.draw_current()
        
    def click(self, pos):
        if self.back_clicked:
            self.sound.play_click()
            self.reset_maze()
            
            if self.difficultyText == "     Easy":
                self.timer = "1:30"
                self.real_time = 90
            elif self.difficultyText == "  Normal":
                self.timer = "1:00"
                self.real_time = 60
            elif self.difficultyText == "     Hard":
                self.timer = "0:30"
                self.real_time = 30
            elif self.difficultyText == "Ultra Hard":
                self.timer = "0:15"
                self.real_time = 15
                            
            self.GameStateManager.set_state("menuPlay")
            self.difficultyBorderColour = Colours.GREEN
            self.difficultyBgColour = Colours.BLUE
            self.difficultyText = "     Easy"
            self.won, self.lost = False, False
            self.finished = False
            
        elif self.gen_button.rect.collidepoint(pos):
            self.progress = ""
            self.difficultyBgColour = Colours.BLUE
            self.showMaze = False
            self.finished = False
            self.sound.play_click()
            self.reset_maze() # Clear any previous maze
            
            if self.difficultyText == "     Easy":
                self.timer = "1:30"
                self.real_time = 90
            elif self.difficultyText == "  Normal":
                self.timer = "1:00"
                self.real_time = 60
            elif self.difficultyText == "     Hard":
                self.timer = "0:30"
                self.real_time = 30
            elif self.difficultyText == "Ultra Hard":
                self.timer = "0:15"
                self.real_time = 15
                
            if self.mazeSize == "  Small":
                self.scale = 3.1
            elif self.mazeSize == "Medium":
                self.scale = 2.65
            elif self.mazeSize == "  Large":
                self.scale = 1.9
            
            self.frame_count = 0
            self.playBgColour = Colours.GREY
            self.won = False
            self.won, self.lost = False, False
            self.generate = True # Set the generate value to True to start the generation process
            self.finished = False
            self.allow_movement = True
            self.no_movement = False
            
        elif self.maze_size_button.rect.collidepoint(pos):
            self.sound.play_click()
            # For each click of the button, the size text, border colour and maze size will change
            # Each state of the button makes the maze density greater by changing the size variable to be smaller
            # The button will cycle through each size in a circle for every click.
            if self.mazeSize == "  Small":
                self.size = 35
                self.scale = 2.65
                self.mazeSize = "Medium"
                self.sizeBorderColour = Colours.ORANGE
            elif self.mazeSize == "Medium":
                self.size = 25
                self.scale = 1.9
                self.mazeSize = "  Large"
                self.sizeBorderColour = Colours.RED
            elif self.mazeSize == "  Large":
                self.size = 40
                self.scale = 3.1
                self.mazeSize = "  Small"
                self.sizeBorderColour = Colours.GREEN
                
            if self.difficultyText == "     Easy":
                self.timer = "1:30"
                self.real_time = 90
            elif self.difficultyText == "  Normal":
                self.timer = "1:00"
                self.real_time = 60
            elif self.difficultyText == "     Hard":
                self.timer = "0:30"
                self.real_time = 30
            elif self.difficultyText == "Ultra Hard":
                self.timer = "0:15"
                self.real_time = 15
                
            self.playBgColour = Colours.GREY
            self.difficultyBgColour = Colours.BLUE
            self.showMaze = True
            self.maze = None
            self.won, self.lost = False, False
            self.finished = False
            
        elif self.play_button.rect.collidepoint(pos):
            if self.maze and self.maze.done():
                self.sound.play_click()
                self.difficultyBgColour = Colours.GREY
                self.showMaze = True
                self.finished = True
                self.won, self.lost = False, False
                
        elif self.playAgain_button.rect.collidepoint(pos):
            if self.won: # If the user has won
                self.sound.play_click()
                self.difficultyBgColour = Colours.GREY
                self.frame_count = 0 # Reset the timer by resetting counted frames
                self.maze.current_cell = self.maze.grid[0] # Set the current cell back to the start
                self.won, self.lost = False, False # No longer won/ lost
                self.allow_movement = True # Allow movement
                self.no_movement = False # Stop movement from being stopped
            elif self.lost: # If the user has lost
                self.sound.play_click()
                self.difficultyBgColour = Colours.GREY
                self.frame_count = 0 # Reset the timer by resetting counted frames
                self.maze.current_cell = self.maze.grid[0] # Set the current cell back to the start
                self.won, self.lost = False, False # No longer won/ lost
                self.allow_movement = True # Allow movement
                self.no_movement = False # Stop movement from being stopped
                
        elif self.theme_button.rect.collidepoint(pos):
            self.sound.play_click()
            if self.mazeSize == "  Small":
                self.scale = 3.1
            elif self.mazeSize == "Medium":
                self.scale = 2.65
            elif self.mazeSize == "  Large":
                self.scale = 1.9
                
            if self.difficultyText == "     Easy":
                self.timer = "1:30"
                self.real_time = 90
            elif self.difficultyText == "  Normal":
                self.timer = "1:00"
                self.real_time = 60
            elif self.difficultyText == "     Hard":
                self.timer = "0:30"
                self.real_time = 30
            elif self.difficultyText == "Ultra Hard":
                self.timer = "0:15"
                self.real_time = 15
                
            self.maze = None
            self.paused = False
            self.pauseText = "Pause"
            self.pauseBorderColour = Colours.GREEN
            self.pauseBgColour = Colours.GREY
            self.playBgColour = Colours.GREY
            self.difficultyBgColour = Colours.BLUE
            self.showMaze = True
            self.maze = None
            
            # For each click of the button, both the border colour and theme will change
            # Each theme will change the background, border, visited, and leading cell of the maze generation
            # The button will cycle through each theme in a circle when clicked
            if self.theme == "Original":
                self.themeBorderColour = Colours.WHITE
                self.theme = "Light"
                self.themeText = "Light"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.WHITE, Colours.BLACK, Colours.BLUE
                self.solutionColour = self.currentColour
            elif self.theme == "Light":
                self.themeBorderColour = Colours.BLACK
                self.theme = "Dark"
                self.themeText = "Dark"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.BLACK, Colours.WHITE, Colours.BLUE
                self.solutionColour = self.currentColour
            elif self.theme == "Dark":
                self.themeBorderColour = Colours.RED
                self.theme = "Red and black"
                self.themeText = "Red"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.RED, Colours.NEONBLUE, Colours.NEONGREEN
                self.solutionColour = self.currentColour
            elif self.theme == "Red and black":
                self.themeBorderColour = Colours.LIGHTPINK
                self.theme = "Neon pink"
                self.themeText = "Pink" 
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.LIGHTPINK, Colours.WHITE, Colours.NEONYELLOW
                self.solutionColour = self.currentColour
            elif self.theme == "Neon pink":
                self.themeBorderColour = Colours.NEONYELLOW
                self.theme = "Neon blue"
                self.themeText = "Yellow"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.NEONYELLOW, Colours.NEONBLUE, Colours.NEONPINK
                self.solutionColour = self.currentColour
            elif self.theme == "Neon blue":
                self.themeBorderColour = Colours.GOLD
                self.theme = "Gold"
                self.themeText = "Gold"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.BLACK, Colours.GOLD, Colours.BLOODRED
                self.solutionColour = self.currentColour
            elif self.theme == "Gold":
                self.themeBorderColour = Colours.NEONBLUE
                self.theme = "Blue"
                self.themeText = "Blue"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.BLACK, Colours.BLUE, Colours.NEONPINK, Colours.NEONORANGE
                self.solutionColour = self.currentColour
            elif self.theme == "Blue":
                self.themeBorderColour = Colours.RED
                self.theme = "Inverted"
                self.themeText = "Inverse"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.GREY, Colours.GREY, Colours.WHITE, Colours.RED
                self.solutionColour = self.currentColour
            elif self.theme == "Inverted":
                self.themeBorderColour = Colours.GREY
                self.theme = "Original"
                self.themeText = "Classic"
                self.mazeColour, self.visitColour, self.wallColour, self.currentColour = Colours.LIGHTGREY, Colours.LIGHTGREY, Colours.GREY, Colours.BLUE
                self.solutionColour = self.currentColour
            
            self.playBgColour = Colours.GREY
            self.won, self.lost = False, False
            self.finished = False
            self.showMaze = True
        
        elif self.difficulty_button.rect.collidepoint(pos):
            if not self.finished or self.won or self.lost:
                self.sound.play_click()
                if self.difficultyText == "Ultra Hard":
                    self.difficultyBorderColour = Colours.GREEN
                    self.difficultyText = "     Easy"
                    self.timer = "1:30"
                    self.real_time = 90
                elif self.difficultyText == "     Easy":
                    self.difficultyBorderColour = Colours.ORANGE
                    self.difficultyText = "  Normal"
                    self.timer = "1:00"
                    self.real_time = 60
                elif self.difficultyText == "  Normal":
                    self.difficultyBorderColour = Colours.RED
                    self.difficultyText = "     Hard"
                    self.timer = "0:30"
                    self.real_time = 30
                elif self.difficultyText == "     Hard":
                    self.difficultyBorderColour = Colours.BLACK
                    self.difficultyText = "Ultra Hard"
                    self.timer = "0:15"
                    self.real_time = 15
            
    def reset_maze(self):
        # Clear the previouos maze when leaving menu or resetting
        self.maze = None # Remove any current maze object
        self.maze_generated = False # Prevent a maze from being generated
        self.generate = False # Stop generating a maze
        
    def wait_screen(self):
        draw_box(self.window, 50, 61, 96, 40.1, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        draw_text(self.window, f"{self.progress}", Colours.GREY, self.font, 50, 52, self.width, self.height)
        draw_text(self.window, "Generating", Colours.GREY, self.font, 50, 59, self.width, self.height)
        draw_text(self.window, f"{self.progress}", Colours.GREY, self.font, 50, 64, self.width, self.height)
        
    def play_screen(self):
        draw_box(self.window, 50, 61, 96, 40.1, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        draw_text(self.window, "Generation Complete", Colours.GREY, self.font, 50, 44, self.width, self.height)
        
    def no_time(self):
        draw_box(self.window, 50, 61, 72, 30.075, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        draw_text(self.window, "Game Over", Colours.RED, self.font, 50, 49, self.width, self.height)
        draw_text(self.window, "Ran out of time", Colours.GREY, self.font, 50, 56, self.width, self.height)
        
    def win(self):
        draw_box(self.window, 50, 61, 72, 30.075, 15, Colours.LIGHTGREY, Colours.GREY, self.width, self.height)
        draw_text(self.window, "You Win!", Colours.GOGREEN, self.font, 50, 49, self.width, self.height)
        draw_text(self.window, "Maze complete", Colours.GREY, self.font, 50, 56, self.width, self.height)