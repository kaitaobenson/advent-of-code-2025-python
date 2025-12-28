# Count the number of times a circular dial from 0 - 99
# LANDS ON 0 during a sequence of turns
# Puzzle answer: 1071
pos = 50
hit_zero_counter = 0

lines = open("Day_01/Day1Input.txt").read().splitlines()

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == "R":
        amount *= 1
    elif direction == "L":
        amount *= -1
    
    pos += amount
    pos %= 100

    if pos == 0:
        hit_zero_counter += 1

print(hit_zero_counter)