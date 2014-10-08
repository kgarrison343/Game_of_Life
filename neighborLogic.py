def num_of_neighbors(grid):
    neighbor_grid = []
    h = len(grid)
    for x in range(h):
        neighbor_grid.append([])
        w = len(grid[x])
        for y in range(w):
            neighbor_grid[x].append(0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        rx = x + i
                        ry = y + j

                        if ry >= 0 and 0 <= rx < w and ry < h and grid[rx][ry] == 1:
                            neighbor_grid[x][y] += 1
    return neighbor_grid
