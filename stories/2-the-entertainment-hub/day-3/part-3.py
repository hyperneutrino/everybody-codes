## NOTE: you probably want to pipe the STDERR into a file
## (I called it output.txt and it's in the .gitignore).

class Die:
    def __init__(self, id, faces, seed):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.roll_number = 1
        self.face = 0
    
    def roll(self):
        spin = self.roll_number * self.pulse
        self.face = (self.face + spin) % len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse = self.pulse + 1 + self.roll_number + self.seed
        self.roll_number += 1
        return self.faces[self.face]

raw = open(0).read()
lines, grid = raw.split("\n\n")

dice = []

for line in lines.split("\n"):
    parts = line.split()
    id = int(parts[0][:-1])
    faces = list(map(int, parts[1].split("=")[1][1:-1].split(",")))
    seed = int(parts[2].split("=")[1])
    dice.append(Die(id, faces, seed))

grid = [list(map(int, row)) for row in grid.split("\n")]

aggregate = set()

for die in dice:
    value = die.roll()
    possible = set((r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == value)
    aggregate |= possible
    while len(possible) > 0:
        value = die.roll()
        next_set = set()
        for r, c in possible:
            for nr, nc in [(r, c), (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[nr]): continue
                if grid[nr][nc] != value: continue
                next_set.add((nr, nc))
        possible = next_set
        aggregate |= possible
        
print(len(aggregate))

art = [[" "] * len(row) for row in grid]

for r, c in aggregate:
    art[r][c] = "#"

art = "\n".join("".join(row) for row in art)

import sys
print(art, file=sys.stderr)