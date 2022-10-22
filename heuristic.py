import math

def heuristic_greedy(a, b,points):
    res = 0
    (x1, y1) = a
    (x2, y2) = b
    res = res + math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))/24
    print(points)
    print(len(points))
    for key in points:
        x_cost,y_cost = key
        if a != key:
            res = res + (points[(x_cost,y_cost)]/((abs(x1-x_cost)+abs(y1-y_cost))*len(points)))/24
        else:
            res = res + (points[(x_cost,y_cost)]/len(points))/24
    return res

def heuristic_star(a, b, points):
    (x1, y1) = a
    (x2, y2) = b
    res = (abs(x2-x1)+abs(y2-y1))/24
    print(len(points))
    for key in points:
        x_cost,y_cost = key
        if a != key:
            res = res + (points[(x_cost,y_cost)]/((abs(x1-x_cost)+abs(y1-y_cost))*len(points)))/24
        else:
            res = res + (points[(x_cost,y_cost)]/len(points))/24
    return res