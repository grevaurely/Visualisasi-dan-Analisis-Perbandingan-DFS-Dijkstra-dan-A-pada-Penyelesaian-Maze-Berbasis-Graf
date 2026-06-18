import random
from collections import deque


def is_connected(maze):
    rows = len(maze)
    cols = len(maze[0])

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    queue = deque([start])
    visited = set([start])

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:

        x, y = queue.popleft()

        if (x, y) == goal:
            return True

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < rows
                and
                0 <= ny < cols
                and
                maze[nx][ny] != '#'
                and
                (nx, ny) not in visited
            ):

                visited.add((nx, ny))
                queue.append((nx, ny))

    return False


def generate_maze(rows, cols, wall_prob=0.30):

    while True:

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

        if is_connected(maze):
            return maze