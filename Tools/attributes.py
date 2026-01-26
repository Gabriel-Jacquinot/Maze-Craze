class FPS:
    def __init__(self, intial_fps):
        self.fps = intial_fps # Amount of cycles of the program per second
        
    def current_fps(self):
        return self.fps
            
    def new_fps(self, num):
        self.fps = num