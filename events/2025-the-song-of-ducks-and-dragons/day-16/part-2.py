nums = list(map(int, input().split(",")))

prod = 1

while any(n > 0 for n in nums):
    index = [n > 0 for n in nums].index(True)
    prod *= index + 1
    for i in range(index, len(nums), index + 1):
        nums[i] -= 1

print(prod)
