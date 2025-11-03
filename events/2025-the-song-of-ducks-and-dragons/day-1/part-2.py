names = input().split(",")
input()
instructions = input().split(",")

index = 0

for ins in instructions:
    dir = 1 if ins[0] == "R" else -1
    offset = dir * int(ins[1:])
    index += offset

print(names[index % len(names)])