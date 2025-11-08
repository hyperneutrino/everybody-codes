line = input()
_, rest = line.split(":")
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

quality = "".join(str(segment[1]) for segment in sword)
print(quality)