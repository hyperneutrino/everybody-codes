sequence = list(input())
bolts = 0
bolt = "R"
next = { "R": "G", "G": "B", "B": "R" }

while len(sequence) > 0:
    while len(sequence) > 0:
        if sequence.pop(0) != bolt:
            break
    bolt = next[bolt]
    bolts += 1

print(bolts)