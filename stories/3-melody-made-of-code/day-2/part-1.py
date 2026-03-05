grid = [line.strip() for line in open(0)]

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
    if at == bone:
        break

    while at + moves[0] in seen:
        moves.append(moves.pop(0))

    at += moves[0]
    seen.add(at)
    move_count += 1
    moves.append(moves.pop(0))

print(move_count)