from collections import deque

grid = [line.strip().strip(".") for line in open(0)]

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "S": S = (r, c)
        if char == "E": E = (r, c)

def neighbors(r, c):
    if c > 0:
        yield (r, c - 1)
    if c < len(grid[r]) - 1:
        yield (r, c + 1)
    if c % 2 == 0:
        if r > 0:
            yield (r - 1, c + 1)
    else:
        yield (r + 1, c - 1)

seen = {S}
queue = deque([(0, S)])

while len(queue) > 0:
    dist, (cr, cc) = queue.popleft()
    for nr, nc in neighbors(cr, cc):
        if (nr, nc) == E:
            print(dist + 1)
            exit(0)
        if (nr, nc) in seen: continue
        if grid[nr][nc] == "#": continue
        seen.add((nr, nc))
        queue.append((dist + 1, (nr, nc)))