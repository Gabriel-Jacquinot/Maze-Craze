import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init() # Initialisation of all mixer functions so errors do not occur
        
        self.clickSFX = pygame.mixer.Sound("Sound/clickSFX.wav") # Loading the sound effect that plays when something is clicked on
        self.menuMusic = pygame.mixer.music.load("Sound/menuMusic.mp3") # Loading the background music which plays in the background

        self.playing = True # Boolean value for if the music is playing or not (playing by default)
        self.click = True # Boolean value for if sound effects are on or off (on by default)
    
    def play_click(self):
        self.clickSFX.play() # Play the click sound effect (called whenever something is clicked)
        
    def play_music(self):
        pygame.mixer.music.play(-1) # By default play the music (called in main loop)
        
    def toggle_music(self):
        if not self.playing: # If the music is not playing
            pygame.mixer.music.play(-1) # Play the music
            self.playing = True # Set boolean for music as playing
        else:
            pygame.mixer.music.stop() # Stop the music from playing
            self.playing = False # Set boolean for music as not playing
            
    def toggle_click(self):
        if not self.click: # If the sound effects are not on
            pygame.mixer.Sound.set_volume(self.clickSFX, 100) # Change the volume to 0
            self.click = True # Set boolean for sound effects as on
            
        else:
            pygame.mixer.Sound.set_volume(self.clickSFX, 0) # Change the volume to 0
            self.click = False # Set boolean for sound effects as not on
    