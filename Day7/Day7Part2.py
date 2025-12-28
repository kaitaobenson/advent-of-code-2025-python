# Find the number of timelines a beam going down from 'S'
# can take, if each time it splits it can go left or right
# Puzzle answer: 15118009521693

# Note: this is similar to pascal's triangle

lines = open("Day7/Day7Input.txt").read().splitlines()

width = len(lines[0])
height = len(lines)

beam_indices = set()
# Current pascal triangle row
row_timelines = [0 for _ in range(width)]

# Add starting point
starting_index = lines[0].find("S")

beam_indices.add(starting_index)
row_timelines[starting_index] = 1

# Iterate through lines
for i in range(1, height):
    line = lines[i]

    next_beam_indices = set()
    next_row_timelines = [0 for _ in range(width)]
    
    for index in beam_indices:

        if line[index] == "^":
            next_beam_indices.add(index + 1)
            next_beam_indices.add(index - 1)
            
            next_row_timelines[index - 1] += row_timelines[index]
            next_row_timelines[index + 1] += row_timelines[index]

        else:
            next_beam_indices.add(index)

            next_row_timelines[index] += row_timelines[index]
    
    row_timelines = next_row_timelines
    beam_indices = next_beam_indices

print(sum(row_timelines))