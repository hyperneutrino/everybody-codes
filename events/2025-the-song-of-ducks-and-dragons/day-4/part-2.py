import math

lines = open(0).read().splitlines()
x = int(lines[0])
y = int(lines[-1])

print(math.ceil(10000000000000 * y / x))
