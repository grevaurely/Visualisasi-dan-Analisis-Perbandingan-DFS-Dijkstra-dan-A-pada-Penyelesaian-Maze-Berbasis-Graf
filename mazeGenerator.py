import random


def generate_maze(rows, cols, wall_prob=0.2):

    maze = []

    for r in range(rows):

        row = []

        for c in range(cols):

            if random.random() < wall_prob:
                row.append('#')
            else:
                row.append('.')

        maze.append(row)

    maze[0][0] = 'S'
    maze[rows - 1][cols - 1] = 'G'

    return maze