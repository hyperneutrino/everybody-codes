line = input()

total = 0

for i in range(len(line)):
    for j in range(i + 1, len(line)):
        if line[i] == line[j].upper() and line[j].islower():
            total += 1

print(total)