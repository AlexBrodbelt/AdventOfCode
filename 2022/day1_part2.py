biggest = second_biggest = third_biggest = 0

top_three_elves = [biggest, second_biggest, third_biggest]

curr_elf = 0

def push_over(lst, i, num):
    pushed_in = num
    for j in range(3-i):
        pushed = lst[i+j]
        lst[i+j] = pushed_in
        pushed_in = pushed
    return lst

with open("day1_complex.txt", 'r') as file:
    for line in file:
        if line != "\n":
            curr_elf += int(line)
        else:
            for i in range(3):
                if curr_elf > top_three_elves[i]:
                    top_three_elves = push_over(top_three_elves, i, curr_elf)
                    break
            curr_elf = 0
    for i in range(3):
        if curr_elf > top_three_elves[i]:
            top_three_elves = push_over(top_three_elves, i, curr_elf)

print(sum(top_three_elves))
    

