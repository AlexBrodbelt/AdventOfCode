def find_marker(datastream):
    for i in range(len(datastream)-4):
        if len(set(datastream[i:i+4])) == 4:
            return i + 4




with open("day6_complex.txt", "r") as file:
    for line in file:
        print(find_marker(line.rstrip()))
