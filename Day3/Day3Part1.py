# Find the largest two digit number that can be made 
# from a row of numbers.  First number picked from the line
# is tens place, second number picked is ones place.
# ex: 818181911112111 largest number is 92
# Puzzle answer: 16927

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

answer = 0

input = open("Day3/Day3Input.txt").read()

for line in input.splitlines():
    line = line.strip()
    first_digit_index = get_largest_digit_idx(line, 0, len(line) - 2)
    first_digit = line[first_digit_index]

    second_digit_index = get_largest_digit_idx(line, first_digit_index + 1, len(line) - 1)
    second_digit = line[second_digit_index]
    
    answer += int(first_digit + second_digit)

print(answer)