def num_of_neighbors(grid):
    """
    Counts number of neighbors and returns a grid for use by the step_logic method
    :param grid: List of List of Ints representing start state
    :return: List of List of Ints representing each member of grid's number of orthogonal and diagonal neighbors
    """
    neighbor_grid = []
    for x, row in enumerate(grid):
        neighbor_grid.append([])
        for y, cell in enumerate(row):
            neighbor_grid[x].append(0)
            for i in range(-1,2):
                for j in range(-1, 2):
                    if not(i == 0 and j == 0):
                        rel_x = x + i
                        rel_y = y + j
                        if len(row) > rel_y >= 0 and 0 <= rel_x < len(grid):
                            neighbor_grid[x][y] += grid[rel_x][rel_y]

    return neighbor_grid
