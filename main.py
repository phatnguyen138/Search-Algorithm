from __future__ import annotations
import turtle                    # import turtle library
from turtle import *
import time
import sys
import heapq
from collections import deque
from tkinter import *
from typing import Protocol, Iterator, Tuple, TypeVar, Optional

T = TypeVar('T')

maze_map = []
cost = {}

def read_file(name):
    count = 0
    with open('mazes/' + name,'r') as f:
        first_line = int(f.readline()[0])
        for line in f.readlines():
            if count >= first_line:
                maze_map.append(line)
            else:
                point_info = line.split(' ')
                cell_x = -400 + (int( point_info[0]) * 24)
                cell_y = 260 - (int(point_info[1]) * 24)
                point = int(point_info[2].rstrip())
                cost[cell_x,cell_y] = point
            count = count + 1
    print(cost)

read_file('maze_map.txt')
grid = maze_map

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("gray")                # set the background colour
wn.title("A BFS Maze Solving Program")
wn.setup(830,550)                  # setup the dimensions of the working window
turtle.speed(0)


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("black")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -400 + (x * 24)         # move to the x location on the screen staring at -400
            screen_y = 260 - (y * 24)          # move to the y location of the screen starting at 260

            if character == "X":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list
                cost[screen_x, screen_y] = 1

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                path.append((screen_x, screen_y))
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                cost[screen_x, screen_y] = 0
                red.goto(screen_x, screen_y)
    for cell in path:
        neighbor[cell] = []
        if (cell[0] - 24,cell[1]) in path:
            neighbor[cell].append((cell[0] -24,cell[1]))

        if (cell[0], cell[1] - 24) in path:
            neighbor[cell].append((cell[0], cell[1] - 24))

        if (cell[0] + 24,cell[1]) in path:
            neighbor[cell].append((cell[0] + 24,cell[1]))

        if (cell[0], cell[1] + 24) in path:
            neighbor[cell].append((cell[0], cell[1] + 24))
        print(cell)



def endProgram():
    wn.exitonclick()
    sys.exit()

def bfs(x,y,end_x,end_y):
    visited = set()
    frontier = deque()
    frontier.append((x, y))
    solution[x,y] = x,y
    goal_reached = False

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cell)        # identify frontier cells
            blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            # print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        if (x,y) == (end_x, end_y):
            goal_reached = True
            break
        green.goto(x,y)
        green.stamp()
    return goal_reached

def dfs(x,y,end_x,end_y):
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
    

def UCS(x,y,end_x,end_y):
    goal_reached = False
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

    return goal_reached

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, T]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

def backRoute(x, y):
    cost = 0
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):   
        yellow.goto(solution[x, y])       
        yellow.stamp()
        x, y = solution[x, y]  
        cost = cost + 1
    return cost

# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
solution = {}
neighbor = {}


# main program starts here ####
setup_maze(grid)
if UCS(start_x,start_y,end_x,end_y):
    print(backRoute(end_x, end_y))
else:
    print("No way")
ts = turtle.getscreen()
print(cost)
wn.exitonclick()
