def find_marker(datastream):
    for i in range(len(datastream)-14):
        if len(set(datastream[i:i+14])) == 14:
            return i + 14
    raise LookupError("There is no start-of-message marker")




with open("day6_complex.txt", "r") as file:
    for line in file:
        print(find_marker(line.rstrip()))