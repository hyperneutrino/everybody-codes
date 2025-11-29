grid = [line.strip().strip(".") for line in open(0)]

pairs = 0

for row in grid:
    for x, y in zip(row, row[1:]):
        if x == y == "T":
            pairs += 1

for r, s in zip(grid, grid[1:]):
    for x, y in zip(r[1::2], s[0::2]):
            if x == y == "T":
                pairs += 1

print(pairs)