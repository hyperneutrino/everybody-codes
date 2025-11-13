NAILS = 256

nums = list(map(int, input().split(",")))

total = 0

cuts = [[0] * NAILS for _ in range(NAILS)]

def add(r1, c1, r2, c2):
    if r1 < 1: return
    if c1 < 1: return
    if r1 > NAILS: return
    if c1 > NAILS: return
    cuts[r1 - 1][c1 - 1] += 1
    if c2 < NAILS: cuts[r1 - 1][c2] -= 1
    if r2 < NAILS: cuts[r2][c1 - 1] -= 1
    if c2 < NAILS > r2: cuts[r2][c2] += 1

for x, y in zip(nums, nums[1:]):
    a, b = sorted([x, y])
    add(a + 1, b + 1, b - 1, NAILS)
    add(1, a + 1, a - 1, b - 1)
    add(a, b, a, b)

for r in range(1, NAILS):
    for c in range(NAILS):
        cuts[r][c] += cuts[r - 1][c]

for r in range(NAILS):
    for c in range(1, NAILS):
        cuts[r][c] += cuts[r][c - 1]

print(max(map(max, cuts)))