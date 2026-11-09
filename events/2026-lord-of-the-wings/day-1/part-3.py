import math

nums = list(map(int, input().split(",")))
total = 0

for num in nums:
    s = math.ceil(math.sqrt(num + 1))
    total += (s + 1 - s % 2) ** 2 - 1 - num

print(total)