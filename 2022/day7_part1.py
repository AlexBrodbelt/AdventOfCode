import re
from treelib import Node, Tree

path = []

FOLDER = -1
FILE = 0
DO_NOTHING = 1

def read_command(line):
    """read the line and determine if its a command starting with a $ or its creating a file"""
    begins = line[0]
    elems = line.split()
    if begins == "$":
        if len(elems) == 3:
            _, command, arg = elems
            return FOLDER, command, arg
        else:
            return DO_NOTHING, None, None
    else:
        value, file_name = line.split()
        return FILE, value, file_name

def change_directory(tree, arg, path):
    if arg == "/":
        return []
    elif arg == "..":
        path.pop()
        return path
    else:
        path.append(arg)
        return path


def parse_command(command, arg):
    pass 

    


with open("day7_simple.txt", "r") as file:
    tree = Tree()
    for line in file:
        command_type, arg1, arg2 = read_command(line)
        if command_type == FILE:
            value, file_name = arg1, arg2
            tree.create_node(value, file_name, path[-1])
        elif command_type == FOLDER:
            
















    
