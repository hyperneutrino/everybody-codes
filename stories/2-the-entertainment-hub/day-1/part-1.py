raw = open(0).read()

grid, lines = raw.split("\n\n")

grid = grid.split("\n")
lines = lines.split("\n")

score = 0

slot = 1

for line in lines:
    col = (slot * 2) - 2
    dirs = list(line)

    for row in grid:
        if row[col] == ".": continue
        
        side = dirs.pop(0)
        
        if col == 0: col += 1
        elif col == len(row) - 1: col -= 1
        else: col += -1 if side == "L" else 1
        
    fslot = (col + 2) // 2
    score += max(0, (fslot * 2) - slot)
    slot += 1

print(score)