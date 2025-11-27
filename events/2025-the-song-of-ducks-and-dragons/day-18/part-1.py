import re

thicknesses = {}
free_branches = set()
link_branches = {}

for block in open(0).read().split("\n\n"):
    plant, *branches = block.splitlines()

    match = re.match(r"^Plant (\d+) with thickness (\d+):$", plant)
    assert match is not None
    plant_number = int(match[1])
    plant_thickness = int(match[2])
    thicknesses[plant_number] = plant_thickness

    for branch in branches:
        if branch.startswith("- free"):
            free_branches.add(plant_number)
            break

        match = re.match(r"^- branch to Plant (\d+) with thickness (\d+)$", branch)
        assert match is not None
        source_plant = int(match[1])
        branch_thickness = int(match[2])

        if plant_number not in link_branches: link_branches[plant_number] = []
        link_branches[plant_number].append((source_plant, branch_thickness))

plant_count = len(thicknesses)

energy = {}

for plant in range(1, plant_count + 1):
    if plant in free_branches:
        energy[plant] = 1
    else:
        energy[plant] = sum(energy[source] * thickness for (source, thickness) in link_branches[plant])
    
    if energy[plant] < thicknesses[plant]:
        energy[plant] = 0

print(energy[plant_count])