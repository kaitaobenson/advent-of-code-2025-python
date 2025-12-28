# This is an input parsing puzzle.
# Now, instead of 
# 123
#  45
#   6
# being 123 + 45 + 6, it is in vertical columns (alignment matters.)
# 1 + 24 + 356

# Puzzle answer: 11950004808442

def sum_list(list: list) -> int:
    sum = 0
    for x in list:
        sum += int(x)
    return sum

def mult_list(list: list) -> int:
    mult = 1
    for x in list:
        mult *= int(x)
    return mult

def get_column(str: str, col: int, row_width: int) -> str:
    column = ""
    idx = col
    while idx < len(str):
        column += str[idx]
        idx += (row_width + 1)
    return column


math_problems = []
operators = []

input = open("Day_06/Day6Input.txt").read()

row_width = len(input.split("\n")[0])

current_problem = -1
for i in range(row_width):
    column = get_column(input, i, row_width)

    if column.strip() == "":
        continue
    
    if column[-1] == "*" or column[-1] == "+":
        operators.append(column[-1])
        column = column[0:len(column) - 1]
        current_problem += 1
    
    if len(math_problems) <= current_problem:
        math_problems.append([])
    
    math_problems[current_problem].append(int(column))

answer = 0

for i in range(len(math_problems)):
    if operators[i] == "*":
        answer += mult_list(math_problems[i])
    if operators[i] == "+":
        answer += sum_list(math_problems[i])

print(answer)