import numpy as np

def scenic_score(i,j, grid):
    score = 1
    current_tree = grid[i,j]
    #          right-row (flipped) left-row    top-col (flipped)  bottom_col
    regions = [grid[i, j-1::-1], grid[i, j+1:], grid[i-1::-1, j], grid[i+1:, j]]
    for region in regions:
        viewing_distance = 0
        for adjacent_tree in region:
            viewing_distance += 1
            if adjacent_tree >= current_tree:
                break
            else:
                continue
        score *= viewing_distance
    return score

file = open("day8_complex.txt", "r")
rows = file.read().splitlines()
grid = np.array(list(map(list, rows)), dtype=int)
m, n = grid.shape
current_max = 0

for i in range(1,m-1):
        for j in range(1,n-1):
            score = scenic_score(i,j, grid)
            if current_max < score:
                current_max = score

print(current_max)

file.close()


