NAILS = 256

nums = list(map(int, input().split(",")))

total = 0
strings = []

for x, y in zip(nums, nums[1:]):
    for a, b in strings:
        if x == a or x == b or y == a or y == b: continue
        if (a < x < b) != (a < y < b):
            total += 1
    strings.append(sorted([x, y]))

print(total)