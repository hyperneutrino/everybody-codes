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

total = 0

for row in range(height):
    for col in range(width):
        if is_isolated(row, col):
            total += 1

print(total)