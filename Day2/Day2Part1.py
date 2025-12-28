# Find the invalid IDs within the ranges provided in the input
# Invalid inputs are made of TWO repeating parts, ex: 504504
# Puzzle answer: 12599655151

input = open("Day2/Day2Input.txt").read()
sum = 0

def is_valid_id(id) -> bool:
	id_string = str(id)

	if len(id_string) % 2 == 1:
			return True

	halfway_index = len(id_string) // 2

	id_string_first_half = id_string[0 : halfway_index]
	id_string_second_half = id_string[halfway_index : ]
	
	if id_string_first_half == id_string_second_half:
		return False
	else:
		return True

for id_range in input.split(","):
	lower_bound = int(id_range.split("-")[0])
	upper_bound = int(id_range.split("-")[1])
	

	for id in range(lower_bound, upper_bound + 1):
		if not is_valid_id(id):
			sum += id

print(sum)