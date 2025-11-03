names = input().split(",")
input()
instructions = input().split(",")

for ins in instructions:
    dir = 1 if ins[0] == "R" else -1
    offset = dir * int(ins[1:]) % len(names)
    names[0], names[offset] = names[offset], names[0]

print(names[0])