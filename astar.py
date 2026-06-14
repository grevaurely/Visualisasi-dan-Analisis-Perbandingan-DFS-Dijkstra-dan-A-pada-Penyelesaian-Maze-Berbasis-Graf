import heapq
from maze_algorithm import isMoveValid

directions = [
    (-1,0), (1,0), (0,-1), (0,1)
]

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) #manhattan distance

def astar(start,goal):
    pq = [(0,0, start, [start])]

    visited = set()
    visited_order = []

    while pq:
        f,g,current, path = heapq.heappop(pq) #g : biaya yg sudah ditempuh,h : perkiraan jarak ke goal, f: rumus A* -> f = g+h, yg dipilih oleh a star adalah f terkecil

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

            if isMoveValid (nx, ny):
                new_g = g+1
                new_f = (new_g+heuristic((nx,ny), goal)) 

                heapq.heappush(
                    pq,
                    (
                        new_f,
                        new_g,
                        (nx,ny),
                        path + [(nx,ny)]
                    )
                )
    return None, visited_order


#pq is priority queue, dijkstra menghitung biaya, heap = yang costnya paling kecil diproses terlebih dahulu
#pq = [(0, start, [start])], formatnya (cost, current_node, path)