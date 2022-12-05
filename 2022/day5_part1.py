import re

flag = False

stack_lines = []

stacks = []


def read_instruction(instruction):
    params = re.findall("[0-9]+", instruction)
    m, f, t = map(int, params)
    return m, f-1, t-1 # to correct indices

def get_crates(line):
    crate = ""
    crates = []
    for i, char in enumerate(line):
        if (i+1) % 4 == 0:
            crates.append(crate)
            crate = ""
        else:
            crate += char
    crates.append(crate)
    return crates            


    

def process_lines(stack_lines, reference):
    stacks = [ list() for _ in range(len(reference.split()))]
    for line in stack_lines:  
        for i,crate in enumerate(get_crates(line)):
            if crate != "   ":
                stacks[i].insert(0, crate)
    return stacks
                
    
with open("day5_complex.txt", "r") as file:
    for line in file:
        if flag:
            line = line.rstrip()
            m, f, t = read_instruction(line)
            for motion in range(m):
                if stacks[f]:
                    crate = stacks[f].pop()
                    stacks[t].append(crate)
                else:
                    raise IndexError("no crates in this stack")

        else:
            if line ==  "\n":
                flag = True 
                stacks = process_lines(stack_lines, reference)

            elif bool(re.search("\s[0-9]", line)):
                reference = line.rstrip()

            else:
                stack_lines.append(line.rstrip())


print("".join([stack.pop()[1] for stack in stacks]))




        
