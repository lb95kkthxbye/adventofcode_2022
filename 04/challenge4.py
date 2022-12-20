import sys

"""
2-3,1-5

2 > 1, 3 < 5
a0 > b0 & a1 < b1

1-5,2-3
a[0] < b[0] & a[1] > b[1]



"""

def fully_contained(a, b) -> bool :
    """
    Test if the array a is contained in array b or vice versa:
    2-3,1-7
    a = [2,3]
    b = [1,7]

    a is fully contained in b

    => fully_conatiner(a, b) => True
    => fully_contained(b, a) => True
    """
    if (int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])) or (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])):
        return True


all_lines = open("input", "r").readlines()
contained_lines = 0

for i in range(len(all_lines)):
    limits = all_lines[i].strip('\n').split(',')
    if fully_contained(limits[0].split('-'), limits[1].split('-')):
        contained_lines += 1

print(contained_lines)

