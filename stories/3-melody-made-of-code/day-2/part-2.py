from collections import deque

grid = [line.strip() for line in open(0)]

min_r = -1
max_r = len(grid)
min_c = -1
max_c = len(grid[0])

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "@":
            at = r * 1j + c
        elif grid[r][c] == "#":
            bone = r * 1j + c

seen = {at}
moves = [-1j, 1, 1j, -1]
move_count = 0

while True:
    if all(bone + offset in seen for offset in moves):
        break
    
    while at + moves[0] in seen or at + moves[0] == bone:
        moves.append(moves.pop(0))
    
    at += moves[0]
    seen.add(at)
    move_count += 1
    moves.append(moves.pop(0))

    min_r = min(min_r, at.imag - 1)
    max_r = max(max_r, at.imag + 1)
    min_c = min(min_c, at.real - 1)
    max_c = max(max_c, at.real + 1)
    
    adj_empty = {at + offset for offset in moves} - seen - {bone}
    
    for start in adj_empty:
        queue = deque([start])
        fill = {start}
        outside = False
        while len(queue) > 0:
            curr = queue.popleft()
            for offset in moves:
                nx = curr + offset
                if nx.imag <= min_r or nx.imag >= max_r or nx.real <= min_c or nx.real >= max_c:
                    outside = True
                    break
                if nx == bone or nx in seen or nx in fill: continue
                queue.append(nx)
                fill.add(nx)
            if outside: break
        if not outside:
            seen |= fill

print(move_count)