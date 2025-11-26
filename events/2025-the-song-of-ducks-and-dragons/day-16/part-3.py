nums = list(map(int, input().split(",")))

spell = []

while any(n > 0 for n in nums):
    index = [n > 0 for n in nums].index(True)
    spell.append(index + 1)
    for i in range(index, len(nums), index + 1):
        nums[i] -= 1

blocks = 202520252025000

lo = 0
hi = blocks

while lo < hi:
    mi = (lo + hi) // 2
    count = sum(mi // n for n in spell)
    if count == blocks:
        break
    if count > blocks:
        hi = mi - 1
    else:
        lo = mi + 1

print(lo)
