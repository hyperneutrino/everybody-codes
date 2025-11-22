grid = tuple((False,) * 34 for _ in range(34))
pattern = [[char == "#" for char in line] for line in open(0).read().splitlines()]

def step_cell(grid, r, c):
    neighborhood = [
        grid[nr][nc]
        for nr, nc in [(r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1), (r, c)]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr])
    ]
    
    return sum(neighborhood) % 2 == 0

def step(grid):
    return tuple(
        tuple(step_cell(grid, r, c) for c in range(len(grid[r])))
        for r in range(len(grid))
    )

def count(grid):
    return sum(map(sum, grid))

def matches(grid):
    row_offset = (len(grid) - len(pattern)) // 2
    col_offset = (len(grid[0]) - len(pattern[0])) // 2
    return all(
        grid[r + row_offset][c + col_offset] == pattern[r][c]
        for r in range(len(pattern))
        for c in range(len(pattern[0]))
    )

seen = set()
seq = []

while True:
    grid = step(grid)
    if grid in seen:
        break
    seen.add(grid)
    seq.append(grid)

T = 1_000_000_000

total = 0

for grid in seq:
    if matches(grid):
        total += count(grid)

total *= T // len(seq)

for grid in seq[:T % len(seq)]:
    if matches(grid):
        total += count(grid)

print(total)