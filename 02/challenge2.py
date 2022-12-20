import sys

def nominalize_sign(sign):
    if ord(sign) > 68:
        return (ord(sign) - 67) % 3
    return (ord(sign) - 65) % 3

def calculate_my_points(sign):
    return sign + 1

def play(sign_player_1, sign_player_2):
    if (sign_player_1 + 1) % 3 == sign_player_2:
        return 6 + calculate_my_points(sign_player_2)
    elif (sign_player_1 == sign_player_2):
        return 3 + calculate_my_points(sign_player_2)
    else:
        return calculate_my_points(sign_player_2)

all_lines = open("input", "r").readlines()
sum_1 = 0
sum_2 = 0

for i in range(len(all_lines)):
    sum_1 += play(nominalize_sign(all_lines[i][0]), nominalize_sign(all_lines[i][2]))
    sum_2 += play(nominalize_sign(all_lines[i][0]), (nominalize_sign(all_lines[i][0]) + nominalize_sign(all_lines[i][2]) + 2) % 3)

print("Part one: " + str(sum_1))
print("Part two: " + str(sum_2))
