import sys
import numpy as np

def move_head(input, head):
    if input == "U":
        head['y'] += 1
    elif input == "D":
        head['y'] -= 1
    elif input == "L":
        head['x'] -= 1
    elif input == "R":
        head['x'] += 1
    return head        

def move_tail(head, tail):
    if abs(head['x'] - tail['x']) > 1 or abs(head['y'] - tail['y']) > 1:
        tail['x'] += np.sign(head['x'] - tail['x'])
        tail['y'] += np.sign(head['y'] - tail['y'])
    return tail

chain = [
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0}
    ]
line = open("input.txt", "r").read().split("\n")
positions = set()

for i in range(len(line)):
    input = line[i].split(" ")
    for j in range(int(input[1])):
        # print(input[0], input[1])
        for k in range(len(chain)):
            if k == 0:
                chain[0] = move_head(input[0], chain[0])
            else:
                chain[k] = move_tail(chain[k-1], chain[k])
                if k == 9:
                    positions.add((chain[k]['x'], chain[k]['y']))

print(len(positions))

"""
def print_board(head, tail):
    print('\n')
    for i in range(10):
        s = ''
        for j in range(10):
            if head['x'] == j and head['y'] == i:
                s += 'H'
            elif tail['x'] == j and tail['y'] == i:
                s += 'T'
            elif j == 0 and i == 0:
                s += 's'
            else:
                s += '.'
        print(s)

class TestTailMovement(unittest.TestCase):
    def test_tail_movement(self):
        expected = {'x': 1, 'y': 1}
        actual = move_tail({'x': 2, 'y': 1}, {'x': 0, 'y': 0})
        self.assertEqual(actual, expected)
        expected = {'x': -1, 'y': -1}
        actual = move_tail({'x': -2, 'y': -1}, {'x': 0, 'y': 0})
        self.assertEqual(actual, expected)
        expected = {'x': 1, 'y': 0}
        actual = move_tail({'x': 2, 'y': 0}, {'x': 0, 'y': 0})
        self.assertEqual(actual, expected)
        expected = {'x': 0, 'y': 1}
        actual = move_tail({'x': 0, 'y': 2}, {'x': 0, 'y': 0})
        self.assertEqual(actual, expected)
        expected = {'x': 0, 'y': 0}
        actual = move_tail({'x': 0, 'y': 1}, {'x': 0, 'y': 0})
        self.assertEqual(actual, expected)
        expected = {'x': 0, 'y': 0}
        actual = move_tail({'x': 1, 'y': 1}, {'x': 0, 'y': 0})
        self.assertEqual(actual, expected)
"""