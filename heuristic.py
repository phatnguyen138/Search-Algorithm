import math
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))/24