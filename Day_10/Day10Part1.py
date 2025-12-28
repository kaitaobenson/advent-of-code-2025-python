# Each line has a set of buttons and a set of lights.  
# Pressing a button will toggle certain lights.
# Find the fewest number of button presses to change the lights to the arrangement shown.
# Puzzle answer: 527

from collections import deque

input = open("Day_10/Day10Input.txt").read()

# Returns min amount of button presses needed
def solve_line(line: str) -> int:
    lights = [] # [true, false ...]
    buttons = [] # [(3,), (2, 3) ...]

    parse_line(line, lights, buttons)
    buttons_amount = len(buttons)

    seen_combos = set()
    combos_queue = deque()

    # Add starting combos of length 1
    for i in range(buttons_amount):
        combo = ButtonCombo([i])
        combos_queue.append(combo)

    # Bfs
    while combos_queue:
        combo: ButtonCombo = combos_queue.popleft()

        if combo in seen_combos:
            continue
        
        # Check if combo works
        if combo.works(buttons, lights):
            return len(combo.button_indices)

        # Add to seen combos
        seen_combos.add(combo)

        # Add new combos to queue
        last = combo.button_indices[-1]

        for i in range(last + 1, buttons_amount):
            new_combo = ButtonCombo(list(combo) + [i])
            combos_queue.append(new_combo)
    
    return -1



class ButtonCombo:
    button_indices: tuple
     
    def __init__(self, button_indices: list[int]):
        self.button_indices = tuple(sorted(button_indices))
    
    # For list()
    def __iter__(self):
        return iter(self.button_indices)
    
    # Methods for hashing, to use in set()
    def __eq__(self, other):
        if not isinstance(other, ButtonCombo):
            return False
        return self.button_indices == other.button_indices

    def __hash__(self):
        return hash(self.button_indices)


    def works(self, buttons: list[tuple], target_light_values: list[bool]) -> bool:
        # test_lights start false
        test_lights = [False for _ in range(len(target_light_values))]

        for index in self.button_indices:
            press_button(buttons[index], test_lights)
        
        return test_lights == target_light_values
     

def parse_line(line: str, lights_output: list, buttons_output: list):
    for item in line.split(" "):
        
        bracket = item[0]
        item = item[1 : len(item) - 1] # Remove brackets

        if bracket == "[": # Lights schematic
            for i in range(len(item)):
                if item[i] == "#":
                    lights_output.append(True)
                elif item[i] == ".":
                    lights_output.append(False)
        
        if bracket == "(": # Button schematic
            indices = []

            for i in item.split(","):
                indices.append(int(i))
            
            # (Tuples with one value still work, they just look funky)
            buttons_output.append(tuple(indices))


def press_button(button: tuple, lights: list) -> None:
        for i in button:
            lights[i] = not lights[i]


sum = 0
for line in input.splitlines():
    sum += solve_line(line)

print(sum)