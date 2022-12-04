f = open("input14.txt","r")
polymer_template, insertion_rules = f.read().split("\n\n")
f.close()

test_insertion_rules = """CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

test_polymer_template = "NNCB"

insertion_rules = dict(map(lambda x: x.split(" -> "), insertion_rules.splitlines()))

insertions = ""

result_polymer = ""

def insert(polymer_template):
    insertions = ""
    result_polymer = ""
    for i in range(len(polymer_template)-1):
        insertions += insertion_rules[polymer_template[i:i+2]]

    for j in range(len(polymer_template)+len(insertions)):
        if j % 2 == 0:
            result_polymer += polymer_template[int(j/2)]; 
        else:
            result_polymer += insertions[int((j-1)/2)]

    return result_polymer


print("into the meat of it")

for i in range(40):
    polymer_template = insert(polymer_template) 

D = {}

for i in polymer_template:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1        
print(D)
most_common = max(D.values())
least_common = min(D.values())

print(most_common-least_common)

print("done")


