from collections import deque

get = lambda: tuple(map(int, input().split("=")[1][1:-1].split(",")))

start = get()
beacons = [get() for _ in range(3)]

beetles = { start }
queue = deque([start])

while len(queue) > 0:
    px, py = queue.popleft()
    for bx, by in beacons:
        n = (int((px + bx) / 2), int((py + by) / 2))
        if n in beetles: continue
        beetles.add(n)
        queue.append(n)

def neighbors(px, py):
    return { (px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1) }

fireflies = set()

for px, py in beetles:
    fireflies |= neighbors(px, py)

print(len(fireflies - beetles))