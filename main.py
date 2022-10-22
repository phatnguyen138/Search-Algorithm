from xml.etree.ElementTree import tostring

from numpy import delete
import maze
import tkinter as tk
import os,glob
from maze import *
from bfs import *
from ucs import *
from dfs import *
from astar import *
from greedy import *

# setup lists
walls = []
path = []
solution = {}
neighbor = {}

# read map from text file
maze_map = []
cost = {}
points = {}

def read_file(name):
    count = 0
    with open(name,'r') as f:
        first_line = int(f.readline())
        print(first_line)
        for line in f.readlines():
            if count >= first_line:
                maze_map.append(line)
            else:
                point_info = line.split(' ')
                cell_x = -400 + (int( point_info[0]) * 24)
                cell_y = 260 - (int(point_info[1]) * 24)
                point = int(point_info[2].rstrip())
                cost[cell_x,cell_y] = point
                points[cell_x,cell_y] = point
            count = count + 1


yellow = Yellow()
blue = Blue()
red = Red()
green = Green()
pink = Pink()
wall = Maze()

wn = turtle.Screen()       
wn.bgcolor("#e6e6e6")            
wn.title("Finding path by searching algorithm")
wn.setup(830,550)  

def setup_maze(grid):                          # define a function called setup_maze
    global start_x,start_y,end_x,end_y
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -400 + (x * 24)         # move to the x location on the screen staring at -400
            screen_y = 260 - (y * 24)          # move to the y location of the screen starting at 260

            if character == "x":
                wall.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                wall.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list
                cost[screen_x, screen_y] = 1
                if y == 0 or x == 0 or x == len(grid[y]) - 1 or y == len(grid) -1:
                    green.goto(screen_x, screen_y)       # send green sprite to screen location
                    end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                    green.color("#A020F0")
                    green.stamp()

            if character == "+":
                path.append((screen_x, screen_y))     # add "+" and e to path list
                pink.goto(screen_x, screen_y)
                pink.stamp() 

            if character == "s":
                path.append((screen_x, screen_y))
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                cost[screen_x, screen_y] = 0
                red.goto(screen_x, screen_y)
                red.stamp()
                
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

def backRoute(x, y, solution):
    cost = 0
    yellow.goto(x, y)
    yellow.color("#A020F0")
    yellow.stamp()  
    while solution[x,y] != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.color("yellow")       
        yellow.stamp()
        x, y = solution[x, y]  
        cost = cost + 1
    red.goto(start_x,start_y)
    red.stamp()
    return cost


def dfs():
    setup_maze(maze_map)
    solution = dfs_func(start_x, start_y, end_x, end_y, path)
    if solution:
        return backRoute(end_x, end_y,solution)
    else:
        return -1

def bfs():
    setup_maze(maze_map)
    solution = bfs_func(start_x, start_y, end_x, end_y, path)
    if solution:
        return backRoute(end_x, end_y,solution)
    else:
        return -1

def ucs():
    setup_maze(maze_map)
    solution = ucs_func(start_x, start_y, end_x, end_y,neighbor,cost)
    if solution:
        return backRoute(end_x, end_y,solution)
    else:
        return -1

def astar():
    setup_maze(maze_map)
    solution = astar_func(start_x, start_y, end_x, end_y,neighbor,points=points,cost=cost)
    if solution:
        return backRoute(end_x, end_y,solution)
    else:
        return -1

def greedy():
    setup_maze(maze_map)
    solution = greedy_bfs(start_x, start_y, end_x, end_y,neighbor,points=points,cost=cost)
    if solution:
        return backRoute(end_x, end_y,solution)
    else:
        return -1

def generate(string,res):
    f = open(output_dir+string+".txt","w")
    turtle.getcanvas().postscript(file = output_dir+string+".eps")
    f.write(str(res))
    f.close()


os.chdir("input/level1")
count = 1
for filename in os.listdir():
    name_file=filename.split('.')[0]
    maze_map = []
    read_file(filename)
    os.chdir("..")
    os.chdir("..")
    output_dir = "output/level1/"+name_file+"/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print("DFS")
    res = dfs()
    generate('dfs',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    print("BFS")
    res = bfs()
    generate('bfs',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    print("UCS")
    res = ucs()
    generate('ucs',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    print("A*")
    res = astar()
    generate('astar',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    print("Greedy")
    res = greedy()
    generate('greedy',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    os.chdir("input/level1")


os.chdir("..")
os.chdir("level2")
count = 1
for filename in os.listdir():
    name_file=filename.split('.')[0]
    maze_map = []
    walls = []
    path = []
    neighbor = {}
    read_file(filename)
    os.chdir("..")
    os.chdir("..")
    output_dir = "output/level2/"+name_file+"/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print("A*")
    res = astar()
    generate('astar',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    print("Greedy")
    res = greedy()
    generate('greedy',res)
    walls = []
    path = []
    neighbor = {}
    time.sleep(1)
    turtle.clearscreen()
    os.chdir("input/level2")