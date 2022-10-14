import maze
import bfs
from maze import *
from bfs import *
from ucs import *
from dfs import *

# setup lists
walls = []
path = []
solution = {}
neighbor = {}

# read map from text file
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

read_file('maze_map.txt')

# set up turtle
wn = turtle.Screen()       
wn.bgcolor("gray")            
wn.title("Finding path by searching algorithm")
wn.setup(830,550)          
turtle.speed(0)

# setup mazegreen = Green()
yellow = Yellow()
blue = Blue()
red = Red()
green = Green()
maze = Maze()

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

def backRoute(x, y, solution):
    cost = 0
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):   
        yellow.goto(solution[x, y])       
        yellow.stamp()
        x, y = solution[x, y]  
        cost = cost + 1
        print(x, y)
    return cost

def draw():
    setup_maze(maze_map)
    solution = dfs(start_x, start_y, end_x, end_y, path)
    if solution:
        print(backRoute(end_x, end_y,solution))
    else:
        print("No way")
    print(cost)
    # wn.exitonclick()
    done()

draw()