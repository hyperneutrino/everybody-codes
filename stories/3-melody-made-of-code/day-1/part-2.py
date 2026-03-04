best_id = None
max_shine = None
min_rgb = None

for line in open(0):
    id, rest = line.split(":")
    id = int(id)
    r, g, b, s = [int("".join("1" if ch.isupper() else "0" for ch in block), 2) for block in rest.split()]

    if (best_id is None) or (s > max_shine) or (s == max_shine and r + g + b < min_rgb):
        best_id = id
        max_shine = s
        min_rgb = r + g + b

print(best_id)