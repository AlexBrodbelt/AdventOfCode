cycle = 0
X = 1
checkpoints = [20+40*i for i in range(6)]

sum_of_signal_strengths = 0

def check_cycle():
    global sum_of_signal_strengths, X, cycle
    if cycle in checkpoints:
        sum_of_signal_strengths += X * cycle 
        print(X * cycle, X, cycle)



def read_instruction(line):
    global cycle, X
    match line.split():
        case ["noop"]:
            cycle += 1
            check_cycle() #
        case ["addx", number]:
            cycle += 1
            check_cycle() # begins execution
            cycle += 1
            check_cycle() # execution finishes
            X += int(number) 
if __name__ == "__main__":
    with open("day10_complex.txt", "r") as file:
        for line in file:
            read_instruction(line.rstrip())


    print(sum_of_signal_strengths)