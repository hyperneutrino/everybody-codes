import math

segments = [list(map(int, line.split(","))) for line in open(0)]
segments.sort()

flaps = 0
position = 0
height = 0

for i in range(len(segments)):
    minhr = 0
    next_pos = segments[i][0]
    for x, h, _ in segments[i:]:
        minhr = max(minhr, h - (x - next_pos))
    sprint = max(0, int(math.ceil((minhr - height + next_pos - position) / 2)))
    flaps += sprint
    height += sprint - (next_pos - position - sprint)
    position = next_pos

print(flaps)