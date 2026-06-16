import pygame
import maze_algorithm

CELL_SIZE = 35

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
GRAY = (180, 180, 180)


def animate_search(
    path,
    visited,
    algorithm_name,
    execution_time
):

    pygame.init()

    font = pygame.font.SysFont("Arial", 20)

    rows = len(maze_algorithm.maze)
    cols = len(maze_algorithm.maze[0])

    width = cols * CELL_SIZE
    height = rows * CELL_SIZE + 120

    screen = pygame.display.set_mode(
        (width, height)
    )

    pygame.display.set_caption(
        "Maze Pathfinding Visualization"
    )

    visited_set = set()

    # ====================
    # Animasi eksplorasi
    # ====================

    for node in visited:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

        visited_set.add(node)

        draw_grid(
            screen,
            visited_set,
            set(),
            algorithm_name,
            execution_time,
            len(path),
            len(visited),
            font
        )

        pygame.display.update()

        pygame.time.delay(80)

    # ====================
    # Animasi path akhir
    # ====================

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
            path_set,
            algorithm_name,
            execution_time,
            len(path),
            len(visited),
            font
        )

        pygame.display.update()

        pygame.time.delay(120)

    # ====================
    # Tetap tampil
    # ====================

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


def draw_grid(
    screen,
    visited_set,
    path_set,
    algorithm_name,
    execution_time,
    path_length,
    visited_count,
    font
):

    screen.fill(WHITE)

    rows = len(maze_algorithm.maze)
    cols = len(maze_algorithm.maze[0])

    # ====================
    # Statistik
    # ====================

    title = font.render(
        f"Algorithm : {algorithm_name}",
        True,
        (0, 0, 0)
    )


    path_text = font.render(
        f"Path Length : {path_length}",
        True,
        (0, 0, 0)
    )

    visited_text = font.render(
        f"Visited : {visited_count}",
        True,
        (0, 0, 0)
    )

    maze_size_text = font.render(
        f"Maze Size : {rows} x {cols}",
        True,
        (0, 0, 0)
    )

    screen.blit(title, (10, 10))
    screen.blit(path_text, (10, 60))
    screen.blit(visited_text, (10, 85))
    screen.blit(maze_size_text, (250, 10))

    # ====================
    # Gambar maze
    # ====================

    for row in range(rows):

        for col in range(cols):

            color = WHITE

            if maze_algorithm.maze[row][col] == '#':
                color = BLACK

            elif maze_algorithm.maze[row][col] == 'S':
                color = GREEN

            elif maze_algorithm.maze[row][col] == 'G':
                color = RED

            if (
                (row, col) in visited_set
                and
                maze_algorithm.maze[row][col] not in ['S', 'G']
            ):
                color = BLUE

            if (
                (row, col) in path_set
                and
                maze_algorithm.maze[row][col] not in ['S', 'G']
            ):
                color = YELLOW

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE + 120,
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