import time

from maze_algorithm import findStartGoal

from dfs import dfs
from dijkstra import dijkstra
from astar import astar

from visualizer import draw_path


start, goal = findStartGoal()

# DFS
t1 = time.perf_counter()

path, visited = dfs(start, goal)

t2 = time.perf_counter()

print("DFS")
print("Path Length:", len(path))
print("Visited:", len(visited))
print("Time:", (t2 - t1) * 1000)

draw_path(path)

print()

# Dijkstra
t1 = time.perf_counter()

path, visited = dijkstra(start, goal)

t2 = time.perf_counter()

print("Dijkstra")
print("Path Length:", len(path))
print("Visited:", len(visited))
print("Time:", (t2 - t1) * 1000)


draw_path(path)

print()

# A*
t1 = time.perf_counter()

path, visited = astar(start, goal)

t2 = time.perf_counter()

print("A*")
print("Path Length:", len(path))
print("Visited:", len(visited))
print("Time:", (t2 - t1) * 1000)

draw_path(path)