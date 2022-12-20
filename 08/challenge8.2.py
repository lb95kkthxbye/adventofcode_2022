import sys

def row(matrix, i):
    return matrix[i]

def column(matrix, i):
    return [row[i] for row in matrix]

line = open("input.txt", "r").read().split("\n")
compare = 0
compare_new = 0

for i in range(len(line)):
    for j in range(len(line[i])):
        factor_zero = 0
        factor_west = 0
        factor_east = 0
        factor_north = 0
        factor_south = 0
        if i == 0 or j == 0 or i == len(line)-1 or j == len(line[i])-1:
            factor_zero = 0
        else:
            factor_zero = 1
            compare = compare_new
            offset = 1
            while j- offset >= 0:
                if line[i][j] > line[i][j - offset]:
                    factor_west += 1
                    offset += 1
                else:
                    factor_west += 1
                    break
            offset = 1
            while j+ offset < len(line[i]):
                if line[i][j] > line[i][j + offset]:
                    factor_east += 1
                    offset += 1
                else:
                    factor_east += 1
                    break
            offset = 1
            while i- offset >= 0:
                if line[i][j] > column(line, j)[i - offset]:
                    factor_north += 1
                    offset += 1
                else:
                    factor_north += 1
                    break
            offset = 1
            while i+ offset < len(line[i]): 
                if line[i][j] > column(line, j)[i + offset]:
                    factor_south += 1
                    offset += 1
                else:
                    factor_south += 1
                    break
            factor_all = factor_zero*factor_west*factor_east*factor_north*factor_south
            if factor_all > compare:
                compare_new = factor_all
            print(f'position: {i},{j}  ({factor_zero}*{factor_west}*{factor_east}*{factor_north}*{factor_south})')
            print(factor_all)
            print(compare)            