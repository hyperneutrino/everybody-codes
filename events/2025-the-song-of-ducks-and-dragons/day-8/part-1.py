NAILS = 32

nums = list(map(int, input().split(",")))

total = 0

for x, y in zip(nums, nums[1:]):
    if abs(x - y) == NAILS / 2:
        total += 1

print(total)