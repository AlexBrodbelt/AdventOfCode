from os import stat


f = open("input10.txt", "r")

input = f.read().splitlines()

f.close()

pairs  = [{"(",")"},{"[","]"},{"{","}"},{"<",">"}]

def match(char1, char2):
    for pair in pairs:
        if (char1 in pair) & (char2 in pair):
            return 1
    return 0

values = {")":3, "]":57, "}":1197, ">":25137}

open = ["[","(","{","<"]

illegal_chars = []

head = ""

record = []

"""for i,line in enumerate(input):
    for j,char in enumerate(line):
        record.append(char)
        if char in open:
            head = char
            #print("new head",head)
        else:
            if match(char, head):
                #print("before",record)
                record.pop(); record.pop() 
                #print("after",record)
                head = record[-1]
                #print("new head from record", head)

            else:
                print("line {}:".format(i+1),char, "doesn't match up with",head, "(symbol {})".format(j+1))
                illegal_chars.append(char)
                break
    print("record",record)    
    record = []

    
print(illegal_chars)

syntax_error_score = 0

for char in illegal_chars:
    syntax_error_score += values[char]

print(syntax_error_score)"""

#part 2

score = 0

scores = []

bracket_match  = {"(":1,"[":2,"{":3,"<":4}


bit = 1


for i,line in enumerate(input):
    bit = 1
    for j,char in enumerate(line):
        record.append(char)
        if char in open:
            head = char
            #print("new head",head)
        else:
            if match(char, head):
                #print("before",record)
                record.pop(); record.pop() 
                #print("after",record)
                head = record[-1]
                #print("new head from record", head)

            else:
                print("line {}:".format(i+1),char, "doesn't match up with",head, "(symbol {})".format(j+1))
                illegal_chars.append(char)
                bit = 0
                break
    if bit:
        print("record",record)
    else:
        print("illegal record", record)
    if bit:
        for symbol in record[::-1]:
            score = 5*score + bracket_match[symbol]
        scores.append(score)
        score = 0
    record = []



scores = sorted(scores)

middle_score = scores[len(scores)//2]

print(middle_score)


