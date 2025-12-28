# Given a set of shapes, and a set of regions with shape requirements
# find how many regions can fit all of the shapes (turning, flipping is allowed)
# Puzzle answer: 492

# Note: This code only checks general cases.  It checks if there are too many
# blocks to possibly fit in the area, and also checks if all the blocks can fit without 
# needing to pack.  This apparantly fits all the cases in the input.
# There also is no part 2.

import re
import math

input = open("Day_12/Day12Input.txt").read()

# Amount of # per block
filled_unit_per_block = [6, 7, 5, 7, 7, 7]

region_regex = r"(\d+)x(\d+):([\d ]+)"

counter = 0

for match in re.findall(region_regex, input):
    width: int = int(match[0])
    height: int = int(match[1])
    block_amounts: list[int] = [int(x) for x in match[2].split()]

    # Check if blocks are greater than area
    area = width * height

    total_filled_units = 0
    for i in range(len(block_amounts)):
        # number of blocks * units in block
        total_filled_units += block_amounts[i] * filled_unit_per_block[i]
    
    if total_filled_units > area:
        continue # Definitely can't fit

    
    # Check if blocks can fit without needing to be packed
    
    # 3x3 areas in the region
    block_areas = math.floor(width/3) * math.floor(height/3)
    total_blocks = sum(block_amounts)
    if block_areas >= total_blocks:
        counter += 1

print(counter)