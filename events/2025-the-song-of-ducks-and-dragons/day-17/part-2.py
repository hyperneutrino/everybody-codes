grid = [[0 if char == "@" else int(char) for char in line] for line in open(0).read().splitlines()]

for r, row in enumerate(grid):
    for c, num in enumerate(row):
        if num == 0:
            zr, zc = r, c

most = (0, 0)

for radius in range(1, len(grid) * 2):
    total = 0
    for r, row in enumerate(grid):
        for c, num in enumerate(row):
            if (radius - 1) ** 2 < (r - zr) ** 2 + (c - zc) ** 2 <= radius ** 2:
                total += num
    most = max(most, (total, radius))

print(most[0] * most[1])
