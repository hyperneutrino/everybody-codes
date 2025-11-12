import functools

names, lines = open(0).read().split("\n\n")
names = names.split(",")
lines = lines.splitlines()

names = [name for name in names if not any(name != test and name.startswith(test) for test in names)]

rules = {}

for line in lines:
    left, right = line.split(" > ")
    rules[left] = right.split(",")

total = 0

@functools.cache
def generate(last, length):
    count = 0

    if length >= 7: count += 1
    if length >= 11: return count
    
    for next in rules.get(last, []):
        count += generate(next, length + 1)

    return count

for index, name in enumerate(names, start=1):
    for x, y in zip(name, name[1:]):
        if y not in rules.get(x, []):
            break
    else:
        total += generate(name[-1], len(name))

print(total)