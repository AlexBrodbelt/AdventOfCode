diag_report = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()

lines = open("input3.txt", "r").read().splitlines()

"""count_ones, count_zeros = 0, 0

gamma_rate, epsilon_rate = "", ""

for byte in range(len(lines[0])):
    for bin_num in lines:
        if bin_num[byte] == "1":
            count_ones += 1
        else:
            count_zeros += 1
    if count_ones > count_zeros:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"
    count_ones, count_zeros = 0, 0

print(gamma_rate, epsilon_rate, to_decimal(gamma_rate)*to_decimal(epsilon_rate))"""

def to_decimal(binary):
    return sum([int(i)*(2**n) for i,n in zip(binary[::-1], range(len(binary)))])

count_ones, count_zeros, ones, zeros = 0, 0, [], []

O2, CO2 = "", ""

newlist = lines

print("oxygen generator rating")

for byte in range(len(lines[0])):
    if len(newlist) > 1 :
        for bin_num in lines:
            if bin_num in newlist:
                if bin_num[byte] == "1":
                    count_ones += 1
                    ones.append(bin_num)
                else:
                    count_zeros += 1
                    zeros.append(bin_num)
        if count_ones >= count_zeros:
            newlist = ones
            #print(newlist, "in {} iteration".format(byte)) useful for debugging
        else:
            newlist = zeros
            #print(newlist, "in {} iteration".format(byte)) useful for debugging
        
        if len(newlist) == 1:
            O2 = newlist[0]
            print(O2)
            break

        count_ones, count_zeros, ones, zeros = 0, 0, [], []
    else:
        print(newlist[0])
        break

newlist = lines

count_ones, count_zeros, ones, zeros = 0, 0, [], []

print("CO2 scrubber rating")

for byte in range(len(lines[0])):
    if len(newlist) > 1 :
        for bin_num in lines:
            if bin_num in newlist:
                if bin_num[byte] == "1":
                    count_ones += 1
                    ones.append(bin_num)
                else:
                    count_zeros += 1
                    zeros.append(bin_num)
        if count_ones >= count_zeros:
            newlist = zeros
            #print(newlist, "in {} iteration".format(byte)) useful for debugging
        else:
            newlist = ones
            #print(newlist, "in {} iteration".format(byte)) useful for debugging

        if len(newlist) == 1:
            CO2 = newlist[0]
            print(O2)
            break

        count_ones, count_zeros, ones, zeros = 0, 0, [], []
    else:
        print(newlist[0])
        break

print(to_decimal(O2)*to_decimal(CO2))
