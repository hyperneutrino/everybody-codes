qualities = []

for line in open(0):
    _, rest = line.split(":")
    id = int(id)
    nums = list(map(int, rest.split(",")))

    sword = []

    for num in nums:
        for segment in sword:
            if num < segment[1] and segment[0] is None:
                segment[0] = num
                break
            if num > segment[1] and segment[2] is None:
                segment[2] = num
                break
        else:
            sword.append([None, num, None])

    qualities.append(int("".join(str(segment[1]) for segment in sword)))

print(max(qualities) - min(qualities))