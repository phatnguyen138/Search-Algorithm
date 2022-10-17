from maze import *
from PriorityQueue import *
from heuristic import *



def greedy_bfs(x,y,x_end,y_end,neighbor,cost=0):
    green = Green()
    blue = Blue()
    red=Red()
    visited=[]
    slution={}
    frontier=PriorityQueue()
    frontier.put((x,y),0)
    while not frontier.empty():
        current=frontier.get()
        if current==(x_end,y_end):
            break
        red.goto(current)
        for next in neighbor[current]:
            if next not in visited:
                priority = heuristic(next,(x_end,y_end))
                frontier.put(next,priority)
                visited.append(next)
                slution[next]=current
                blue.goto(next)
                blue.stamp()
        if current != (x,y):
            green.goto(current)
            green.stamp()
    return slution

