import pygame
from MineSweeper.settings import *

class GUI():
    def __init__(self, level): # reset
        pygame.init()  # Initialize pygame.
        super().__init__()
        SCREEN_SIZE=self.getScreenSize(level)
        SCREEN_WIDTH = self.getScreenSize(level)[0]
        SCREEN_HEIGHT = self.getScreenSize(level)[1]
        self.count = 0
        self.screen = pygame.display.set_mode(SCREEN_SIZE)  # set display size
        pygame.display.set_caption('Minesweeper')  # set program name
        gameLevel=self.getLevel(level) # Receive level in tuple format.

    def getLevel(self, level): # Get the level (need to fix it later)
        if level=='Beginner':
            return BEGINNER
        elif level=='Intermediate':
            return INTERMEDIATE
        elif level=='Expert':
            return ADVANCED

    def getScreenSize(self,level):
        if level=='Beginner':
            return SCREEN_SIZE_BEGINNER
        elif level=='Intermediate':
            return SCREEN_SIZE_INTERMEDIATE
        elif level=='Expert':
            return SCREEN_SIZE_ADVANCED
