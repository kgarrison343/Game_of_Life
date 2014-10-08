# main.py
import neighborLogic

START_GRID = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0,0,0],
              [0,0,0,0,1,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0,0]]

def display2DGrid(grid):
  "Print 2D grid to screen"
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      print(grid[row][column], end=' ')
			
    print()

def stepLogic(mainGrid, neighborGrid):
  for x, row in enumerate(neighborGrid):
    for y, cell in enumerate(row):
      if cell == 3:
        mainGrid[x][y] = 1
      elif cell < 2 or cell > 3:
        mainGrid[x][y] = 0
  return mainGrid
        

if __name__ == "__main__":

    mainGrid = START_GRID

    while(1):
      neighborGrid = neighborLogic.checkNumOfNeighbors(mainGrid)
      display2DGrid(mainGrid)
      input('Press enter to continue...')
      mainGrid = stepLogic(mainGrid, neighborGrid)
