from treelib import Node, Tree

tree = Tree()
path = []

dirnames = dict()

def read_command(line):
    """read the line and determine if its a command starting with a $ or its creating a file"""
    global tree, path
    match line.split():
        case ["$", "cd", arg]:
            change_directory(arg)
        case ["dir", dirname]:
            tree.create_node(tag=dirname, identifier=dirname, parent=path[-1])
        case ["$", "ls"]:
            pass
        case [size, filename]:
            tree.create_node(tag=filename, identifier=filename, parent=path[-1], data=int(size))
        case other:
            pass
        
def change_directory(arg):
    global path
    match arg:
        case "/":
            path = ["root"]
        case "..":
            path.pop()
        case other:
            path.append(arg)

def size_of_dir(node):
    total = 0
    for children in tree.leaves(node.identifier):
        total += children.data
    return total


total = 0

with open("day7_complex.txt", "r") as file:
    tree.create_node(tag="Root", identifier="root")
    for line in file:
        read_command(line.rstrip())
    tree.show()
    for node in tree.all_nodes():
        if node.data == None:
            if size_of_dir(node) <= 100000:
                total += size_of_dir(node)

print(total)

    
        

        
            
















    
