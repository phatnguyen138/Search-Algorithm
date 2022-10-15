from maze import *
from PriorityQueue import *
from heuristic import *

green = Green()
yellow = Yellow()
blue = Blue()
red = Red()

def greedy_bfs(x,y,x_end,y_end,neighbor,cost=0):
    visited=[]
    slution={}
    frontier=PriorityQueue()
    frontier.put((x,y),0)
    # came_from={}
    # came_from[(x,y)]=None
    while not frontier.empty():
        current=frontier.get()
        if current==(x_end,y_end):
            break
        priority_list=[]
        for next in neighbor[current]:
            if next not in visited:
                priority_list.append(heuristic(next,(x_end,y_end)))
                frontier.put(next,heuristic(next,(x_end,y_end)))
                slution[next]=current
                blue.goto(next)
                blue.stamp()
                green.goto(current)
                green.stamp()
                visited.append(current)
    return slution

