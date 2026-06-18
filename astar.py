import heapq
import maze_algorithm

directions = [
    (-1,0), (1,0), (0,-1), (0,1)
]

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) #manhattan distance

def astar(start,goal):
    start_h = heuristic(start,goal)
    pq = [(start_h, start_h, 0, start, [start])]

    visited = set()
    visited_order = []
    g_score = { start:0}

    while pq:
        f,h,g,current, path = heapq.heappop(pq) #g : biaya yg sudah ditempuh,h : perkiraan jarak ke goal, f: rumus A* -> f = g+h, yg dipilih oleh a star adalah f terkecil

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

            if maze_algorithm.isMoveValid (nx, ny):
                new_g = g+1
                if((nx,ny) not in g_score or new_g<g_score[(nx,ny)]):
                    g_score[(nx, ny)] = new_g
                    new_h = heuristic((nx, ny), goal)
                    new_f = new_g + new_h 

                

                    heapq.heappush(
                        pq,
                        (
                            new_f,
                            new_h,
                            new_g,
                            (nx,ny),
                            path + [(nx,ny)]
                        )
                    )
    return None, visited_order


#pq is priority queue, dijkstra menghitung biaya, heap = yang costnya paling kecil diproses terlebih dahulu
#pq = [(0, start, [start])], formatnya (cost, current_node, path)