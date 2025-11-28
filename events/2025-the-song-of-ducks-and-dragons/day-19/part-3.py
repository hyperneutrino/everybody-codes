import math
import functools

segments = {}

for line in open(0):
    x, h, o = map(int, line.split(","))
    if x not in segments: segments[x] = []
    segments[x].append((h, o))

@functools.cache
def solve(position, height):
    future_pos = sorted(pos for pos in segments if pos > position)
    if len(future_pos) == 0: return 0
    next_pos, *future_pos = future_pos

    optimal = float("inf")

    global_minhr = 0
    global_maxhr = float("inf")

    for pos in future_pos:
        lh, _ = min(segments[pos])
        hh, ho = max(segments[pos])
        global_minhr = max(global_minhr, lh - (pos - next_pos))
        global_maxhr = min(global_maxhr, hh + ho - 1 + (pos - next_pos))

    for H, O in segments[next_pos]:
        minhr = max(global_minhr, H)
        maxhr = min(global_maxhr, H + O - 1)

        minsprint = max(0, int(math.ceil((minhr - height + next_pos - position) / 2)))
        maxsprint = max(0, (maxhr - height + next_pos - position) // 2)

        for sprint in range(minsprint, maxsprint + 1):
            newheight = height + sprint - (next_pos - position - sprint)
            optimal = min(optimal, sprint + solve(next_pos, newheight))

    return optimal

print(solve(0, 0))