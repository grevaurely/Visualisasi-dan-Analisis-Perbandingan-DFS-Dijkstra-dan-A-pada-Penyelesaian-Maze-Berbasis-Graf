import pygame
import time

from maze_algorithm import maze

CELL_SIZE = 35

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,100,255)
YELLOW = (255,255,0)
GRAY = (180,180,180)


def animate_search(path, visited):

    pygame.init()

    rows = len(maze)
    cols = len(maze[0])

    width = cols * CELL_SIZE
    height = rows * CELL_SIZE

    screen = pygame.display.set_mode(
        (width, height)
    )

    pygame.display.set_caption(
        "Maze Pathfinding Visualization"
    )

    running = True

    visited_set = set()

    for node in visited:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

        visited_set.add(node)

        draw_grid(
            screen,
            visited_set,
            []
        )

        pygame.display.update()

        pygame.time.delay(120)

    path_set = set()

    for node in path:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

        path_set.add(node)

        draw_grid(
            screen,
            visited_set,
            path_set
        )

        pygame.display.update()

        pygame.time.delay(150)

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


def draw_grid(screen, visited_set, path_set):

    screen.fill(WHITE)

    rows = len(maze)
    cols = len(maze[0])

    for row in range(rows):

        for col in range(cols):

            color = WHITE

            if maze[row][col] == '#':
                color = BLACK

            elif maze[row][col] == 'S':
                color = GREEN

            elif maze[row][col] == 'G':
                color = RED

            if (row, col) in visited_set:

                if maze[row][col] not in ['S', 'G']:
                    color = BLUE

            if (row, col) in path_set:

                if maze[row][col] not in ['S', 'G']:
                    color = YELLOW

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                color,
                rect
            )

            pygame.draw.rect(
                screen,
                GRAY,
                rect,
                1
            )