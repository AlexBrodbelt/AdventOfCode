import re

flag = False

stack_lines = []

stacks = []

from day5_part1 import read_instruction, process_stack_lines
                
    
with open("day5_complex.txt", "r") as file:
    for line in file:
        if flag:
            line = line.rstrip()
            m, f, t = read_instruction(line)
            crates = stacks[f][-m:] # might present an error
            del stacks[f][-m:] # delete elements
            stacks[t].extend(crates)
        else:
            if line ==  "\n":
                flag = True 
                stacks = process_stack_lines(stack_lines, reference)

            elif bool(re.search("\s[0-9]", line)):
                reference = line.rstrip()

            else:
                stack_lines.append(line.rstrip())


print("".join([stack.pop()[1] for stack in stacks]))