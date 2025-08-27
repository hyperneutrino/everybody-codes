from collections import deque

REPEAT = 100000

raw = input() * REPEAT
left = raw[:len(raw) // 2]
right = raw[len(raw) // 2:]

lseq = deque(left)
rseq = deque(right)
bolts = 0
bolt = "R"
next = { "R": "G", "G": "B", "B": "R" }

while len(lseq) > 0 or len(rseq) > 0:
    if len(lseq) != len(rseq):
        lseq.popleft()
    elif lseq[0] == bolt:
        lseq.popleft()
        rseq.popleft()
    else:
        lseq.popleft()
        lseq.append(rseq.popleft())
    bolt = next[bolt]
    bolts += 1

print(bolts)