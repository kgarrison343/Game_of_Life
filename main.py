# main.py

import sys

import pygame
from pygame.locals import *

from neighborLogic import num_of_neighbors


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


def display_2D_grid_pygame(grid):
    """

    :param grid:
    """
    cell_length = (windowLength // 10) - 2

    windowSurfaceObj.fill(grey)

    cell_x, cell_y = 2, 2
    for row in mainGrid:
        for cell in row:
            if cell == 1:
                pygame.draw.rect(windowSurfaceObj, black, (cell_x, cell_y, cell_length, cell_length))
            else:
                pygame.draw.rect(windowSurfaceObj, white, (cell_x, cell_y, cell_length, cell_length))
            cell_x += cell_length + 2
        cell_y += cell_length + 2
        cell_x = 2

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()

    windowLength = 302
    windowSurfaceObj = pygame.display.set_mode((windowLength, windowLength))
    pygame.display.set_caption('Game of Life')

    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    grey = pygame.Color(127, 127, 127)

    mainGrid = START_GRID

    display_2D_grid_pygame(mainGrid)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    neighborGrid = num_of_neighbors(mainGrid)
                    step_logic(mainGrid, neighborGrid)
                    display_2D_grid_pygame(mainGrid)

        pygame.display.update()
        fps_clock.tick(30)