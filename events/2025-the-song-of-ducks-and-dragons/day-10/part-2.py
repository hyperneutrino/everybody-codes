grid = list(map(list, open(0).read().splitlines()))
ROWS = len(grid)
COLS = len(grid[0])

DRAGON = None

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "D":
            DRAGON = (r, c)

def dragon_can_move_to(dragon):
    spots = []
    for dr, dc in [(1, 2), (2, 1)]:
        for sr, sc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r = dragon[0] + sr * dr
            c = dragon[1] + sc * dc
            if 0 <= r < ROWS and 0 <= c < COLS:
                spots.append((r, c))
    return spots

s = {DRAGON}
e = set()

for turn in range(20):
    s = {spot for dragon in s for spot in dragon_can_move_to(dragon)}
    e |= {(sr, c) for r, c in s for sr in (r - turn, r - turn - 1) if grid[r][c] != "#" and sr >= 0 and grid[sr][c] == "S"}

print(len(e))