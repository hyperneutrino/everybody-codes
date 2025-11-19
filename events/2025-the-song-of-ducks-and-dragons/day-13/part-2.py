intervals = [tuple(map(int, line.split("-"))) for line in open(0)]

dial = [1]

right = True

for x, y in intervals:
    if x <= y:
        nums = list(range(x, y + 1))
    else:
        nums = list(range(y, x - 1, -1))

    if right:
        dial += nums
    else:
        dial = nums[::-1] + dial
    
    right = not right

print(dial[(dial.index(1) + 20252025) % len(dial)])