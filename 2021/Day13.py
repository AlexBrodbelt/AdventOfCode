test = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

f = open("input13.txt", "r")

input = f.read()


f.close()

# points

points, instructions = input.split("\n\n")

coord_str = points.splitlines()

points = list(map(lambda x: tuple(map(lambda y : int(y), x.split(","))), coord_str))

def print_grid(points):
    x_max = max([x for x,y in points])
    y_max = max([y for x,y in points])
    grid = ""
    for y in range(y_max+1):
        for x in range(x_max+1):
            grid += "."
        grid += "\n"
    grid = grid.splitlines()
    grid = list(map(list, grid))
    for x,y in points:
        grid[y][x] = "#"
    grid = "\n".join(list(map(lambda x: "".join(x), grid)))
    return grid


"""x_max = max([x for x,y in points])

y_max = max([y for x,y in points])

grid = ""

for y in range(y_max+1):
    for x in range(x_max+1):
        grid += "."
    grid += "\n"

grid = grid.splitlines()

grid  = list(map(list, grid))

for x,y in points:
    grid[y][x] = "#"

grid = "\n".join(list(map(lambda x: "".join(x), grid)))

print(grid)"""

#print(print_grid(points))

# folds

instructions = instructions.splitlines()

instructions = [ls[2].split("=") for ls in list(map(lambda x: x.split(), instructions))]

s_points = set()

def fold(axis, coord, point):
    if axis == "y":
        if point[1] < int(coord):
            return point
        else:
            return (point[0], 2*int(coord)-point[1])
    if axis == "x":
        if point[0] < int(coord):
            return point 
        else:
            return (2*int(coord)-point[0], point[1])


l = len(points)
print(l)

for folding in instructions:
    for i in range(len(points)):
        if i < l:
            s_points.add(fold(folding[0], folding[1], points[i]))
            #print(len(s_points))
        else: 
            break
    points = list(s_points)
    l = len(s_points); print("end of iteration", l)
    print((print_grid(points)))
    s_points = set()



#print(instructions)
        