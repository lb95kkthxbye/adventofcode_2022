import sys

def add_to_directories(directories, current_path, value):
    print('add_to_directories called')
    list_of_dirs = current_path.split('/')
    tmp_dir = ''
    for i in range(len(list_of_dirs)):
        tmp_dir += '/'+list_of_dirs[i]
        value = directories.get(tmp_dir)
        if value:
            directories[tmp_dir] += int(line[0])
        else:
            directories[tmp_dir] = int(line[0])

all_lines = open("input.txt", "r").read().split('\n')

directories = {}
current_path = ''
directories['root'] = 0

for i in range(len(all_lines)):
    if all_lines[i] == '':
        break
    elif all_lines[i] == '$ ls':
        j = 1
        while True:
            line = all_lines[i + j].split(' ')
            if line[0] == '$':
                break
            if line[0] == '':
                break
            else:
                if line[0].isnumeric():
                    add_to_directories(directories, current_path, line[0])
                j += 1
        print('ls')
    elif '$ cd ' in all_lines[i]:
        if all_lines[i][5:] == '/':
            current_path = 'root'
        elif all_lines[i][5:] == '..':
            current_path = '/'.join(current_path.split('/')[0:-1])
        else:
            current_path = current_path + '/' + all_lines[i][5:]

sum = 0

for k,v in directories.items():
    print(str(k) + ' => ' + str(v))
    sum += v

print("Total mem used:")
total_mem = directories['/root']
print("Total memory free")
print(70000000 - total_mem)
print("At least clean up")
print(30000000- (70000000 - total_mem))

mem_to_clean_up = 30000000- (70000000 - total_mem)
min = 9999999999999999999

for k,v in directories.items():
    if (v > mem_to_clean_up) and (v < min):
        min = v

print(min)