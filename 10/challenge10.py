import sys

lines = open("input.txt", "r").read().split("\n")
cycles = 1
x_factor = 1
slogan_input = {}
slogan_sum = 0

for i in range(len(lines)):
    input = lines[i].split(" ")
    if input[0] == "noop":
        cycles += 1
        if cycles == 20 or ((cycles + 20) % 40) == 0:
            slogan_input[cycles] = cycles * x_factor
            slogan_sum += slogan_input[cycles]
    if input[0] == "addx":
        cycles += 1
        if cycles == 20 or ((cycles + 20) % 40) == 0:
            slogan_input[cycles] = cycles * x_factor
            slogan_sum += slogan_input[cycles]
        cycles += 1
        x_factor += int(input[1])
        if cycles == 20 or ((cycles + 20) % 40) == 0:
            slogan_input[cycles] = cycles * x_factor
            slogan_sum += slogan_input[cycles]
    # print(input, cycles, x_factor)
print(slogan_input)
print(slogan_sum)