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


def step_logic(main_grid, neighbor_grid):
    """
    :param neighbor_grid:
    :return:
    """
    new_grid = []
    for x, row in enumerate(neighbor_grid):
        new_grid.append([])
        for y, cell in enumerate(row):
            if cell == 3 or (cell == 2 and main_grid[x][y] == 1):
                new_grid[x].append(1)
            else:
                new_grid[x].append(0)
    return new_grid


def display_2d_grid(grid):
    """

    :param grid:
    """
    cell_length = (windowLength // 10) - 2

    windowSurfaceObj.fill(grey)

    cell_x, cell_y = 2, 2
    for row in grid:
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

    display_2d_grid(mainGrid)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    neighborGrid = num_of_neighbors(mainGrid)
                    mainGrid = step_logic(mainGrid, neighborGrid)
                    display_2d_grid(mainGrid)
                if event.key == K_r:
                    mainGrid = START_GRID
                    neighborGrid = []
                    display_2d_grid(mainGrid)

        pygame.display.update()
        fps_clock.tick(30)