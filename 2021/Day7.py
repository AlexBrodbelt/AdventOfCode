#input = list(map(int,"16,1,2,0,4,2,7,1,2,14".split(",")))

input = list(map(int, open("input7.txt", "r").read().split(",")))

mean = sum(input)/len(input)



print(mean)

def dictify(ls):
    D = {}
    for item in ls:
        if item in D:
            D[item] += 1
        else:
            D[item] = 1
    return D

dictionary = dictify(input)

mode = max(dictionary, key=dictionary.get)

"""slow implementation"""
print(max(input), min(input))

s = sum([int(abs(x-mode)*(abs(x-mode)+1)/2) for x in input])

print(s, mode)

optimal = 0

for position in range(min(input), max(input)+1):
    #print(position)
    new_s  = sum([int(abs(x-position)*(abs(x-position)+1)/2) for x in input])
    if new_s < s:
        s = new_s
        optimal = position


print(s, optimal)

    