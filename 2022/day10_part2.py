X = 1
cycle = 0
position = -1
def read_instruction(line):
    global cycle, X, position
    match line.split():
        case ["noop"]:
            cycle += 1; position += 1
            draw_pixel()
        case ["addx", number]:
            cycle += 1; position += 1
            draw_pixel()
            cycle += 1; position += 1
            draw_pixel()
            X += int(number) 

def sprite_range(X):
    return [X-1, X, X+1]


def draw_pixel():
    global cycle, position
    if position == 40:
        print("\n", end="")
        position = 0
    if position in sprite_range(X):
        print("#", end="")
    else:
        print(".", end="")
    
        



with open("day10_complex.txt", "r") as file:
    for line in file:
        read_instruction(line.rstrip())
