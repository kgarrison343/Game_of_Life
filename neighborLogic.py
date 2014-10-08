def checkNumOfNeighbors(grid):
  neighborGrid = []
  H = len(grid)
  for x in range(H):
    neighborGrid.append([])
    W = len(grid[x])
    for y in range(W):
      neighborGrid[x].append(0)
      for i in range(-1, 2):
        for j in range(-1, 2):
          if i != 0 or j != 0:
            rx = x + i
            ry = y + j

            if rx >= 0 and ry >= 0 and rx < W and ry < H:
              if grid[rx][ry] == 1:
                neighborGrid[x][y] += 1
  return neighborGrid
