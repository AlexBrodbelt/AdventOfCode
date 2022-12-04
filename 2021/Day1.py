f = open("input.txt", "r").read()
count, j = 0, 0  

lines = f.splitlines()

"""for i in lines:
    i = int(i)
    if i > j:
        count += 1
    j = i
print(count-1)"""



for i in range(len(lines)):
    k, l = sum(map(int,lines[i:i+3])), sum(map(int,lines[i+1:i+4]))
    if l  > k:
        count += 1
print(count)
