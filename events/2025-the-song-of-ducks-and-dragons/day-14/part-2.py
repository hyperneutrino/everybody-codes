grid = [[char == "#" for char in line] for line in open(0).read().splitlines()]

def step_cell(grid, r, c):
    neighborhood = [
        grid[nr][nc]
        for nr, nc in [(r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1), (r, c)]
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr])
    ]
    
    return sum(neighborhood) % 2 == 0

def step(grid):
    return [
        [step_cell(grid, r, c) for c in range(len(grid[r]))]
        for r in range(len(grid))
    ]

def count(grid):
    return sum(map(sum, grid))

total = 0

for _ in range(2025):
    grid = step(grid)
    total += count(grid)

print(total)