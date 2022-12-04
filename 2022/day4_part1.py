
def isSubset(range1, range2):
    start1, end1 = range1.split("-")
    start2, end2 = range2.split("-")
    if (int(start1) <= int(start2)) and int(end2) <= int(end1):
        return True
    elif (int(start2) <= int(start1)) and int(end1) <= int(end2):
        return True
    else:
        return False


pairs = 0

with open("day4_complex.txt", "r") as file:
    for line in file:
        range_elf1, range_elf2 = line.split(",")
        if isSubset(range_elf1, range_elf2):
            pairs += 1

print(pairs)

