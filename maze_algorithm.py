maze = [
    ['S', '.', '.', '#', '.'],
    ['#', '.', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '.', 'G']
]

ROWS = len(maze)
COLS = len(maze[0])

def findStartGoal():
    start = None
    goal = None

    for i in range (ROWS):
        for j in range (COLS):
            if maze[i][j]== 'S':
                start = (i,j)
            elif maze[i][j] == 'G':
                goal = (i,j)
    return start, goal

def isMoveValid(x,y):
    return(0<=x<ROWS and 0<= y<COLS and maze[x][y] != '#')

# tembok : '#'
#mis : start @ (0,0), goal @ (3,4)

