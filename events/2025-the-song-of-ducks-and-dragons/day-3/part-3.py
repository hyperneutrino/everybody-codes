sizes = list(map(int, input().split(",")))
count = {}

for size in sizes:
    count[size] = count.get(size, 0) + 1

print(max(count.values()))