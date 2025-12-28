# Each line has a set of buttons and a set of counters.  
# Pressing a button will increase certain counters by 1.
# Find the fewest number of button presses to change counters to the arrangement shown.
# Puzzle answer: 19810

import pulp

input = open("Day10/Day10Input.txt").read()

# Returns min amount of button presses needed
def solve_line(line: str) -> int:
    buttons = [] # [(3,), (2, 3) ...]
    joltages = [] # [5, 9 ...]

    buttons, joltages = parse_line(line)

    # Turn button index array into a matrix
    # 1, 3 -> 0,1,0,1
    coefficient_matrix = []

    for button in buttons:
        coefficient_row = []
        for i in range(len(joltages)):
            if i in button:
                coefficient_row.append(1)
            else:
                coefficient_row.append(0)
        
        coefficient_matrix.append(coefficient_row)
    
    prob = pulp.LpProblem("min_sum", pulp.LpMinimize)

    A = coefficient_matrix
    b = joltages

    x = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer")
        for i in range(len(buttons))
    ]

    prob += pulp.lpSum(x)

    for j in range(len(b)):
        prob += pulp.lpSum(A[i][j] * x[i] for i in range(len(buttons))) == b[j]

    
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    solution = [int(v.value()) for v in x]

    return sum(solution)

def parse_line(line: str):
    buttons = []
    joltages = []

    for item in line.split(" "):
        
        bracket = item[0]
        item = item[1 : len(item) - 1] # Remove brackets
        
        if bracket == "(": # Button schematics (many)
            indices = [int(x) for x in item.split(",")]
            buttons.append(tuple(indices))
        
        if bracket == "{": # Joltage schematic (one)
            joltages = [int(x) for x in item.split(",")]
    
    return buttons, joltages

total = 0
for line in input.splitlines():
    ans = solve_line(line)
    total += ans

print(total)