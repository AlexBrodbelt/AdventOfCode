max_calories = 0
temp_calories = 0
with open("day1_complex.txt", 'r') as file:
    for line in file:
        if line == "\n":
            if temp_calories > max_calories:
                max_calories = temp_calories
            #print(temp_calories)
            temp_calories = 0
        else:
            temp_calories += int(line)
    #print(temp_calories)
    if temp_calories > max_calories:
        max_calories = temp_calories

print(max_calories)

