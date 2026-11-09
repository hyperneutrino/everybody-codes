import math

nums = list(map(int, input().split(",")))
total = 0

for num in nums:
    total += max(math.ceil(num / 4) * 4, 8) - num

print(total)