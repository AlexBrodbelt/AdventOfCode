test = """11111
19991
19191
19991
11111"""

test = test.splitlines()

test = list(map(lambda x: list(map(int,list(x))), test))

#print(list(test))

flashes = 0

m = len(test)
n = len(test[0])

def check(i,j):
    global test, flashes, m, n
    if test[i][j] >= 9:
        print(i,j)
        flashes += 1
        for k in range(-1,2):
            for l in range(-1,2):
                if (k != 0) and (l != 0):
                    i_, j_ = i+k, j+l
                    if (i_ < m) and (-1 < i_) and (j_ < m) and (-1 < j_):
                        test[i_][j_] += 1
                        check(i_, j_)
        return 0
    if test[i][j] != 9:
        return test[i][j]



steps = 1



for step in range(steps):
    test = list(map(lambda x: list(map(lambda y: y+1, x)), test))
    for i in range(m):
        for j in range(n):
            if test[i][j] >= 9:
                flashes += 1
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (k != 0) or (l != 0):
                            i_, j_ = i+k, j+l
                            if (i_ < m) and (-1 < i_) and (j_ < m) and (-1 < j_):
                                print(test[i_][j_], i_, j_ , "originating from", i, j)
                                test[i_][j_] += 1
                test[i][j] = 0

            


"""if test[i][j] == 9:
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (k != 0) and (l != 0):
                            i_, j_ = i+k, j+l
                            if (i_ < m) and (-1 < j_) and (j_ < m) and (-1 < j_):
                                test[i_][j_] += 1
                                if test[i_][j_] == 9:
                                    test[i_][j_] = 0"""
        
def pretty(matrix):
    matrix = list(map(lambda x: list(map(str, x)), matrix)) 
    return "\n".join(list(map(lambda x: "".join(x),matrix)))
print(pretty(test))

print(flashes)

