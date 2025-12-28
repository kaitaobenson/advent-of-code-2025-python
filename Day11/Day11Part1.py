# The input contains a graph with each line as a node
# input : output, output, output ...
# Find the amount of paths that lead from node "you" to node "out".
# Puzzle answer: 534

from collections import deque

input = open("Day11/Day11Input.txt").read()

connections = {}

for line in input.splitlines():
    parts = line.split(":")

    input = parts[0]
    outputs = parts[1].split()

    connections[input] = outputs

paths_counter = 0

queue = deque()
queue.append("you")

while queue:
    outputs: list = connections[queue.pop()]

    for output in outputs:
        if output == "out":
            paths_counter += 1
        else:
            queue.append(output)

print(paths_counter)