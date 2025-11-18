cols = list(map(int, open(0)))

phase = 1
rounds = 0

while True:
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
        rounds += 1
    else:
        if phase == 1:
            phase = 2
        else:
            break

print(rounds)