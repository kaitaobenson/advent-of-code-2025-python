# Find the invalid IDs within the ranges provided in the input
# Invalid inputs are made of ANY AMOUNT of repeating parts, ex: 32323232
# Puzzle answer: 20942028255

input = open("Day_02/Day2Input.txt").read()

sum = 0

def is_valid_id(id) -> bool:
	id_string = str(id)

	for i in range(1, len(id_string)):
		if is_repeating(id_string, i):
			return False
	
	return True

def is_repeating(string, repeat_size) -> bool:
	if repeat_size > len(string) / 2:
		return False
	
	if len(string) % repeat_size != 0:
		return False

	repeating_string = string[0 : repeat_size]

	for i in range(len(string)):
		if string[i] != repeating_string[i % repeat_size]:
			return False
	
	return True

for id_range in input.split(","):
	lower_bound = int(id_range.split("-")[0])
	upper_bound = int(id_range.split("-")[1])
	

	for id in range(lower_bound, upper_bound + 1):
		if not is_valid_id(id):
			sum += id

print(sum)