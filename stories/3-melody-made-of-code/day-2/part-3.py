from collections import deque

grid = [line.strip() for line in open(0)]
all_coords = {r * 1j + c for r in range(len(grid)) for c in range(len(grid[r]))}
bones = set()

min_r = -1
max_r = len(grid)
min_c = -1
max_c = len(grid[0])

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "@":
            at = r * 1j + c
        elif grid[r][c] == "#":
            bones.add(r * 1j + c)

offsets = [-1j, 1, 1j, -1]
boundary = {bone + offset for bone in bones for offset in offsets} - bones

seen = {at}
moves = [-1j, -1j, -1j, 1, 1, 1, 1j, 1j, 1j, -1, -1, -1]
move_count = 0

def floodfill(start, shortcut_outside):
    queue = deque([start])
    fill = {start}
    while len(queue) > 0:
        curr = queue.popleft()
        for offset in moves:
            nx = curr + offset
            if nx.imag < min_r or nx.imag > max_r or nx.real < min_c or nx.real > max_c:
                if shortcut_outside: return (True, set())
                else: continue
            if nx in bones or nx in seen or nx in fill: continue
            queue.append(nx)
            fill.add(nx)
    return (False, fill)

_, reachable = floodfill(min_r * 1j + min_c, False)
seen |= all_coords - reachable

while True:
    if boundary <= seen: break
    
    while at + moves[0] in seen or at + moves[0] in bones:
        moves.append(moves.pop(0))
    
    at += moves[0]
    seen.add(at)
    move_count += 1
    moves.append(moves.pop(0))

    min_r = min(min_r, at.imag - 1)
    max_r = max(max_r, at.imag + 1)
    min_c = min(min_c, at.real - 1)
    max_c = max(max_c, at.real + 1)
    
    adj_empty = {at + offset for offset in moves} - seen - bones
    
    for start in adj_empty:
        outside, fill = floodfill(start, True)
        if not outside:
            seen |= fill

print(move_count)