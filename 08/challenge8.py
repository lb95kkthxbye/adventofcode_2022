import sys

def row(matrix, i):
    return matrix[i]

def column(matrix, i):
    return [row[i] for row in matrix]

line = open("input.txt", "r").read().split("\n")
visible = 0

for i in range(len(line)):
    for j in range(len(line[i])):
        if i == 0 or j == 0 or i == len(line)-1 or j == len(line[i])-1:
            visible += 1
        elif line[i][j] > max(row(line, i)[0:j]) or \
             line[i][j] > max(row(line, i)[j + 1:]) or \
             line[i][j] > max(column(line, j)[0:i]) or \
             line[i][j] > max(column(line, j)[i + 1:]):
                visible += 1

print(visible)