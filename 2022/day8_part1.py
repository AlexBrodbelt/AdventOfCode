import numpy as np

def is_visible(i,j, grid):
    """determines if 'tree' in i-jth position in the grid (numpy array) is visible"""
    current_tree = grid[i,j]
                      #left-row    right-row      top_col      bottom_col 
    regions = [grid[i, :j], grid[i, j+1:], grid[:i, j], grid[i+1:, j]]
    for region in regions:
        visible = True # reset flag to true
        for adjacent_tree in region:
            if adjacent_tree >= current_tree:
                visible = False # adjacent tree is taller than the current tree, therefore not visible from this regions direction
                break # no need to check for more adjacent trees, so break inner loop
        if visible: # if visible from a direction, the tree is visible
            return True
    return False # if no visible regions, return false

if __name__ == "__main__":   
    file = open("day8_complex.txt", "r")
    rows = file.read().splitlines()
    grid = np.array(list(map(list, rows)), dtype=int)
    m, n = grid.shape
    visible_tree_count = 2 *(m-1) + 2*(m-1) # initialize count with number of trees on the edge    
    for i in range(1,m-1):
        for j in range(1,n-1):
            if is_visible(i,j, grid):
                visible_tree_count += 1

    print(visible_tree_count)


    file.close()
