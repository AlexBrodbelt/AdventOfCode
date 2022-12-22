import numpy as np
from day9_part1 import pythagorean_distance, get_direction

positions = set()
knots = np.zeros((10,2))
knots_new = np.zeros((10,2))


def update_knot(knots_new, knots, i):
    difference = knots_new[i] - knots[i+1]
    dir = np.sign(difference) * np.array([1,1])
    #knots_new[i+1] = knots[i].copy()
    knots_new[i+1] = knots[i+1] + dir
    return



def update_knots(knots_new, knots, i):
    if i < 8:
        if pythagorean_distance(knots_new[i], knots[i+1]) > 2:
            update_knot(knots_new, knots, i) # tail of ith-knot moves to ith-knots previous position
            update_knots(knots_new, knots, i+1)
        else: # tail of ith-knot does not move
            return 
    elif i == 8: # update last knot of the rope
        if pythagorean_distance(knots_new[i], knots[i+1]) > 2:
            update_knot(knots_new, knots, i) # tail of ith-knot moves to ith-knots previous position
            positions.add(tuple(knots_new[9])) # record position change
        else: # tail of ith-knot does not move
            return
    else: # has already reached end of the rope - must not reach this case
        raise IndexError(f"invalid index {i}")
    
if __name__ == "__main__":
    with open("day9_complex.txt", "r") as file:
        for line in file:
            direction, distance = line.rstrip().split() # get direction and distance
            distance = int(distance) # cast to integer
            direction_vector = get_direction(direction)
            for _ in range(distance):
                knots_new[0] = knots[0].copy() + direction_vector
                update_knots(knots_new, knots, 0)
                knots = knots_new.copy()

    print(len(positions) + 1)