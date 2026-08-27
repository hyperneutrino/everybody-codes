get = lambda: tuple(map(int, input().split("=")[1][1:-1].split(",")))

start = get()
beacons = { "A": get(), "B": get(), "C": get() }
moves = input().split("=")[1]

beetles = { start }
position = start

for move in moves:
    px, py = position
    bx, by = beacons[move]
    position = (int((px + bx) / 2), int((py + by) / 2))
    beetles.add(position)

print(len(beetles))