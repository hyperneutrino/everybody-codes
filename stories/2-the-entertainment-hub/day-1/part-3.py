raw = open(0).read()

grid, lines = raw.split("\n\n")

grid = grid.split("\n")
lines = lines.split("\n")

score = 0

tokens = []

for line in lines:
    tokens.append([])
    
    for slot in range(1, len(grid[0]) // 2 + 2):
        col = (slot * 2) - 2
        dirs = list(line)

        for row in grid:
            if row[col] == ".": continue
            
            side = dirs.pop(0)
            
            if col == 0: col += 1
            elif col == len(row) - 1: col -= 1
            else: col += -1 if side == "L" else 1
            
        fslot = (col + 2) // 2
        tokens[-1].append(max(0, (fslot * 2) - slot))

import itertools

gmin = float("inf")
gmax = 0

for k in itertools.permutations(list(range(len(tokens[0]))), 6):
    total = sum(row[x] for row, x in zip(tokens, k))
    gmin = min(gmin, total)
    gmax = max(gmax, total)

print(gmin, gmax)