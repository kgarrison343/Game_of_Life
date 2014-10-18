# main.py

import sys

import pygame
from pygame.locals import *

import json

from neighborLogic import num_of_neighbors


def save_current_grid_state(grid):
    with open('save/savedGrid', 'w') as save_file:
        json.dump(grid, save_file)


def load_saved_grid_state():
    with open('save/savedGrid', 'r') as load_file:
        return json.load(load_file)


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
    cellRects = []
    cell_x, cell_y = 2, 2
    for x, row in enumerate(grid):
        cellRects.append([])
        for y, cell in enumerate(row):
            cellRects[x].append(Rect(cell_x, cell_y, cell_length, cell_length))
            if cell == 1:
                pygame.draw.rect(windowSurfaceObj, black, cellRects[x][y])
            else:
                pygame.draw.rect(windowSurfaceObj, white, cellRects[x][y])
            cell_x += cell_length + 2
        cell_y += cell_length + 2
        cell_x = 2
    return cellRects


if __name__ == "__main__":

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

    pygame.init()
    fps_clock = pygame.time.Clock()

    windowLength = 302
    windowSurfaceObj = pygame.display.set_mode((windowLength, windowLength))
    pygame.display.set_caption('Game of Life')

    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    grey = pygame.Color(127, 127, 127)

    mainGrid = START_GRID

    cell_rects = display_2d_grid(mainGrid)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    neighborGrid = num_of_neighbors(mainGrid)
                    mainGrid = step_logic(mainGrid, neighborGrid)
                    cell_rects = display_2d_grid(mainGrid)
                elif event.key == K_r:
                    mainGrid = START_GRID
                    neighborGrid = []
                    cell_rects = display_2d_grid(mainGrid)
                elif event.key == K_s:
                    save_current_grid_state(mainGrid)
                elif event.key == K_l:
                    START_GRID = load_saved_grid_state()
                    mainGrid = START_GRID
                    neighborGrid = []
                    cell_rects = display_2d_grid(mainGrid)
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for x, row in enumerate(cell_rects):
                    for y, cell in enumerate(row):
                        if cell.collidepoint(pos) == 1:
                            mainGrid[x][y] = 0 if mainGrid[x][y] == 1 else 1
                            cell_rects = display_2d_grid(mainGrid)

        pygame.display.update()
        fps_clock.tick(30)