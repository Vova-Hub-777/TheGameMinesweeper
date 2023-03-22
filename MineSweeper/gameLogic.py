import random

class GameLogic():
    def __init__(self):
        pass

    def createMap(self,
                  level):  # Generate the map according to the level + planting mines according to the level + creating appropriate numbers near the mines
        width = level[0]
        height = level[1]
        mine = level[2]
        arr = [[0 for row in range(width)] for column in range(height)]
        num = 0
        while num < mine:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            print(num)
            if arr[y][x] == 'X':
                print(num)
                continue
            print("[HINT] Generated mine location: (x:", x, ", y:", y,
                  ")")
            arr[y][x] = 'X'  # Display 'X' in the coordinate where the mine is created.

            # Generate number hints around the mines
            if (x >= 0 and x <= width - 2) and (y >= 0 and y <= height - 1):
                if arr[y][x + 1] != 'X':
                    arr[y][x + 1] += 1  # center right
            if (x >= 1 and x <= width - 1) and (y >= 0 and y <= height - 1):
                if arr[y][x - 1] != 'X':
                    arr[y][x - 1] += 1  # center left
            if (x >= 1 and x <= width - 1) and (y >= 1 and y <= height - 1):
                if arr[y - 1][x - 1] != 'X':
                    arr[y - 1][x - 1] += 1  # top left
            if (x >= 0 and x <= width - 2) and (y >= 1 and y <= height - 1):
                if arr[y - 1][x + 1] != 'X':
                    arr[y - 1][x + 1] += 1  # top right
            if (x >= 0 and x <= width - 1) and (y >= 1 and y <= height - 1):
                if arr[y - 1][x] != 'X':
                    arr[y - 1][x] += 1  # top center
            if (x >= 0 and x <= width - 2) and (y >= 0 and y <= height - 2):
                if arr[y + 1][x + 1] != 'X':
                    arr[y + 1][x + 1] += 1  # bottom right
            if (x >= 1 and x <= width - 1) and (y >= 0 and y <= height - 2):
                if arr[y + 1][x - 1] != 'X':
                    arr[y + 1][x - 1] += 1  # bottom left
            if (x >= 0 and x <= width - 1) and (y >= 0 and y <= height - 2):
                if arr[y - 1][x] != 'X':
                    arr[y - 1][x] += 1  # bottom center
            num += 1
        return arr