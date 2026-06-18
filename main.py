import time

from maze_algorithm import findStartGoal

from dfs import dfs
from dijkstra import dijkstra
from astar import astar

from pygame_visualizer import animate_search
from mazeGenerator import generate_maze
import maze_algorithm

start, goal = findStartGoal()



while True:

    print("\n===== PILIH UKURAN MAZE =====")
    print("1. 10 x 10")
    print("2. 20 x 20")
    print("3. 30 x 30")

    size_choice = input("Pilihan: ")

    if size_choice == "1":
        rows = 10
        cols = 10
        break

    elif size_choice == "2":
        rows = 20
        cols = 20
        break

    elif size_choice == "3":
        rows = 30
        cols = 30
        break

    else:
        print("Pilihan tidak valid")

while True:

    generated = generate_maze(rows, cols)

    maze_algorithm.set_maze(generated)

    start, goal = maze_algorithm.findStartGoal()

    path, _ = dijkstra(start, goal)

    if path is not None:
        break
    print("Maze berhasil dibuat")

while True:

    print("\n====================")
    print(" Maze Pathfinder ")
    print("====================")
    print("1. DFS")
    print("2. Dijkstra")
    print("3. A*")
    print("0. Keluar")

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

        animate_search(
            path,
            visited,
            "DFS",
            (t2 - t1) * 1000
        )

    elif choice == "2":

        t1 = time.perf_counter()

        path, visited = dijkstra(start, goal)

        t2 = time.perf_counter()

        print("\nDijkstra")
        print("Path Length:", len(path))
        print("Visited:", len(visited))
        print("Time:", (t2 - t1) * 1000, "ms")

        animate_search(
            path,
            visited,
            "Dijkstra",
            (t2 - t1) * 1000
        )

    elif choice == "3":

        t1 = time.perf_counter()

        path, visited = astar(start, goal)

        t2 = time.perf_counter()

        print("\nA*")
        print("Path Length:", len(path))
        print("Visited:", len(visited))
        print("Time:", (t2 - t1) * 1000, "ms")

        animate_search(
            path,
            visited,
            "A*",
            (t2 - t1) * 1000
        )

    else:

        print("Pilihan tidak valid.")