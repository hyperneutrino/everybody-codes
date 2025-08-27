REPEAT = 100

sequence = list(input()) * REPEAT
bolts = 0
bolt = "R"
next = { "R": "G", "G": "B", "B": "R" }

while len(sequence) > 0:
    if len(sequence) % 2 == 1:
        sequence.pop(0)
    else:
        if sequence[0] == bolt:
            sequence.pop(len(sequence) // 2)
        sequence.pop(0)
    bolt = next[bolt]
    bolts += 1

print(bolts)