import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from maze_algorithm import maze


def draw_maze(path=None, visited=None):

    rows = len(maze)
    cols = len(maze[0])

    grid = np.zeros((rows, cols))

    for i in range(rows):

        for j in range(cols):

            if maze[i][j] == '#':
                grid[i][j] = 1

            elif maze[i][j] == 'S':
                grid[i][j] = 2

            elif maze[i][j] == 'G':
                grid[i][j] = 3

    if visited:

        for x, y in visited:

            if maze[x][y] not in ['S', 'G']:
                grid[x][y] = 5

    if path:

        for x, y in path:

            if maze[x][y] not in ['S', 'G']:
                grid[x][y] = 4

    cmap = ListedColormap([
        'white',      # 0 jalan
        'black',      # 1 tembok
        'green',      # 2 start
        'red',        # 3 goal
        'yellow',     # 4 path
        'deepskyblue' # 5 visited
    ])

    plt.figure(figsize=(8, 8))

    plt.imshow(grid, cmap=cmap)

    plt.xticks([])
    plt.yticks([])

    plt.title("Maze Visualization")

    plt.show()