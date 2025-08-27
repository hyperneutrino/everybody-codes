raw = open(0).read()

grid, lines = raw.split("\n\n")

grid = grid.split("\n")
lines = lines.split("\n")

score = 0

for line in lines:
    opt = 0
    
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
        opt = max(opt, (fslot * 2) - slot)
    
    score += opt

print(score)