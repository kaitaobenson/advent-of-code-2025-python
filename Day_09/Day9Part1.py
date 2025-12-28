# Given a list of 2d coordinates, find the 
# largest area that can be made by using two coordinates as 
# opposite corners in a rectangle.
# Puzzle answer: 4763040296

coords = []

input = open("Day_09/Day9Input.txt").read()

for line in input.splitlines():
    coords.append(
        tuple([int(s) for s in line.split(",")])
    )

def get_area(pos1, pos2) -> float:
    a = abs(pos2[0]-pos1[0]) + 1
    b = abs(pos2[1]-pos1[1]) + 1
    return (a*b)

# (area, (x, y), (x, y))
pairs = []

for i in range(0, len(coords) - 1):
    for j in range(i + 1, len(coords)):
        a, b = coords[i], coords[j]

        area = get_area(a, b)
        
        pairs.append((area, a, b))

pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

print(pairs[0])