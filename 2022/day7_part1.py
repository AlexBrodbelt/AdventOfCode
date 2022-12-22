from treelib import Node, Tree

tree = Tree()
path = []
identifiers = {"root":0}
counter = 1

def generate_id(path, dirname):
    global counter, identifiers
    full_path = "/".join(path) + "/" + dirname
    if full_path not in identifiers:
        identifiers[full_path] = counter
        counter += 1
    return identifiers[full_path]

    
def get_id(path):
    full_path = "/".join(path)
    if full_path not in identifiers:
        raise LookupError(full_path, "is an invalid path")
    else:
        return identifiers[full_path]

def read_command(line):
    """read the line and determine if its a command starting with a $ or its creating a file"""
    global tree, path
    match line.split():
        case ["$", "cd", arg]:
            change_directory(arg)
        case ["dir", dirname]:
            tree.create_node(tag=dirname, identifier=generate_id(path, dirname), parent=get_id(path))
        case ["$", "ls"]:
            pass
        case [size, filename]:
            tree.create_node(tag=filename, identifier=generate_id(path, filename), parent=get_id(path), data=int(size))
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
smallest_file_to_remove = float("inf")

with open("day7_complex.txt", "r") as file:
    tree.create_node(tag="Root", identifier=0)
    for line in file:
        read_command(line.rstrip())
    tree.show()
    unused_space = 70000000 - size_of_dir(tree.get_node(0))
    size_to_remove = 30000000 - unused_space
    for node in tree.all_nodes():
        current_size = size_of_dir(node) 
        if (current_size >= size_to_remove) and (current_size < smallest_file_to_remove):
            smallest_file_to_remove = current_size
print(smallest_file_to_remove)


    
        

        
            
















    
