from __future__ import annotations
import maze
from heuristic import *
from maze import *
from PriorityQueue import *

green = Green()
yellow = Yellow()
blue = Blue()
red = Red()


def astar(x,y,end_x,end_y, neighbor, cost):
    visited = []
    solution = {}
    # goal_reached = False
    frontier = PriorityQueue()
    frontier.put((x,y),0)
    came_from = {}
    cost_so_far = {}
    came_from[(x, y)] = None
    cost_so_far[(x, y)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == (end_x, end_y):
            goal_reached = True
            break
        
        for next in neighbor[current]:
            if next not in visited:
                new_cost = cost_so_far[current] + cost[next]
                if next == (176, 20):
                    print(next,cost_so_far[current],cost[next])
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(next,(end_x,end_y))
                    frontier.put(next, priority)
                    if next == (176, 20):
                        frontier.print()
                        print(neighbor[next])
                    blue.goto(next)
                    blue.stamp()
                    solution[next] = current
                green.goto(current)                 # green turtle goto x and y position
                green.stamp() 
                visited.append(current)

    return solution

