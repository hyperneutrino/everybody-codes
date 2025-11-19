intervals = [tuple(map(int, line.split("-"))) for line in open(0)]

dial = [(1, 1)]

right = True

for x, y in intervals:
    if right:
        dial.append((x, y))
    else:
        dial.insert(0, (y, x))
    
    right = not right

index_of_one = dial.index((1, 1))
dial = dial[index_of_one:] + dial[:index_of_one]

size = sum(abs(x - y) + 1 for x, y in dial)
index = 202520252025 % size

for x, y in dial:
    if index > abs(x - y):
        index -= abs(x - y) + 1
        continue
    
    if x > y:
        print(x - index)
    else:
        print(x + index)
    
    break