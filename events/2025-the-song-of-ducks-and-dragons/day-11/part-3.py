cols = list(map(int, open(0)))

assert all(x < y for x, y in zip(cols, cols[1:]))

average = sum(cols) // len(cols)

print(sum(average - num for num in cols if num < average))