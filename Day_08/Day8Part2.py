# Given a list of 3d coordinates, connect points into circuits.
# Continue making connections, connecting the closest points first.
# The answer is the product of the x coordinates of the last points you connect
# to create one large circuit.
# Puzzle answer: 8141888143

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

print("Done finding pairs")


circuits = []

def progress_update():
    lengths = []
    for c in circuits:
        lengths.append(len(c))
    print("Lengths of circuits: " + str(lengths))

    print("Coordinates left: " + str(len(coords)))


counter = 0
for pair in closest_pairs:

    counter += 1
    if counter > 100:
        counter = 0
        progress_update()

    a, b = pair[1], pair[2]

    if a in coords:
        coords.remove(a)
    if b in coords:
        coords.remove(b)

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

    # All connected in one circuit
    if len(coords) == 0 and len(circuits) == 1:
        print(a)
        print(b)
        print(a[0] * b[0])
        break