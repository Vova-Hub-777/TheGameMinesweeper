import sys, pygame
from MineSweeper.settings import *
from pygame.locals import *
from MineSweeper.gameLogic import GameLogic

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
        arr = GameLogic.createMap(self, gameLevel) # create and save the map
        OPENED = [[False for column in range(len(arr[0]))] for row in range(len(arr))] # Check if the column is open
        CHECKED = [[False for column in range(len(arr[0]))] for row in range(len(arr))] # Check if flag is checked
        self.draw_Cells(arr)  # Draw cells

        while True:  # main game loop (call the methods needed for the game)
            for event in pygame.event.get(): # Area that receives events in the window. For example, quit key, keyboard key, mouse click, etc.
                if event.type == QUIT: # Keep the program running until you press the X key at the top (required)
                    pygame.quit()
                    sys.exit()
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


    def draw_Cells(self, arr):
        COLUMN_COUNT = len(arr[0])
        ROW_COUNT = len(arr)

        for column_index in range(COLUMN_COUNT):
            for row_index in range(ROW_COUNT):
                rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

