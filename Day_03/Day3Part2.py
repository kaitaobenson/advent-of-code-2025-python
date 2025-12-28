# Find the largest TWELVE digit number that can be made 
# from a row of numbers.
# ex: 811111111111119 largest number is 811111111119
# Puzzle answer: 167384358365132

# Returns index of largest digit in string within range [min, max]
def get_largest_digit_idx(string = "", min = 0, max = 0) -> int:
    largest_num = -1
    largest_num_idx = -1

    for i in range(min, max + 1):
        num = int(string[i])

        if num > largest_num:
            largest_num = num
            largest_num_idx = i

    return largest_num_idx

max_digits = 12
answer = 0

input = open("Day_03/Day3Input.txt").read()

for line in input.splitlines():
    line = line.strip()

    min = 0
    max = len(line) - max_digits

    digits = ""

    for _ in range(max_digits):
        digit_index = get_largest_digit_idx(line, min, max)
        digits += line[digit_index]

        min = digit_index + 1
        max += 1
    
    answer += int(digits)

print(answer)