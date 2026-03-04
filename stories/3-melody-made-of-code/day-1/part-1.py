total = 0

for line in open(0):
    id, rest = line.split(":")
    id = int(id)
    r, g, b = [int("".join("1" if ch.isupper() else "0" for ch in block), 2) for block in rest.split()]
    if g > r and g > b:
        total += id

print(total)