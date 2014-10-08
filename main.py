# main.py
import neighborLogic

START_GRID = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]


def display_2d_grid(grid):
    """Print 2D grid to screen"""
    for row in grid:
        for cell in row:
            print(cell, end=' ')

        print()


def step_logic(main_grid, neighbor_grid):
    """

    :param main_grid:
    :param neighbor_grid:
    :return:
    """
    for x, row in enumerate(neighbor_grid):
        for y, cell in enumerate(row):
            if cell == 3:
                main_grid[x][y] = 1
            elif cell < 2 or cell > 3:
                main_grid[x][y] = 0
    return main_grid


if __name__ == "__main__":

    mainGrid = START_GRID
    cease = 'y'
    while cease != 'n':
        neighborGrid = neighborLogic.num_of_neighbors(mainGrid)
        display_2d_grid(mainGrid)
        cease = input('Continue? (Y/N)')
        mainGrid = step_logic(mainGrid, neighborGrid)
