from collections import deque

instructions = [(section[0], int(section[1:])) for section in input().split(",")]

grid = { 0: "S" }

d = 1j
p = 0

for turn, size in instructions:
    if turn == "R":
        d *= -1j
    else:
        d *= 1j
    
    for _ in range(size):
        p += d
        grid[p] = "#"

grid[p] = "E"

T = max(x.imag for x in grid) + 1
B = min(x.imag for x in grid) - 1
L = min(x.real for x in grid) - 1
R = max(x.real for x in grid) + 1

seen = {0}
queue = deque([(0, 0)])

while len(queue) > 0:
    dist, curr = queue.popleft()
    for n in [curr - 1, curr + 1, curr - 1j, curr + 1j]:
        if B <= n.imag <= T and L <= n.real <= R and n not in seen and grid.get(n) != "#":
            if grid.get(n) == "E":
                print(dist + 1)
                exit(0)
            seen.add(n)
            queue.append((dist + 1, n))