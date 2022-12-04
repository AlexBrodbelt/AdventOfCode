def find_common_item(rucksack1, rucksack2):
    letters = set(rucksack1)
    for letter in rucksack2:
        if letter in letters:
            return letter
    raise LookupError("There is no common item in both rucksacks")

def priority(letter):
    if letter.isupper():
        return 26 + ord(letter) - ord('A') + 1
    else:
        return ord(letter) - ord('a') + 1

if __name__ == "__main__":
    sum_of_priorities = 0
    with open("day3_complex.txt", "r") as file:
        for line in file:
            half = len(line) // 2
            sum_of_priorities += priority(find_common_item(line[:half], line[half:]))

    print(sum_of_priorities)