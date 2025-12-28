# Given a list of 3d coordinates, connect points into circuits.
# Make 1000 connections, connecting the closest points first.
# Answer is the sizes of the top 3 largest circuits multiplied together.
# Puzzle answer: 46398

coords = []

input = open("Day_08/Day8Input.txt").read()

for line in input.splitlines():
    coords.append(
        tuple([int(s) for s in line.split(",")])
    )

def get_dist_squared(pos1: list[3], pos2: list[3]) -> float:
    return (
        (pos2[0]-pos1[0]) ** 2 + 
        (pos2[1]-pos1[1]) ** 2 + 
        (pos2[2]-pos1[2]) ** 2
    )

# (dist, (x, y, z), (x, y, z))
closest_pairs = []

for i in range(0, len(coords) - 1):
    for j in range(i + 1, len(coords)):
        a = coords[i]
        b = coords[j]

        dist = get_dist_squared(a, b)
        
        closest_pairs.append((dist, a, b))

closest_pairs = sorted(closest_pairs, key=lambda x: x[0])

print("1")

circuits = []

for i in range(1000):

    dist, a, b = closest_pairs[i]

    set_a = None
    set_b = None

    for circuit in circuits:
        if a in circuit:
            set_a = circuit
        if b in circuit:
            set_b = circuit
    
    # Neither are in a circuit - add new
    if not set_a and not set_b:
        circuits.append({a, b})
    
    # One is in a circuit - add other
    elif set_a and not set_b:
        set_a.add(b)
    elif not set_a and set_b:
        set_b.add(a)
    
    # both exist but separate - join
    elif set_a is not set_b:
        set_a |= set_b
        circuits.remove(set_b)
    
    # both exist and are the same - nothing
    else:
        pass

print("2")


sizes = []
for c in circuits:
    sizes.append(len(c))

sizes.sort(reverse=True)

print("3")

print(sizes[0] * sizes[1] * sizes[2])