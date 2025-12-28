# Count the number of times a circular dial from 0 - 99
# CROSSES 0 during a sequence of turns
# Puzzle answer: 6700

# Note: There is a mathematical way to do this, but it is much easier
# to just simulate each click.

pos = 50
hit_zero_counter = 0

lines = open("Day_01/Day1Input.txt").read().splitlines()

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    for _ in range(amount):
        if direction == "R":
            pos = (pos + 1) % 100
        else:
            pos = (pos - 1) % 100
        
        if pos == 0:
            hit_zero_counter += 1

print(hit_zero_counter)