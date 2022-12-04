from os import error


input = open("input8.txt", "r").read().splitlines()
input1 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()
input1 = list(map(lambda item: item.split("|"), input1))

#print(input)
#vals = {'0': ('a', 'b', 'c', 'e','f','g'), '1':('c', 'f'), '2':('a','c','d','e','g')}
counts = {8:('a','c'), 6:'b', 7:('d','g'), 4:'e',9:'f'}
count = 0
letters = ('a', 'b','c','d','e','f','g')

new_digits = []

total = 0

def get_key(D, value):
    for key, val in zip(D.keys(),D.values()):
        if val == value:
            return key
    return error

for unique_pattern, output in input1:
    D = {}
    digits = unique_pattern.strip().split()
    for i, digit in enumerate(digits):
        if len(digit) == 2:
            D[tuple(sorted(digit))] = "1"
        elif len(digit) == 4:
            D[tuple(sorted(digit))] = "4"
        elif len(digit) == 3:
            D[tuple(sorted(digit))] = "7"
        elif len(digit) == 7:
            D[tuple(sorted(digit))] = "8"
        
        if len(digit) not in [2,3,4,7]:
            new_digits.append(digit)

    one = get_key(D,"1")
    four = get_key(D,"4")

    for digit in new_digits:
        if (len(digit) == 5) & (all([x in digit for x in one])):
                D[tuple(sorted(digit))] = "3"
            

        if (len(digit) == 6):
            if (all([x in digit for x in one])):
                if (all([x in digit for x in four])):
                    D[tuple(sorted(digit))] = "9"
                else:
                    D[tuple(sorted(digit))] = "0"
            else:
                D[tuple(sorted(digit))] = "6"

    six = get_key(D,"6")

    for digit in new_digits:
        if (len(digit) == 5):
            if (all([x in six for x in digit])):
                D[tuple(sorted(digit))]  = "5"
            else:
                D[tuple(sorted(digit))] = "2" 
    four_digit = "" 

    numbers = output.strip().split() 

    for nums in numbers:
        four_digit += D[tuple(sorted(nums))]
    print(output, four_digit)

    total += int(four_digit)


print(total)

        

#the code above should work

"""for digit in digits:
    
    if (len(digit) == 5):
        if (all([x in digit for x in one])):
            D[sorted(digit)] = "3"
        else:
            D[sorted(digit)] = "2"

four_digit = ""
for number in output:
    four_digit += D[sorted(number)]
    
count += int(four_digit)"""

