lines = [line.split(":")[1] for line in open(0).read().splitlines()]

a, b, c = lines

sim1 = sum(x == y for x, y in zip(a, c))
sim2 = sum(x == y for x, y in zip(b, c))

print(sim1 * sim2)