## could also do this with a generator using yield pretty easily,
## but I thought of the class approach first

# def die(faces, seed):
#     pulse = seed
#     roll_number = 1
#     face = 0

#     while True:
#         spin = roll_number * pulse
#         face = (face + spin) % len(faces)
#         pulse = (pulse + spin) % seed + 1 + roll_number + seed
#         roll_number += 1
#         yield faces[face]

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

dice = []

for line in open(0):
    parts = line.split()
    id = int(parts[0][:-1])
    faces = list(map(int, parts[1].split("=")[1][1:-1].split(",")))
    seed = int(parts[2].split("=")[1])
    dice.append(Die(id, faces, seed))

rolls = 0
total = 0

while True:
    rolls += 1
    total += sum(die.roll() for die in dice)
    if total >= 10000:
        break

print(rolls)