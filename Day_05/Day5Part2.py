# Given a set of ranges (the values can now be ignored)
# Find how many values fit within the ranges.
# Puzzle answer: 345821388687084

# Note: Since I already joined the overlapping ranges in the previous 
# part, this part is easy and I can just subtract.

ranges = []
values = []

input = open("Day_05/Day5Input.txt").read()

parts = input.split("\n\n")

for line in parts[0].split("\n"):
    nums = line.split("-")
    range = (int(nums[0]), int(nums[1]))
    ranges.append(range)

for line in parts[1].split("\n"):
    values.append(int(line))

ranges = sorted(ranges, key=lambda x: x[0])

# Join overlapping ranges
idx = 0
while True:
    current = ranges[idx]
    next = ranges[idx + 1]

    if current[1] >= next[0]:
        # Need to combine
        new_max =  max(current[1], next[1])
        ranges[idx] = (current[0], new_max)
        ranges.remove(next)
    else:
        idx += 1
    
    if idx >= len(ranges) - 1:
        break

sum = 0

for range in ranges:
    sum += range[1] - range[0] + 1

print(sum)