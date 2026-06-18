maze = []

ROWS = 0
COLS = 0


def set_maze(new_maze):

    global maze
    global ROWS
    global COLS

    maze = new_maze

    ROWS = len(maze)
    COLS = len(maze[0])


def findStartGoal():

    start = None
    goal = None

    for i in range(ROWS):

        for j in range(COLS):

            if maze[i][j] == 'S':
                start = (i, j)

            elif maze[i][j] == 'G':
                goal = (i, j)

    return start, goal


def isMoveValid(x, y):

    return (
        0 <= x < ROWS
        and
        0 <= y < COLS
        and
        maze[x][y] != '#'
    )