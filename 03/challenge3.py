import sys

all_lines = open("input", "r").readlines()
bucket = 0

def letter_value(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27

def contains(to_compare: str, backpack: str) -> int:
    if len(to_compare) != 1:
        print("error")
    if to_compare in backpack:
        print("letter found: " + str(int(letter_value(to_compare))))
        return int(letter_value(to_compare))
    else:
        return 0

for i in range(len(all_lines)):
    first_backpack = all_lines[i][0:int(len(all_lines[i])/2)]
    second_backpack = all_lines[i][int(len(all_lines[i])/2):]
    print(first_backpack)
    print(second_backpack)

    for j in range(len(first_backpack)):
        found = contains(first_backpack[j],second_backpack)
        if found > 0:
            bucket += found
            break

print(bucket)