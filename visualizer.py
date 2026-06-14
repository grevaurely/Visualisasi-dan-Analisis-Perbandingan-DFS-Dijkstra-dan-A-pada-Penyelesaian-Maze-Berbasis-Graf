import matplotlib.pyplot as plt
from maze_algorithm import maze

def draw_path(path):

    rows = len(maze)
    cols = len(maze[0])

    grid = []
    
    for row in maze:
        grid.append(row.copy())

    if path:
        for x, y in path:
            if grid[x][y] not in ['S', 'G']:
                grid[x][y] = '*'

    for row in grid:
        print(" ".join(row))