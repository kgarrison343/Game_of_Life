# main.py

def display2DGrid(grid):
	"Print 2D grid to screen"
	for row in range(len(grid)):
		for column in range(len(grid[row])):
			print(grid[row][column], end=' ')
			
		print("\n")

if __name__ == "__main__":
	mainGrid = []
	
	for row in range(10):
		# Fill grid with lists
		mainGrid.append([])
		for column in range(10):
			# Fill grid with 0s
			mainGrid[row].append(0)
			
	display2DGrid(mainGrid)