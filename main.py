import time

from maze_algorithm import findStartGoal

from dfs import dfs
from dijkstra import dijkstra
from astar import astar

from pygame_visualizer import animate_search


start, goal = findStartGoal()

while True:

    print("\n====================")
    print(" Maze Pathfinder ")
    print("====================")
    print("1. DFS")
    print("2. Dijkstra")
    print("3. A*")
    print("0. Keluar")
    print("note: jika ingin mengubah algoritma, klik silang di bagian animasi")

    choice = input("\nPilih algoritma: ")

    if choice == "0":

        print("Program selesai.")
        break

    elif choice == "1":

        t1 = time.perf_counter()

        path, visited = dfs(start, goal)

        t2 = time.perf_counter()

        print("\nDFS")
        print("Path Length:", len(path))
        print("Visited:", len(visited))
        print("Time:", (t2 - t1) * 1000, "ms")

        animate_search(path, visited)

    elif choice == "2":

        t1 = time.perf_counter()

        path, visited = dijkstra(start, goal)

        t2 = time.perf_counter()

        print("\nDijkstra")
        print("Path Length:", len(path))
        print("Visited:", len(visited))
        print("Time:", (t2 - t1) * 1000, "ms")

        animate_search(path, visited)

    elif choice == "3":

        t1 = time.perf_counter()

        path, visited = astar(start, goal)

        t2 = time.perf_counter()

        print("\nA*")
        print("Path Length:", len(path))
        print("Visited:", len(visited))
        print("Time:", (t2 - t1) * 1000, "ms")

        animate_search(path, visited)

    else:

        print("Pilihan tidak valid.")