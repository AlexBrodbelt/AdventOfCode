import sympy
from heapq import nlargest
from operator import mul
from functools import reduce

monkey_ids = []
monkey_items = []
monkey_inspections = [0]*8
monkey_operations = []
monkey_throw_to = []

round = 1

file = open("day11_complex.txt", "r")
monkey_file = file.read().split("\n\n")
monkey_file = list(map(lambda x: x.splitlines(), monkey_file))


def get_element(note):
    match note.split():
        case ["Monkey", id]:
            return int(id.strip(":"))
        case ["Starting", "items:", *args]:
            return list(map(lambda x: int(x.strip(",")), args))
        case ["Operation:", "new", "=", *operation]:
            return "".join(operation)
        case ["Test:", "divisible", "by", divisor]:
            return int(divisor)
        case ["If", "true:", "throw", "to", "monkey", id]:
            return int(id)
        case ["If", "false:", "throw", "to", "monkey", id]:
            return int(id)
        case other:
            raise LookupError("invalid note" + note)

def get_operation(string):
    f = sympy.sympify(string) 
    def get_new_item(old):
        result = f.subs({"old": old})
        return result
    return get_new_item

def get_throw_to(monkey_true, monkey_false, divisor):
    def throw_to(item):
        if item % divisor == 0:
            return monkey_true
        else:
            return monkey_false
    return throw_to

def throw_item(item, monkey_id):
    global monkey_items
    operation = monkey_operations[monkey_id]
    new = operation(item)
    new //= 3
    throw_to = monkey_throw_to[monkey_id]
    receiver_monkey = throw_to(new)
    monkey_items[receiver_monkey].append(new)
    

def throw_items(monkey_id):
    global monkey_items, monkey_inspections
    while monkey_items[monkey_id]:
        item = monkey_items[monkey_id].pop()
        monkey_inspections[monkey_id] += 1
        throw_item(item, monkey_id)



# Set-up
for monkey_notes in monkey_file:
    monkey_id = get_element(monkey_notes[0].strip()) # get the id of the moneky
    starting_items = get_element(monkey_notes[1].strip()) # get the starting items of that monkey
    operation = get_operation(get_element(monkey_notes[2].strip())) # get the operation of the monkey
    divisor = get_element(monkey_notes[3].strip()) # get the divisor necessary for the test
    monkey_true = get_element(monkey_notes[4].strip()) # where to throw if test is false
    monkey_false = get_element(monkey_notes[5].strip()) # where to throw if test is true
    throw_to =  get_throw_to(monkey_true, monkey_false, divisor)  # function to determine where to throw | lambda item: monkey_true if item % divisor == 0 else monkey_false
    monkey_ids.append(monkey_id) 
    monkey_items.append(starting_items)
    monkey_operations.append(operation)
    monkey_throw_to.append(throw_to) # function to determine where to throw






while round <= 20:
    for monkey_id in monkey_ids:
        throw_items(monkey_id)
    round += 1

two_largest = nlargest(2, monkey_inspections)

print(two_largest)
print(reduce(mul, two_largest))

file.close()
