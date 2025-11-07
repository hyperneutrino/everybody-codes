ratios = [ratio.splitlines() for ratio in open(0).read().split("|")]
total = 1

for x, y in ratios:
    total *= int(x) / int(y)

print(int(total * 100))