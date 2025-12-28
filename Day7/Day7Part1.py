# Find the number of times a beam going down from 'S'
# splits on '^' signs
# Puzzle answer: 1570

input = open("Day7/Day7Input.txt").read()
lines = input.splitlines()

beam_indices = set()
split_count = 0

beam_indices.add(lines[0].find("S"))

for i in range(1, len(lines)):

    line = lines[i]

    next_beam_indices = set()
    
    for index in beam_indices:
        if line[index] == "^":
            next_beam_indices.add(index + 1)
            next_beam_indices.add(index - 1)
            split_count += 1
        else:
            next_beam_indices.add(index)
    
    beam_indices = next_beam_indices
    
print(split_count)