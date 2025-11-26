grid = [[0 if char == "@" else int(char) for char in line] for line in open(0).read().splitlines()]

for r, row in enumerate(grid):
    for c, num in enumerate(row):
        if num == 0:
            zr, zc = r, c

radius = 10
total = 0

for r, row in enumerate(grid):
    for c, num in enumerate(row):
        if (r - zr) ** 2 + (c - zc) ** 2 <= radius ** 2:
            total += num

print(total)
