import pygame
import random

class RDFS:
    def __init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y):
            self.window = window
            self.width, self.height = width, height
            self.size = size
            self.x, self.y = x, y
            self.maze_x, self.maze_y = maze_x, maze_y
            self.visitColour = visitColour
            self.currentColour = currentColour
            self.wallColour = wallColour
            self.cols, self.rows = int(width//size), int(height//size)
            self.walls = {"top": True, "right": True, "bottom": True, "left": True}
            
    def remove_walls(self, current, next): # Remove the walls of current cells 
        dx, dy = current.x - next.x, current.y - next.y
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        if dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        if dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
            
        
class Cell(RDFS):
    def __init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y):
        super().__init__(window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y) # Inheriting the attributes and methods of the RDFS class
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        
    def draw(self): # This function is for drawing one cell
        x, y =  self.maze_x + self.x * self.size, self.maze_y + self.y * self.size
        if self.visited:
            pygame.draw.rect(self.window, self.visitColour, (x, y, self.size, self.size))
        
        if self.walls["top"]:
            pygame.draw.line(self.window, self.wallColour, (x, y), (x + self.size, y), 2)
        if self.walls["right"]:
            pygame.draw.line(self.window, self.wallColour, (x + self.size, y), (x + self.size, y + self.size), 2)
        if self.walls["bottom"]:
            pygame.draw.line(self.window, self.wallColour, (x ,y + self.size), (x + self.size, y + self.size), 2)
        if self.walls["left"]:
            pygame.draw.line(self.window, self.wallColour, (x, y), (x, y + self.size), 2)
            
    def draw_current_cell(self):
        x, y = self.maze_x + self.x * self.size, self.maze_y + self.y * self.size
        pygame.draw.rect(self.window, self.currentColour, (x + 8, y + 8, self.size - 8, self.size - 8)) # For drawing the leading cell, the one in blue
        
    def check_cell(self, x, y, grid): # Checking to see if the cell is within the grid???
        find_index = lambda x, y: x + y * self.cols
        if x < 0 or x > self.cols - 1 or y < 0 or y > self.rows - 1:
            return False
        return grid[find_index(x, y)]
    
    def check_neighbours(self, grid):
        neighbours = []
        top = self.check_cell(self.x, self.y - 1, grid)
        right = self.check_cell(self.x + 1, self.y, grid)
        bottom = self.check_cell(self.x, self.y + 1, grid)
        left = self.check_cell(self.x - 1, self.y,grid)
        if top and not top.visited:
            neighbours.append(top)
        if left and not left.visited:
            neighbours.append(left)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if right and not right.visited:
            neighbours.append(right)
        return random.choice(neighbours) if neighbours else False # Getting a random neighbour cell if it is valid

# May make this part of the main run function
class Grid(RDFS):
    def __init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y):
        RDFS.__init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y)
        self.grid = [Cell(window, width, height, size, visitColour, wallColour, col, row, currentColour, maze_x, maze_y) for row in range(self.rows) for col in range(self.cols)] # Making the grid in accordance to the input size
        self.current_cell = self.grid[0] # Making the top left cell the current cell (cell to start at)
        self.stack = [] # Making a stack for backtracking

class MazeGenerator(Grid):
    def __init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y):
        Grid.__init__(self, window, width, height, size, visitColour, wallColour, x, y, currentColour, maze_x, maze_y)
        
    def run(self):
        for cell in self.grid:
            cell.draw()

        self.current_cell.visited = True
        self.current_cell.draw_current_cell()
        
        next_cell = self.current_cell.check_neighbours(self.grid)
        if next_cell:
            next_cell.visited = True
            self.stack.append(self.current_cell)
            self.remove_walls(self.current_cell, next_cell)
            self.current_cell = next_cell
        elif self.stack:
            self.current_cell = self.stack.pop()
            
    def draw_grid(self):
        for cell in self.grid:
            cell.draw()