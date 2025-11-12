names, lines = open(0).read().split("\n\n")
names = names.split(",")
lines = lines.splitlines()

rules = {}

for line in lines:
    left, right = line.split(" > ")
    rules[left] = right.split(",")
    
for name in names:
    for x, y in zip(name, name[1:]):
        if y not in rules.get(x, []):
            break
    else:
        print(name)