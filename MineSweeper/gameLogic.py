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
        return arr