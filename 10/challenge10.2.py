import sys

def draw_CRT(x_factor, CRT_position, CRT_print):
    if (CRT_position % 40) == x_factor or (CRT_position % 40) == (x_factor - 1) or (CRT_position % 40) == (x_factor + 1):
            CRT_print += "#"
            CRT_position += 1
    else:
        CRT_print += "."
        CRT_position += 1
    return x_factor, CRT_position, CRT_print 

lines = open("input.txt", "r").read().split("\n")
cycles = 1
x_factor = 1
CRT_position = 0
CRT_print = ''

for i in range(len(lines)):
    input = lines[i].split(" ")
    if input[0] == "noop":
        x_factor, CRT_position, CRT_print = draw_CRT(x_factor, CRT_position, CRT_print)
        cycles += 1

    else:
        x_factor, CRT_position, CRT_print = draw_CRT(x_factor, CRT_position, CRT_print)
        cycles += 1
        x_factor, CRT_position, CRT_print = draw_CRT(x_factor, CRT_position, CRT_print)
        cycles += 1
        x_factor += int(input[1])

for j in range(int(len(CRT_print)/ 40)):
    print(CRT_print[(j*40):((j+1)*40)])