import sys

def get_moves(moves):
    return int(moves.split(' ')[1]), int(moves.split(' ')[3]), int(moves.split(' ')[5])

stacks = [[] for i in range(9)]
all_lines = open("input.txt", "r").read().split('\n\n')
constellation = all_lines[0].split('\n')
moves = all_lines[1].split('\n')

for i in range(len(constellation)):
    if (i != 0):
        line = constellation[len(constellation)- (i + 1)]
        for j in range(9):
            if line[1+(j*4)] != ' ':
                stacks[j].append(line[1+(j*4)])

for i in range(len(moves) - 1):
    rep, src, dest = get_moves(moves[i])
    temps = stacks[src - 1][-rep:]
    stacks[dest - 1] = stacks[dest - 1] + temps
    stacks[src - 1] = stacks[src - 1][0:-rep]

"""
    for j in range(rep):
        temp = stacks[src - 1].pop()
        stacks[dest - 1].append(temp)
"""     

for i in range(len(stacks)):
    print(stacks[i].pop())