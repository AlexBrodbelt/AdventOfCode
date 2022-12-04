bingo ="""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n\n")

row_nums = "22 8 21 6 1".split()

real_bingo = lines = open("input4.txt", "r").read().split("\n\n")

nums = real_bingo[0].split(",")


tables = list(map(lambda xs: list(map(lambda ys : list(map(lambda zs : [zs,0] , [x for x in ys.split(" ") if x != ''])) , xs.splitlines())), real_bingo[1::]))

def mark(nums, table):
    for n in nums:
        for row in table:
            for number in row:
                if number[0] == n:
                    number[1] = 1
    return table


def check_row(table):
    ans = 1
    for i, row in enumerate(table):
        for number, bit in row:
            ans &= bit
        if ans:
            return (i, 1)
        ans = 1 
    return (i,0)


def check_column(table):
    ans = 1
    table = map(list, zip(*table)) #transposes matrix
    for i, row in enumerate(table):
        for number, bit in row:
            ans &= bit
        if ans:
            return (i, 1)
        ans = 1 
    return (0, 0)

def check(table):
    if check_row(table)[1]:
        return check_row(table)
    elif check_column(table)[1]:
        return check_column(table)
    else:
        return (0, 0) #first zero is just for tuple format





"""bit = 1
for n in range(len(nums)):
    if bit:
        for i, table in enumerate(tables):
            if check(mark(nums[:n], table))[1] == 1:
                print("table", i, "with numbers",  nums[:n], "pulled out")
                print("the resulting table being", mark(nums[:n], table))
                print("with score being",sum([int(num) for row in table for num, bit in row if not bit])*int(nums[n-1])) #sum of unmarked numbers 
                bit = 0
                break
    else:
        break"""

completed_tables = set()

all_tables = set(range(len(tables)))

bit = 1
for n in range(len(nums)):
    if bit:
        for i, table in enumerate(tables):
                if check(mark(nums[:n], table))[1] == 1 and (i not in completed_tables):
                    completed_tables.add(i)
                    if completed_tables == all_tables:
                        print("table",i, "with score being",sum([int(num) for row in table for num, bit in row if not bit])*int(nums[n-1]))
                        bit = 0
                        break
                    #print(i,nums[:n], completed_tables)
                    
            
    else:
        break
                
                

      
      
#print("with score being",sum([int(num) for row in tables[j] for num, bit in row if not bit])*int(nums[n-1])) #sum of unmarked numbers



