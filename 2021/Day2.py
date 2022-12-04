lines = open("input2.txt", "r").read().splitlines()
horizontal, depth, aim = 0, 0, 0  

lines1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()


for line in lines:
    command, value = line.split(" ")
    value = int(value)
    if command == "forward":
        horizontal += value
    elif command == "down":
        depth += value
    else:
        depth -= value

"""for line in lines:
    command, value = line.split(" ")
    value = int(value)
    if command == "forward":
        horizontal += value
        depth += value*aim
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value"""


print(horizontal,depth)