# main.py
import neighborLogic

def display2DGrid(grid):
  "Print 2D grid to screen"
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      print(grid[row][column], end=' ')
			
    print()

if __name__ == "__main__":
    mainGrid = []
	
    for row in range(10):
      # Fill grid with lists
      mainGrid.append([])
      for column in range(10):
        # Fill grid with 1s
        mainGrid[row].append(1)
	
    neighborGrid = neighborLogic.checkNumOfNeighbors(mainGrid)
    display2DGrid(mainGrid)
    input('Press enter to continue...')
    display2DGrid(neighborGrid)
