get = lambda: input().split("=")[1]

width = int(get())
height = int(get())
horizontal = list(map(int, get()))
vertical = list(map(int, get()))

def has_line_left(row, col):
    return vertical[col % len(vertical)] == row % 2

def has_line_up(row, col):
    return horizontal[row % len(horizontal)] == col % 2

def is_isolated(row, col):
    return has_line_left(row, col) and has_line_up(row, col) and has_line_left(row, col + 1) and has_line_up(row + 1, col)

parent = { (row, col): (row, col) for row in range(height) for col in range(width) }

def root(point):
    if parent[point] == point: return point
    parent[point] = root(parent[point])
    return parent[point]

def connect(left, right):
    parent[root(left)] = root(right)

for row in range(height):
    for col in range(1, width):
        if not has_line_left(row, col):
            connect((row, col - 1), (row, col))

for col in range(width):
    for row in range(1, height):
        if not has_line_up(row, col):
            connect((row - 1, col), (row, col))

colors = { root((0, 0)): False }

for row in range(height):
    for col in range(width):
        index = root((row, col))
        if index in colors: continue
        colors[index] = not colors[root((row, col - 1) if row == 0 else (row - 1, col))]

totals = [0, 0]

for row in range(height):
    for col in range(width):
        if is_isolated(row, col):
            totals[colors[root((row, col))]] += 1

print(max(totals))