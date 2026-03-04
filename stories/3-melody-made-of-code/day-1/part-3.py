groups = {}

for line in open(0):
    id, rest = line.split(":")
    id = int(id)
    r, g, b, s = [int("".join("1" if ch.isupper() else "0" for ch in block), 2) for block in rest.split()]

    if r > g and r > b:
        color = "red"
    elif g > r and g > b:
        color = "green"
    elif b > r and b > g:
        color = "blue"
    else:
        continue

    if s <= 30:
        shine = "matte"
    elif s >= 33:
        shine = "shiny"
    else:
        continue

    key = color + "-" + shine
    if key not in groups: groups[key] = []
    groups[key].append(id)

print(sum(max(groups.values(), key=len)))