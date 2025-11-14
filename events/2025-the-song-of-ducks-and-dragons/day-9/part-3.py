lines = [line.split(":")[1] for line in open(0).read().splitlines()]

def to_num(line):
    num = 0
    for symbol in line:
        num *= 16
        num += 2 ** "ATCG".index(symbol)
    return num

nums = list(map(to_num, lines))

ands = [[x & y for y in nums] for x in nums]

conns = [[] for _ in range(len(nums) + 1)]

for i, a in enumerate(nums, 1):
    for j, b in enumerate(nums[i:], i + 1):
        for k, c in enumerate(nums, 1):
            if i == k or j == k: continue
            if ands[i - 1][k - 1] | ands[j - 1][k - 1] == c:
                conns[k].append(i)
                conns[k].append(j)
                conns[i].append(k)
                conns[j].append(k)

seen = set()
best = []

for start in range(1, len(nums) + 1):
    if start in seen: continue
    seen.add(start)
    family = [start]
    for current in family:
        for neighbor in conns[current]:
            if neighbor in seen: continue
            seen.add(neighbor)
            family.append(neighbor)
    if len(family) > len(best): best = family

print(sum(best))