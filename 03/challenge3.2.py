import sys
from itertools import islice

all_lines = open("input", "r").readlines()
bucket = 0

def letter_value(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27

def contains(to_compare: str, backpack: str) -> int:
    """
    Returns letter code of string to_compare if it's contained in string backpack
    """
    if len(to_compare) != 1:
        print("error")
    if to_compare in backpack:
        print("letter found: " + str(int(letter_value(to_compare))))
        return int(letter_value(to_compare))
    else:
        return 0

for i in range(int(len(all_lines) / 3)):
    three_slices = list(islice(all_lines, 0 + (i * 3), 3 + (i * 3)))
    for j in range(len(three_slices[0])):
        found_1 = contains(three_slices[0][j],three_slices[1])
        found_2 = contains(three_slices[0][j], three_slices[2])
    
        if (found_1 > 0) & (found_2 > 0):
            bucket += found_1
            break

print(bucket)