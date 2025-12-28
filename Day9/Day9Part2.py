# Given a list of 2d coordinates, find the 
# largest area that can be made by using two coordinates as 
# opposite corners in a rectangle.
# This time, all points in the rectangle must be inside the shape made 
# by connecting coordinates in the list to the following coordinate
# Puzzle answer: 4763040296


from collections import deque

lines = open("Day9/Day9Input.txt").read().splitlines()

raw_pos_list = []

x_conversion = {}
y_conversion = {}

# Load data
for line in lines:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])

    raw_pos_list.append((x,y))

    x_conversion[x] = -1
    y_conversion[y] = -1


# Sort and number conversions
counter = 1 # Start at 1 to give space to floodfill
for i in sorted(x_conversion.keys()):
    x_conversion[i] = counter
    counter += 1

counter = 1
for i in sorted(y_conversion.keys()):
    y_conversion[i] = counter
    counter += 1

def from_real_to_grid(pos: tuple[int, int]) -> tuple[int, int]:
    x, y = pos
    return (x_conversion[x], y_conversion[y])


# Make the compacted grid now
grid = []
grid_size = len(x_conversion) + 2 # Space to floodfill

for i in range(grid_size):
    grid.append([])
    for j in range(grid_size):
        grid[i].append(".")

# Draw lines
raw_pos_amount = len(raw_pos_list)

for i in range(raw_pos_amount):
    p1 = raw_pos_list[i]
    p2 = raw_pos_list[(i + 1) % raw_pos_amount]

    g1x, g1y = from_real_to_grid(p1)
    g2x, g2y = from_real_to_grid(p2)
    
    # Vertical line
    if g1x == g2x:
        x_value = g1x
        for y_value in range(min(g1y, g2y), max(g1y, g2y) + 1):
            grid[y_value][x_value] = "X"
    
    # Horizontal line
    if g1y == g2y:
        y_value = g1y
        for x_value in range(min(g1x, g2x), max(g1x, g2x) + 1):
            grid[y_value][x_value] = "X"

# Floodfill
def is_pos_within_bounds(pos: tuple[int, int]) -> bool:
    x, y = pos
    if x < 0 or x >= grid_size:
        return False
    if y < 0 or y >= grid_size:
        return False

    return True

def get_adjacent_positions(pos: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pos
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

positions_to_fill = deque()
positions_to_fill.append((0, 0))

while len(positions_to_fill) > 0:

    pos = positions_to_fill.pop()
    x, y = pos
    
    if grid[y][x] == "X" or grid[y][x] == "O":
        continue
    
    grid[y][x] = "O"

    for adj_pos in get_adjacent_positions(pos):
        if is_pos_within_bounds(adj_pos):
            positions_to_fill.append(adj_pos)


# Loop through all rectangles

def is_valid_rect(pos1, pos2) -> bool:
    # First test other two corners (speed things up)
    c1x, c1y = pos1[0], pos2[1]
    c2x, c2y = pos2[0], pos1[1]

    if grid[c1y][c1x] == "O":
        return False
    if grid[c2y][c2x] == "O":
        return False

    # Then loop through all of them
    x_min, x_max = min(pos1[0], pos2[0]), max(pos1[0], pos2[0])
    y_min, y_max = min(pos1[1], pos2[1]), max(pos1[1], pos2[1])

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if grid[y][x] == "O":
                return False

    return True

def get_area(pos1, pos2) -> float:
    a = abs(pos2[0]-pos1[0]) + 1
    b = abs(pos2[1]-pos1[1]) + 1
    return (a*b)

largest_area = 0

for i in range(0, raw_pos_amount - 1):
    for j in range(i + 1, raw_pos_amount):
        p1 = raw_pos_list[i]
        p2 = raw_pos_list[j]

        g1 = from_real_to_grid(p1)
        g2 = from_real_to_grid(p2)

        if not is_valid_rect(g1, g2):
            continue

        area = get_area(p1, p2)
        
        if area > largest_area:
            largest_area = area


print(largest_area)