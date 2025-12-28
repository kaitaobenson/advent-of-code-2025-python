# This is an input parsing puzzle.
# Numbers are arranged vertically, with an opterator * or + 
# At the bottom.  Multiply and add them up to get the answer.

# Puzzle answer: 6299564383938

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

input = open("Day6/Day6Input.txt").read()

numbers = []
operators = []

for line in input.splitlines():
    parts = line.split()
    if parts[0] == "+" or parts[0] == "*":
        operators = parts
    else:
        numbers.append(parts)

answer = 0

for i in range(len(operators)):
    column = [row[i] for row in numbers]

    if operators[i] == "+":
        answer += sum_list(column)
    elif operators[i] == "*":
        answer += mult_list(column)

print(answer)