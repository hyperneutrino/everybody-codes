total = 0

def any_intersect(arcs, arc):
    a, b = arc
    return any(a < x < b < y or x < a < y < b for x, y in arcs)

for line in open(0):
    position = 0
    visited = set()
    active = []
    inactive = []
    for step in map(int, line.split(",")):
        if (
            position - step > 0
            and position - step not in visited
            and not any_intersect(active, (position - step, position))
        ):
            active.append((position - step, position))
            position -= step
        else:
            fail = False
            while (
                position + step in visited 
                or any_intersect(active, (position, position + step))
            ):
                if any(x < position < y < position + step for x, y in active):
                    fail = True
                    break
                step += 1
            if fail: continue
            active.append((position, position + step))
            position += step
        visited.add(position)
        active, inactive = inactive, active
    total += position

print(total)