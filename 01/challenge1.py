import sys

all_lines = open("input", "r").readlines()
buckets = [0] * int(len(all_lines) / 2 + 1)
current_bucket = 0

for i in range(len(all_lines)):
    if all_lines[i].strip('\n').isnumeric():
        buckets[current_bucket] += int(all_lines[i].strip('\n'))
    else:
        current_bucket += 1

print(buckets)
print("Whats the sum of top three, hon?")

max_0 = 0
max_1 = 0
max_2 = 0

for i in range(len(buckets)):
    to_compare = int(buckets[i])
    if to_compare > max_0:
        print(str(to_compare) + " is bigger than current max_0: " + str(max_0))
        temp = to_compare
        to_compare = max_0
        max_0 = temp
    if to_compare > max_1:
        print(str(to_compare) + " is bigger than current max_1: " + str(max_1))
        temp = to_compare
        to_compare = max_1
        max_1 = temp
    if to_compare > max_2:
        print(str(to_compare) + " is bigger than current max_2: " + str(max_2))
        max_2 = to_compare

print("max 0: " + str(max_0))
print("max 1: " + str(max_1))
print("max 2: " + str(max_2))

print(max_0 + max_1 + max_2)
