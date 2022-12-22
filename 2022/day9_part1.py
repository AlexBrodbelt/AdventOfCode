import numpy as np

positions = set()
head = np.array([0,0])
head_new = np.array([0,0])
tail = np.array([0,0])


def pythagorean_distance(H, T):
    """pythagorean distance of position vectors H and T"""
    return (H[0] - T[0])**2 + (H[1]- T[1])**2 

def get_direction(direction):
    """returns vector associated to the direction"""
    match direction:
        case "R":
            return np.array([1,0])
        case "L":
            return np.array([-1,0])
        case "U":
            return np.array([0,1])
        case "D":
            return np.array([0,-1])
        case other:
            raise ValueError(f"Invalid direction: {direction}")

if __name__ == "__main__":
    with open("day9_complex.txt", "r") as file:
        for line in file:
            direction, distance = line.rstrip().split() # get direction and distance
            #print(direction, distance)
            distance = int(distance) # cast to integer
            direction_vector = get_direction(direction)
            for _ in range(distance):
                head_new = head + direction_vector
                #print(f"new head {head_new}, head {head}, tail {tail}")
                if pythagorean_distance(head_new, tail) > 2: # update tail<-head
                    #print("pythagorean ditance" , pythagorean_distance(head_new, tail))
                    tail = head
                    positions.add(tuple(tail))
                head = head_new

    print(len(positions) + 1)
    

        



