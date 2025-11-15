import functools

grid = list(map(list, open(0).read().splitlines()))
ROWS = len(grid)
COLS = len(grid[0])

DRAGON = None
SHEEP = []

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "D":
            DRAGON = (r, c)
        elif val == "S":
            SHEEP.append((r, c))

SHEEP = tuple(SHEEP)

def dragon_can_move_to(dragon):
    spots = []
    for dr, dc in [(1, 2), (2, 1)]:
        for sr, sc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            r = dragon[0] + sr * dr
            c = dragon[1] + sc * dc
            if 0 <= r < ROWS and 0 <= c < COLS:
                spots.append((r, c))
    return spots

@functools.cache
def count(sheep, dragon, turn="sheep"):
    if turn == "sheep":
        if len(sheep) == 0: return 1
        total = 0
        moved = 0
        for i, (r, c) in enumerate(sheep):
            if r == ROWS - 1:
                moved += 1
            elif grid[r + 1][c] == "#" or dragon != (r + 1, c):
                moved += 1
                total += count((*sheep[:i], (r + 1, c), *sheep[i + 1:]), dragon, turn="dragon")
        if moved == 0: return count(sheep, dragon, turn="dragon")
        return total
    if turn == "dragon":
        total = 0
        for r, c in dragon_can_move_to(dragon):
            total += count(tuple((sr, sc) for sr, sc in sheep if grid[sr][sc] == "#" or (sr, sc) != (r, c)), (r, c), turn="sheep")
        return total

print(count(SHEEP, DRAGON))