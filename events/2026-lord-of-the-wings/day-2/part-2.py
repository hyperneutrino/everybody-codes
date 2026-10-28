# It turns out that the part 1 solution works exactly the same for part 2, because topological sort
# will find any valid ordering, and since there's only one, then it'll find it nonetheless. The
# trivial solution mentioned in the part 1 comment (just try every ordering) would also still work
# albeit we now have 362880 permutations (9 blades) so it's less practical. Looping for the blade
# that wins every match should also still work, as ambiguity could only arise if the top two blades
# have no match (i.e. they beat all other blades but there's no comparison between them), but that
# ambiguity would be impossible to resolve and therefore not a valid input.

# This is the exact same solution as part 1 but condensed for fun.

total = 0

for line in open(0):
    pairs = []

    for item in line.split():
        if ">" in item: pairs.append(tuple(map(int, item.split(">"))))
        else: pairs.append(tuple(map(int, item.split("<")))[::-1])

    blades = set(sum(pairs, ()))
    in_degrees = { blade: 0 for blade in blades }
    worse_blades = { blade: [] for blade in blades }

    for b, w in pairs:
        worse_blades[b].append(w)
        in_degrees[w] += 1

    n = 0

    for _ in blades:
        next = [blade for blade in in_degrees if in_degrees[blade] == 0][0]
        del in_degrees[next]
        n = n * 10 + next
        for w in worse_blades[next]: in_degrees[w] -= 1

    total += n

print(total)