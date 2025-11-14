lines = [line.split(":")[1] for line in open(0).read().splitlines()]

total = 0

for i, a in enumerate(lines):
    for j, b in enumerate(lines[i + 1:], i + 1):
        for k, c in enumerate(lines):
            if i == k or j == k: continue
            if all(p == r or q == r for p, q, r in zip(a, b, c)):
                sim1 = sum(x == y for x, y in zip(a, c))
                sim2 = sum(x == y for x, y in zip(b, c))
                total += sim1 * sim2

print(total)