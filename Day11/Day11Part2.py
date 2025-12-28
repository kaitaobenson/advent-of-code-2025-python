# The input contains a graph with each line as a node
# input : output, output, output ...
# Find the amount of paths that lead from node "svr" to node "out"
# and also must include nodes "dac" and "fft" along the path.
# Puzzle answer: 499645520864100

from collections import deque

input = open("Day11/Day11Input.txt").read()

connections = {}

for line in input.splitlines():
    parts = line.split(":")

    input = parts[0]
    outputs = parts[1].split()

    connections[input] = outputs

memo = {}

def dfs(node: str, visited_dac: bool, visited_fft: bool) -> int:
    # Check if memoized
    key = (node, visited_dac, visited_fft)
    if key in memo:
        return memo[key]

    count = 0

    for output in connections[node]:

        now_visited_dac = visited_dac or (output == "dac")
        now_visited_fft = visited_fft or (output == "fft")

        if output == "out":
            if now_visited_dac and now_visited_fft:
                count += 1
        else:
            count += dfs(output, now_visited_dac, now_visited_fft)
    
    # Add to memo
    memo[key] = count

    return count

paths: int = dfs("svr", False, False)
print(paths)