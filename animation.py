import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

from maze_algorithm import maze


def animate_search(path, visited):

    rows = len(maze)
    cols = len(maze[0])

    base_grid = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):

            if maze[i][j] == '#':
                base_grid[i][j] = 1

            elif maze[i][j] == 'S':
                base_grid[i][j] = 2

            elif maze[i][j] == 'G':
                base_grid[i][j] = 3

    cmap = ListedColormap([
        "white",      # jalan
        "black",      # tembok
        "green",      # start
        "red",        # goal
        "yellow",     # path akhir
        "deepskyblue" # visited
    ])

    fig, ax = plt.subplots(figsize=(8,8))

    def update(frame):

        grid = base_grid.copy()

        for x, y in visited[:frame]:

            if maze[x][y] not in ['S', 'G']:
                grid[x][y] = 5

        ax.clear()

        ax.imshow(grid, cmap=cmap)

        ax.set_xticks([])
        ax.set_yticks([])

        ax.set_title(
            f"Explored Nodes: {frame}"
        )

    ani = FuncAnimation(
        fig,
        update,
        frames=len(visited)+1,
        interval=100,
        repeat=False
    )

    plt.show()

    return ani