import re

path = []


ROOT = 1
PARENT = 2
CURR = 3
CHILD = 4

class Tree:

    def __init__(self):
        prev_level = None
        root_dict = dict()
        prev_dict = None
        curr_dict = None
        """Look into using a doubly linked list with the value being the dictionary, prev being the parent, next being ..."""
        

    def add_element(self, level, name, content):
        if content == "dir":
            self.add_branch(level, name)
        else:
            self.add_leaf(level, name, content)

    def add_leaf(self):
        self.curr_dict[name] = content
        return

    def add_branch(self, level, name):
        if level == 0:
            self.create_branch(ROOT, level, name)
            return

        elif self.prev_level > level:
            self.create_branch(CHILD, level, name)
            return

        elif self.prev_level < level:
            self.create_branch(PARENT, level, name)
            return
        else:
            self.create_branch(CURR, level, name)
            return

    def create_branch(self, branch, level, name):
        match branch:
            case ROOT:
                pass
            case CHILD:
                pass
            case CURR:
                pass
            case PARENT:
                pass
        return

def read_command(line):
    """read the line and determine if its a command starting with a $ or its creating a file"""
    pass







def parse_tree(lines):
    """
    Parse an indented outline into (level, name, parent) tuples.  Each level
    of indentation is 2 spaces.
    """
    #regex = re.compile(r'^(?P<indent>(?: {2})*)(?P<name>\S.*)')
    regex = re.compile(r'^(?P<indent>(?: {2})*)(?:- )(?P<name>[^\s]+)(?:\s\()(?P<content>\S.*)') # regex can be improved
    stack = []
    for line in lines:
        match = regex.match(line)
        if not match:
            raise ValueError(
                'Indentation not a multiple of 2 spaces: "{0}"'.format(line)
            )
        level = len(match.group('indent')) // 2
        if level > len(stack):
            raise ValueError('Indentation too deep: "{0}"'.format(line))
        stack[level:] = [match.group('name')]
        yield level, match.group('name'), match.group('content'), (stack[level - 1] if level else None)

with open("day7_simple.txt", "r") as file:
    tree = Tree()
    raw = file.read()
    stack = []
    for level, name, content, parent in parse_tree(raw.split('\n')):
        tree.add_element(level, name, content) # needs to be worked more   
        print('{0} {1} ( {2} ) parent ( {3} )'.format(level, name, content, parent or 'root'))
    
