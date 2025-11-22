import heapq

instructions = [(section[0], int(section[1:])) for section in input().split(",")]

class Wall:
    def __init__(self, horizontal, start, end):
        self.horizontal = horizontal
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{"horizontal" if self.horizontal else "vertical"} wall from {self.start} to {self.end}"

walls = []

d = 1j
p = 0

poi_reals = set()
poi_imags = set()

for index, (turn, size) in enumerate(instructions):
    if turn == "R":
        d *= -1j
    else:
        d *= 1j
    
    end = p + d * size

    if index == len(instructions) - 1:
        end -= d

    walls.append(Wall(d in [1, -1], p + d, end))
    p += d * size
    
    if d in [1, -1]:
        poi_imags |= { p.imag - 1, p.imag, p.imag + 1 }
    else:
        poi_reals |= { p.real - 1, p.real, p.real + 1 }

end = p

poi_reals.add(end.real)
poi_imags.add(end.imag)

seen = set()
pq = [(0, 0, 0)]

inc = 0

while len(pq) > 0:
    dist, _, curr = heapq.heappop(pq)

    if curr == end:
        print(int(dist))
        break

    if curr in seen: continue
    seen.add(curr)

    for d in [1, -1, 1j, -1j]:
        horizontal = d in [1, -1]
        farthest = float("inf")
        for wall in walls:
            if horizontal:
                if curr.imag < min(wall.start.imag, wall.end.imag): continue
                if curr.imag > max(wall.start.imag, wall.end.imag): continue
                if d == 1:
                    pt = min(wall.start.real, wall.end.real)
                    if pt > curr.real:
                        farthest = min(farthest, pt - curr.real - 1)
                else:
                    pt = max(wall.start.real, wall.end.real)
                    if pt < curr.real:
                        farthest = min(farthest, curr.real - pt - 1)
            else:
                if curr.real < min(wall.start.real, wall.end.real): continue
                if curr.real > max(wall.start.real, wall.end.real): continue
                if d == 1j:
                    pt = min(wall.start.imag, wall.end.imag)
                    if pt > curr.imag:
                        farthest = min(farthest, pt - curr.imag - 1)
                else:
                    pt = max(wall.start.imag, wall.end.imag)
                    if pt < curr.imag:
                        farthest = min(farthest, curr.imag - pt - 1)
        if horizontal:
            for poi in poi_reals:
                if d == 1 and poi <= curr.real or d == -1 and poi >= curr.real: continue
                step = abs(poi - curr.real)
                if step > farthest: continue
                n = poi + curr.imag * 1j
                if n in seen: continue
                heapq.heappush(pq, (dist + step, inc := inc + 1, n))
        else:
            for poi in poi_imags:
                if d == 1j and poi <= curr.imag or d == -1j and poi >= curr.imag: continue
                step = abs(poi - curr.imag)
                if step > farthest: continue
                n = curr.real + poi * 1j
                if n in seen: continue
                heapq.heappush(pq, (dist + step, inc := inc + 1, n))