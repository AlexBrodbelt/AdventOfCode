from day3_part1 import priority

def find_common_item(rucksack1, rucksack2, rucksack3):
    return (set(rucksack1) & set(rucksack2) & set(rucksack3)).pop() 

sum_of_priorities = 0

with open("day3_complex.txt") as file:
    num_lines = sum(1 for line in file)

with open("day3_complex.txt", "r") as file:
    for _ in range(num_lines//3):
        rucksack1 = file.readline().rstrip() 
        rucksack2 = file.readline().rstrip() 
        rucksack3 = file.readline().rstrip() 
        sum_of_priorities += priority(find_common_item(rucksack1,rucksack2,rucksack3))      

print(sum_of_priorities)