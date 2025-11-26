import heapq
import functools

grid = [[-1 if char == "@" else 0 if char == "S" else int(char) for char in line] for line in open(0).read().splitlines()]

for r, row in enumerate(grid):
    for c, num in enumerate(row):
        if num == 0:
            sr, sc = r, c
        if num == -1:
            zr, zc = r, c

for radius in range(2 * len(grid)):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r - zr) ** 2 + (c - zc) ** 2 <= radius ** 2:
                grid[r][c] = -1

    seen = {}
    pq = [(0, sr, sc, None)]

    while len(pq) > 0:
        time, cr, cc, last = heapq.heappop(pq)
        if (cr, cc) in seen: continue
        seen[(cr, cc)] = (time, last)
        for nr, nc in [(cr, cc - 1), (cr, cc + 1), (cr - 1, cc), (cr + 1, cc)]:
            if (nr, nc) in seen: continue
            if nr < 0 or nr >= len(grid): continue
            if nc < 0 or nc >= len(grid[nr]): continue
            if grid[nr][nc] == -1: continue
            if time + grid[nr][nc] >= (radius + 1) * 30: continue
            heapq.heappush(pq, (time + grid[nr][nc], nr, nc, (cr, cc)))

    @functools.cache
    def is_left(key):
        if key not in seen: return None
        r, c = key
        if r == zr:
            return c < zc
        _, last = seen[key]
        return is_left(last)

    best = float("inf")

    for lr, lc in seen:
        if not is_left((lr, lc)): continue
        for rr, rc in [(lr, lc - 1), (lr, lc + 1), (lr - 1, lc), (lr + 1, lc)]:
            if is_left((rr, rc)) != False: continue
            best = min(best, seen[(lr, lc)][0] + seen[(rr, rc)][0])

    if best < (radius + 1) * 30:
        print(best * radius)
        break
