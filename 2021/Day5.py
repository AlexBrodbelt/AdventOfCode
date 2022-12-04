from collections import Counter

ls = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

ys = """8,0 -> 0,8
6,4 -> 2,0
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

xs = open("input5.txt", "r").read().splitlines()

ls = list(map(lambda x: list(map(lambda y: list(map(int, y.split(","))), x.split(" -> "))),xs))

filtered_ls = []

for i, j in ls:
    if i[0] == j[0]:
        filtered_ls.append([i,j,0]) #vertical line
    elif i[1] == j[1]:
        filtered_ls.append([i,j,1]) #horizontal line
    elif i[0] - j[0] == i[1] - j[1]:
        filtered_ls.append([i,j,2]) #45 degree line
    elif i[0] - j[0] == -(i[1] - j[1]):
        filtered_ls.append([i,j,3]) #135 degree line

#print(filtered_ls)
print("finished filtering")
points = []

for i,j,k in filtered_ls:
    if k == 0:
        vals = (i[1],j[1])
        points.extend([(i[0],x) for x in range(min(vals), max(vals)+1)])
    elif k == 1:
        vals = (i[0],j[0])
        points.extend([(x,i[1]) for x in range(min(vals), max(vals)+1)])
    elif k == 2:
        base = min(i,j)
        points.extend([(base[0]+x, base[1]+x) for x in range(abs(i[0]-j[0])+1)]) #it might break here
    elif  k == 3:
        if i[0] > j[0]:
            points.extend([(i[0]-x, i[1]+x) for x in range(abs(i[0]-j[0])+1)]) # first component of i is greater than first component of j
        else:
            points.extend([(i[0]+x, i[1]-x) for x in range(abs(i[0]-j[0])+1)])




#print(points)
print("finished adding points")
unique = set(points)
        
#print(unique)
D = dict(Counter(points))
ocurrences = D.values()


#print("finished determining unique points")
#print(ocurrences)

print(len([j for j in ocurrences if j > 1]))





    