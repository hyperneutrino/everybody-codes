nums = list(map(int, open(0)))

dial = [1]

right = True

for num in nums:
    if right:
        dial.append(num)
    else:
        dial.insert(0, num)
    
    right = not right

print(dial[(dial.index(1) + 2025) % len(dial)])