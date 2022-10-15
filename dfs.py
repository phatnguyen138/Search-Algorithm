from maze import *
from collections import deque
import time


def dfs(x ,y, end_x, end_y, path):
    blue = Blue()
    green = Green()
    red = Red()
    yellow = Yellow()
    start_x = x
    start_y = y
    solution = {}
    frontier = deque()
    solution[x,y] = x,y
    visited = []
    frontier.append((x,y))
    while len(frontier) > 0:
        time.sleep(0)
        current = (x,y)
        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            cellleft = (x - 24, y)
            solution[cellleft] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellleft)        # blue turtle goto the  cellleft position
            blue.stamp()               # stamp a blue turtle on the maze
            frontier.append(cellleft)  # add cellleft to the frontier list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            celldown = (x, y - 24)
            solution[celldown] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(celldown)
            blue.stamp()
            frontier.append(celldown)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            cellright = (x + 24, y)
            solution[cellright] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellright)
            blue.stamp()
            frontier.append(cellright)

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
            cellup = (x, y + 24)
            solution[cellup] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellup)
            blue.stamp()
            frontier.append(cellup)

        x, y = frontier.pop()           # remove last entry from the frontier list and assign to x and y
        if x == end_x & y == end_y:
            break
        visited.append(current)         # add current cell to visited list
        green.goto(x,y)                 # green turtle goto x and y position
        green.stamp()                   # stamp a copy of the green turtle on the maze
        if (x,y) == (end_x, end_y):     # makes sure the yellow end turtle is still visible after been visited
            yellow.stamp()              # restamp the yellow turtle at the end position 
            break
        if (x,y) == (start_x, start_y): # makes sure the red start turtle is still visible after been visited
            red.stamp()
    return solution