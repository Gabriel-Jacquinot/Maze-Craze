import pygame
import random
from Objects.image import Image
from Tools.scale import size

class RDFS:
    def __init__(self, window, width, height, size1, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y):
            self.window = window
            self.width, self.height = width, height
            self.size1 = size1 # Size of the maze
            self.x, self.y = x, y # Coordinate position (starts at (0,0))
            self.maze_x, self.maze_y = maze_x, maze_y # Coordinate position of the whole maze
            self.visitColour = visitColour
            self.currentColour = currentColour
            self.wallColour = wallColour
            self.MazeColour = mazeColour
            self.cols, self.rows = int(width//size1), int(height//size1) # The number of rows and columns in the maze in relation to the size
            self.walls = {"top": True, "right": True, "bottom": True, "left": True} # All the walls of every cell are there at the start of generation
            self.scale = scale
            self.fin_x, self.fin_y = fin_x, fin_y
            self.maze_done = False
            
    def remove_walls(self, current, next): # Remove the walls of current cell and next cell
        dx, dy = current.x - next.x, current.y - next.y # Find the direction of the next cell compared to current cell
        # Then, remove wall of current cell
        # And, remove wall of next cell
        if dx == 1: # If to the left of current cell
            current.walls['left'] = False
            next.walls['right'] = False
        if dx == -1: # If to the right of current cell
            current.walls['right'] = False
            next.walls['left'] = False
        if dy == 1: # If above current cell
            current.walls['top'] = False
            next.walls['bottom'] = False
        if dy == -1: # If below current cell
            current.walls['bottom'] = False
            next.walls['top'] = False
            
    def entrance_exit(self):
        start = self.grid[0] # Retrieving first cell object in the grid index
        end_index = (self.cols - 1) + (self.rows - 1) * self.cols # Calculating the position of the last cell in the grid index
        end = self.grid[end_index] # Retrieving last cell object in the grid index

        start.walls["top"] = False # Remove the top wall of the first cell to show entrance
        end.walls["bottom"] = False # Remove the bottom wall of the last cell to show exit

    def cell_to_screen(self, cell):
        x, y = self.maze_x + cell.x * self.size1, self.maze_y + cell.y * self.size1  # Coordinate of a cell relative to the screen
        return x, y
        
    def maze_finish(self):
        end_index = (self.cols - 1) + (self.rows - 1) * self.cols # Retrieving last cell object in the grid index
        end = self.grid[end_index] # Retrieving last cell object in the grid index
        end_x, end_y = self.cell_to_screen(end) # Getting the x and y coordinates of the last cell relative to the screen
        
        finish_w, finish_h = size(self.width, self.height, self.scale, self.scale)
        finish_x, finish_y = 1 + end_x + (self.size1 - finish_w) // 2, 1 + end_y + (self.size1 - finish_h) // 2 # Calculate the middle of the cell, with + 1 to account for wall size
        finish = Image("checkered.png", finish_x, finish_y, finish_w, finish_h)
        finish.draw_image(self.window) # Draw the checkered box image
            
class Cell(RDFS):
    def __init__(self, window, width, height, size1, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y):
        # Inherit all attributes and methods of the RDFS object
        super().__init__(window, width, height, size1, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y)
        self.visited = False
        
    def draw(self): # Function for drawing one cell in the maze
        x, y =  self.maze_x + self.x * self.size1, self.maze_y + self.y * self.size1 # Grid position to screen position
        if self.visited: # Fill the background cell if visited (sometimes different colour)
            pygame.draw.rect(self.window, self.visitColour, (x, y, self.size1, self.size1))
        
        # Draw each wall of the cell that exists
        # Line width is always 2 and starting postion is top right of the cell
        # Ending postion of line is calculated relative to the size of one cell
        if self.walls["top"]:
            pygame.draw.line(self.window, self.wallColour, (x, y), (x + self.size1, y), 2)
        if self.walls["right"]:
            pygame.draw.line(self.window, self.wallColour, (x + self.size1, y), (x + self.size1, y + self.size1), 2)
        if self.walls["bottom"]:
            pygame.draw.line(self.window, self.wallColour, (x ,y + self.size1), (x + self.size1, y + self.size1), 2)
        if self.walls["left"]:
            pygame.draw.line(self.window, self.wallColour, (x, y), (x, y + self.size1), 2)
        
    def draw_current_cell(self):
        x, y = self.maze_x + self.x * self.size1, self.maze_y + self.y * self.size1 # Find the the current cell x and y coordinates relative to the maze size
        pygame.draw.rect(self.window, self.currentColour, (x + 2, y + 2, self.size1 - 2, self.size1 - 2)) # For drawing the leading cell
        
    def find_index(self, x, y): # Convert 2D grid coordinates into a 1D index (for one value each time)
        return x + (y * self.cols) # Calculate the correct position by adding how far in row to how many cells in all full rows above
        
    def check_cell(self, x, y, grid): # Checking to see if a cell fits within the bounds of the grid
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows: # If the cell is outside the boundary return no cell
            return None # No cell is returned as it is not valid
        return grid[self.find_index(x, y)] # Return the valid cell object at correct index
    
    def check_neighbours(self, grid):
        neighbours = [] # List of neighbours
        
        # Check all directions
        top = self.check_cell(self.x, self.y - 1, grid)
        right = self.check_cell(self.x + 1, self.y, grid)
        bottom = self.check_cell(self.x, self.y + 1, grid)
        left = self.check_cell(self.x - 1, self.y,grid)
        
        # Add all valid and unvisited neighbours to the list
        if top and not top.visited:
            neighbours.append(top)
        if left and not left.visited:
            neighbours.append(left)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if right and not right.visited:
            neighbours.append(right)
            
        # Return a random unvisited neighbour cell, unless unavailable then return False
        if neighbours:
            return random.choice(neighbours)
        else:
            return False

class MazeGenerator(RDFS):
    def __init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y):
        # Inherit attributes and methods of the Grid object
        super().__init__(window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y)
        self.mazeColour = mazeColour # Background colour of the maze
        # Create the maze grid by looping the rows and columns with the Cell class 
        self.grid = [Cell(window, width, height, size, visitColour, wallColour, col, row, currentColour, maze_x, maze_y, mazeColour, scale, fin_x, fin_y) for row in range(self.rows) for col in range(self.cols)] # Making the grid in accordance to the input size
        self.current_cell = self.grid[0] # Making the top left cell the current cell (cell to start at)
        self.stack = [] # Making a stack for backtracking
        
    def run(self):
        # Draw maze background
        pygame.draw.rect(self.window, self.mazeColour, (self.maze_x, self.maze_y, self.cols * self.size1, self.rows * self.size1))
        
        # Draw all the cells in the grid
        self.draw_grid()    
        self.entrance_exit() 

        self.current_cell.visited = True # Current cell is visited (top left)
        self.current_cell.draw_current_cell() # Highlight the leading cell
        
        next_cell = self.current_cell.check_neighbours(self.grid) # Get a random, valid neighbour cell
        if next_cell:
            next_cell.visited = True # Mark neighbour as visited 
            self.stack.append(self.current_cell) # Push current cell to the stack
            self.remove_walls(self.current_cell, next_cell) # Remove the cells walls
            self.current_cell = next_cell # Move to the next cell
        elif self.stack: # If there are no valid neighbours and stack isn't empty then backtrack
            self.current_cell = self.stack.pop() # Pop last cell of stack
        else:
            self.maze_finish() # Initially draw the finish
            self.maze_done = True # Boolean to state that the maze is finished
        
    def draw_grid(self):
        # Draw out the current maze by drawing each cell in the grid as well as the background
        pygame.draw.rect(self.window, self.mazeColour, (self.maze_x, self.maze_y, self.cols * self.size1, self.rows * self.size1))
        for cell in self.grid:
            cell.draw()
            
    def draw_current(self):
        self.current_cell.draw_current_cell() # Highlight the leading cell
        
    def done(self):
        if self.maze_done: # If the maze is done generating
            self.maze_finish() # Draw the checkered box