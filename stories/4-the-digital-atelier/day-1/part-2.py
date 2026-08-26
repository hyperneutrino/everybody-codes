total = 0

for line in open(0):
    position = 0
    visited = set()
    for step in map(int, line.split(",")):
        if position - step > 0 and position - step not in visited:
            position -= step
        else:
            position += step
            while position in visited:
                position += 1
        visited.add(position)
    total += position

print(total)