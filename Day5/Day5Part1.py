# Given a set of ranges and a set of values (the input)
# Find how many of the values fit within any of the ranges.
# Puzzle answer: 733

# Note: I tried a more optimized approach where the ranges were 
# preprocessed first (overlapping ranges were joined)
# then used a binary search to determine if the values were inside

ranges = []
values = []

input = open("Day5/Day5Input.txt").read()

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


def is_num_within_ranges(num: int, ranges: tuple[int, int]) -> bool:
    # Binary search
    low = 0
    high = len(ranges) - 1

    while low <= high:
        mid = low + (high - low) // 2

        range_at_mid = ranges[mid]

        if num >= range_at_mid[0] and num <= range_at_mid[1]:
            return True

        # Ignore left half
        elif num > range_at_mid[0]:
            low = mid + 1

        # Ignore right half
        else:
            high = mid - 1
    
    return False

counter = 0

for x in values:
    if is_num_within_ranges(x, ranges):
        counter += 1

print(counter)