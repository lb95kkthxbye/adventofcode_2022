import sys

"""
2-3,1-5

2 > 1, 3 < 5
a0 > b0 & a1 < b1

1-5,2-3
a[0] < b[0] & a[1] > b[1]



"""

def string_numbers(c):
    return list(range(int(c[0]), int(c[1])+1))

all_lines = open("input", "r").readlines()
contained_lines = 0

for i in range(len(all_lines)):
    limits = all_lines[i].strip('\n').split(',')
    if len(set(string_numbers(limits[0].split("-"))).intersection(set(string_numbers(limits[1].split("-"))))) > 0:
        contained_lines += 1

print(contained_lines)