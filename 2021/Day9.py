f = open("input9.txt", "r")

test = f.read().splitlines()

f.close()


i = len(test)
j = len(test[0])

input = []

for row in test:
    input.append("9"+row+"9")

n = len(input[0])

aux_list = (-1,1)

matrix = ["9"*n] + input + ["9"*n]

print(matrix)

low_points = []

for row in range(1,i+1):
    for column in range(1,j+1):
        adjacents = [int(matrix[row][column+x]) for x in aux_list] + [int(matrix[row+x][column]) for x in aux_list]
        head = int(matrix[row][column])
        if all(map(lambda x: x > head, adjacents)):
                low_points.append(head+1) #risk level is head+1


print(low_points)

print(sum(low_points))


