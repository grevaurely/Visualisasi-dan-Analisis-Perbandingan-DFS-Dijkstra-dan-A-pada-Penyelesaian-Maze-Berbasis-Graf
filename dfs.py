from maze_algorithm import isMoveValid

directions = [
    (-1,0), (1,0), (0,-1), (0,1)
]

def dfs(start, goal):

    stack = [(start, [start])] #current node, path (jalur yg udah dilewti)
    visited = set() #untuk mencegah loop
    visited_order = [] # buat animasi

    while stack: #selama stack tidak kosong
        current, path = stack.pop()
        
        if current in visited:
            continue

        visited.add(current)
        visited_order.append(current)

        if current == goal:
            return path, visited_order

        x,y = current

        for dx, dy in directions: #dx dy berasal dari directions, nx = new x, ny = new y
            nx = x+dx
            ny = y+dy
            
            if isMoveValid(nx,ny):
                stack.append(((nx,ny), path+[(nx,ny)])
            )
                
    return None, visited_order