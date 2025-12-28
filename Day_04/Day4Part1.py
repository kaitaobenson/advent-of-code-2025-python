# Count the number of paper rolls on the grid that can be removed
# (have less than 4 paper rolls in adjacent positions)
# Puzzle answer: 1537

accessable_rolls = 0
paper_roll_positions = set()

def get_adjacent_positions(pos: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pos
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),

        (x - 1, y),
        (x + 1, y),

        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1)
    ]

input = open("Day_04/Day4Input.txt").read()
lines = input.splitlines()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "@":
            paper_roll_positions.add((i, j))

for pos in paper_roll_positions:
    adjacent_counter = 0

    for adj_pos in get_adjacent_positions(pos):
        if adj_pos in paper_roll_positions:
            adjacent_counter += 1
        
        if adjacent_counter >= 4:
            break
    
    if adjacent_counter < 4:
        accessable_rolls += 1

print(accessable_rolls)