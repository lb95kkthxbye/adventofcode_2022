import sys
import math

sys.set_int_max_str_digits(50000)

class Monkey:
    def __init__(self, number, number_of_inspects, items, operation, test, dest_true, dest_false):
        self.number = number
        self.number_of_inspects = number_of_inspects
        self.items = items
        self.operation = operation
        self.test = test
        self.dest_true = dest_true
        self.dest_false = dest_false

    def __str__(self):
        return f"(ID: {self.number}, Number of Inspections: {self.number_of_inspects}, Items: {self.items})"

    def play(self):
        self.number_of_inspects += 1
        item_to_play = self.items.pop(0)
        new_value = math.floor((eval(self.operation.replace("old", str(item_to_play)))))
        if (int(new_value) % int(self.test)) == 0:
            return self.dest_true, new_value
        else:
            return self.dest_false, new_value

    def has_items(self):
        return len(self.items) > 0
    
    def give_item(self, item):
        self.items.append(item)

lines = open("input.txt", "r").read().split("\n\n")
monkeys = []
rounds = 10000
list = []
pops = 2

for i in range(len(lines)):
    monkey_text = lines[i].split("\n")
        #gives us the individual texts for all the monkeys as one element
    number = int(str(monkey_text[0]).split(" ")[1][0:-1])
    print(number)
        #gives us the number of the monkey
    items = monkey_text[1].split(": ")[1].split(", ")
    print(items)
        #gives us an array of the items with their care value
    operation = monkey_text[2].split("= ")[1]
    print(operation)
        #gives us the operation to define the outcome care value
    test = monkey_text[3].split(" ")[5]
    print(test)
        #tests, if the result is dividable by test (with %)
    dest_true = monkey_text[4].split(" ")[-1]
    print(dest_true)
    dest_false = monkey_text[5].split(" ")[-1]
    print(dest_false)

    monkey = Monkey(number, 0, items, operation, test, dest_true, dest_false)
    monkeys.append(monkey)

for i in range(rounds):
    for monkey in monkeys:
        while monkey.has_items():
            dest, value = monkey.play()
            monkeys[int(dest)].give_item(value)
    
    if i % 1000 == 0:
        print(f'Round {i}:')
        for monkey in monkeys:
            print(monkey) 

for monkey in monkeys:
    list.append(monkey.number_of_inspects)
    print(monkey.number_of_inspects)

sorted_list = sorted(list)
val_1 = sorted_list.pop()
val_2 = sorted_list.pop()

result = val_1 * val_2
    
print(result)