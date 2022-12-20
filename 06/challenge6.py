"""
We have a string of letters in a row. We need to find the first sequence of 4 letters, in which no letter appears more than once. 

1. We want to form groups of 4 letters that we check. -> The indicator should always move forward 1 space.
    for i in range(len(line)):
        group_letters = line[i:i+4]

2. We want to check this group for duplicates

"""

import sys

line = open('input.txt', 'r').read()

for i in range(len(line)-3):
    sublist = line[i-14:i]
    if len(set(sublist)) == 14:
        break
print(i)