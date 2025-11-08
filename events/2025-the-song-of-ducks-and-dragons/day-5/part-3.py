swords = []

for line in open(0):
    id, rest = line.split(":")
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

    quality = int("".join(str(segment[1]) for segment in sword))
    levels = [int("".join("" if item is None else str(item) for item in segment)) for segment in sword]
    identifier = int(id)

    swords.append([quality, levels, identifier])

swords.sort(reverse=True)
ids = [sword[2] for sword in swords]
print(sum(index * id for index, id in enumerate(ids, start=1)))