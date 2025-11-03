names = input().split(",")
input()
instructions = input().split(",")

index = 0

for ins in instructions:
    dir = 1 if ins[0] == "R" else -1
    offset = dir * int(ins[1:])
    index += offset
    if index < 0: index = 0
    if index >= len(names): index = len(names) - 1

print(names[index])