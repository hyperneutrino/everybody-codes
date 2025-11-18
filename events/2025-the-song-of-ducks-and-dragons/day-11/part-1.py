cols = list(map(int, open(0)))

phase = 1
rounds = 10

while rounds > 0:
    moved = False
    for i in range(len(cols) - 1):
        if phase == 1:
            if cols[i] > cols[i + 1]:
                cols[i] -= 1
                cols[i + 1] += 1
                moved = True
        else:
            if cols[i] < cols[i + 1]:
                cols[i] += 1
                cols[i + 1] -= 1
                moved = True
    if moved:
        rounds -= 1
    else:
        if phase == 1:
            phase = 2
        else:
            break

print(sum(i * x for i, x in enumerate(cols, 1)))