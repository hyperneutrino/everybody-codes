import re

thicknesses = {}
link_branches = {}

blocks, tests = open(0).read().split("\n\n\n")

for block in blocks.split("\n\n"):
    plant, *branches = block.splitlines()

    match = re.match(r"^Plant (\d+) with thickness (\d+):$", plant)
    assert match is not None
    plant_number = int(match[1])
    plant_thickness = int(match[2])
    thicknesses[plant_number] = plant_thickness

    for branch in branches:
        if branch.startswith("- free"):
            break

        match = re.match(r"^- branch to Plant (\d+) with thickness (-?\d+)$", branch)
        assert match is not None
        source_plant = int(match[1])
        branch_thickness = int(match[2])

        if plant_number not in link_branches: link_branches[plant_number] = []
        link_branches[plant_number].append((source_plant, branch_thickness))

plant_count = len(thicknesses)

def calculate(activations):
    energy = {index: value for index, value in enumerate(activations, 1)}

    for plant in range(len(activations) + 1, plant_count + 1):
        energy[plant] = sum(energy[source] * thickness for (source, thickness) in link_branches[plant])

        if energy[plant] < thicknesses[plant]:
            energy[plant] = 0

    return energy[plant_count]

total = 0

for test in tests.splitlines():
    total += calculate(list(map(int, test.split())))

print(total)