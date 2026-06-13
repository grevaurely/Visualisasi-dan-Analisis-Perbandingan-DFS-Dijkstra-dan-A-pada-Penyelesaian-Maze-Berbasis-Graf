import heapq
from maze_algorithm import isMoveValid

directions = [
    (-1,0), (1,0), (0,-1), (0,1)
]

def dijkstra(start,goal):
    pq = [(0, start, [start])]

    visited = set()
    visited_order = []

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
        visited_order.append(current)

        if current == goal:
            return path, visited_order
        
        x,y = current
        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if isMoveValid (nx,ny):

                heapq.heappush( pq, 
                               (cost+1, (nx,ny), path +[(nx+ny)]))
    return None, visited_order