import math

nums = list(map(int, input().split(",")))
total = 0

for num in nums:
    total += math.ceil(math.sqrt(num)) ** 2 - num

print(total)