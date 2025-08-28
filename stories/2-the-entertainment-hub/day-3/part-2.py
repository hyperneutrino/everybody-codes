class Die:
    def __init__(self, id, faces, seed):
        self.id = id
        self.faces = faces
        self.seed = seed
        self.pulse = seed
        self.roll_number = 1
        self.face = 0
    
    def roll(self):
        spin = self.roll_number * self.pulse
        self.face = (self.face + spin) % len(self.faces)
        self.pulse += spin
        self.pulse %= self.seed
        self.pulse = self.pulse + 1 + self.roll_number + self.seed
        self.roll_number += 1
        return self.faces[self.face]

raw = open(0).read()
lines, track = raw.split("\n\n")

dice = []

for line in lines.split("\n"):
    parts = line.split()
    id = int(parts[0][:-1])
    faces = list(map(int, parts[1].split("=")[1][1:-1].split(",")))
    seed = int(parts[2].split("=")[1])
    dice.append(Die(id, faces, seed))

track = list(map(int, track))

turns = []

for die in dice:
    turn = 0
    for x in track:
        while True:
            turn += 1
            if die.roll() == x:
                break
    turns.append(turn)

indexes = list(range(len(turns)))
indexes.sort(key=lambda index: turns[index])

print(*[x + 1 for x in indexes], sep=",")