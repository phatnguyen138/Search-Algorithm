from __future__ import annotations
import maze
import heapq
from maze import *
from typing import Protocol, Iterator, Tuple, TypeVar, Optional

T = TypeVar('T')


green = Green()
yellow = Yellow()
blue = Blue()
red = Red()

def UCS(x,y,end_x,end_y, neighbor, cost):
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
            new_cost = cost_so_far[current] + cost[next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                solution[next] = current
            green.goto(current)                 # green turtle goto x and y position
            green.stamp() 

    return solution

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, T]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]