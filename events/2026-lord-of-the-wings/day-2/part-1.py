# Admittedly, this entire solution is slightly overkill. There are only 5 blades so there are only
# 120 possible orderings. We could simply try them all. Since we have every pair, we could also
# just loop for the one that wins every match, remove all of its pairs, and repeat.

checksum = 0

for line in open(0):
    comparisons = line.split()
    pairs = []
    for item in comparisons:
        if ">" in item:
            better, worse = tuple(map(int, item.split(">")))
        else:
            worse, better = tuple(map(int, item.split("<")))
        pairs.append((better, worse))
    blades = set(sum(pairs, ()))

    # Let the in-degree of a blade be the number of blades better than it (basically, if we order
    # the blades on a DAG (directed acyclic graph) with the edges pointing from better to worse,
    # the in-degree is the number of edges pointing IN to the node). Then, we repeatedly select a
    # blade with in-degree 0 (the best) and place it next, then reduce the in-degree of each blade
    # known to be worse than it by one. This is topological sort and means that blades will never
    # be output out-of-order by the listed comparisons. This is not always unique if the graph
    # doesn't carry enough information, but we can assume the comparisons form a total ordering in
    # this problem. Tracking in-degree -> blade would be more efficient but is overkill.
    in_degrees = { blade: 0 for blade in blades }
    worse_blades = { blade: [] for blade in blades }

    for better, worse in pairs:
        worse_blades[better].append(worse)
        in_degrees[worse] += 1

    number = 0

    for _ in range(len(blades)):
        for blade in in_degrees:
            if in_degrees[blade] == 0:
                del in_degrees[blade]
                break
        else:
            raise RuntimeError("No blade with in-degree 0 found.")

        number = number * 10 + blade

        for worse in worse_blades[blade]:
            in_degrees[worse] -= 1

    checksum += number

print(checksum)