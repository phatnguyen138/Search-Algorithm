p_list = []
maze_map = []
count = 0

with open('mazes/maze_map.txt','r') as f:
    first_line = int(f.readline()[0])
    print(first_line)
    for line in f.readlines():
        if count >= first_line:
            line_map = []
            for char in line.rstrip():
                line_map.append(char)
            maze_map.append(line_map)
        else:
            point_info = line.split(' ')
            p_list.append([int(point_info[0]), int(point_info[1]), int(point_info[2].rstrip()) ]) 
        count = count + 1
