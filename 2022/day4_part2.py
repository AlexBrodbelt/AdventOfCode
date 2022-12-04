
def overlap(range1, range2):
    start1, end1 = range1.split("-")
    start2, end2 = range2.split("-")
    if (int(end1) < int(start2)) or (int(end2) < int(start1)): # 4-6 2-3
        return False
    else:
        return True

overlaps = 0

with open("day4_complex.txt", "r") as file:
    for line in file:
        range_elf1, range_elf2 = line.split(",")
        if overlap(range_elf1, range_elf2):
            overlaps += 1

print(overlaps)
