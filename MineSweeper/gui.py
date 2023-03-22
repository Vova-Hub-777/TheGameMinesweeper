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

            pygame.display.update()
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

    def open_Cell(self,arr,OPENED,col,row):

        if col < 0 or col >= len(arr[0]) or row < 0 or row >= len(arr):
            return arr
        cell = arr[row][col]  # selected cell
        if OPENED[row][col]: # Already checked cells
            return arr
        OPENED[row][col] = True
        if cell == 0: # If the cell is 0, create a recursive function that opens repeatedly until a number greater than 1 is generated / Looks like it should be fixed with a for statement
            self.open_Cell(arr, OPENED, col + 1, row)
            self.open_Cell(arr, OPENED,col, row + 1)
            self.open_Cell(arr, OPENED,col + 1, row + 1)
            self.open_Cell(arr, OPENED,col - 1, row)
            self.open_Cell(arr, OPENED,col, row - 1)
            self.open_Cell(arr, OPENED,col - 1, row - 1)
            self.open_Cell(arr, OPENED,col + 1, row - 1)
            self.open_Cell(arr, OPENED,col - 1, row + 1)
        font5 = pygame.font.SysFont('notosanscjkkrblack', 50)
        img5 = font5.render(str(cell), True, BLACK)
        self.screen.blit(img5, (CELL_SIZE*col+10, CELL_SIZE*row+10))
        return OPENED

    def open_All(self,arr,OPENED):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                self.open_Cell(arr,OPENED,j,i)