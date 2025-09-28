class GameStateManager():
    def __init__(self, initial_state): 
        self.current_state = initial_state # Sets the default program state to the state the program starts with, which is menuMain
    
    def get_state(self):
        return self.current_state # Returns the current program state
    
    def set_state(self, state):
        self.current_state = state # Change the current state to the one specified