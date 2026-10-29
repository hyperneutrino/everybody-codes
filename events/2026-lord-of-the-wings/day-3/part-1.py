# Since we want to line up the digits in the standard and the vote, we can use zip, which lines up
# corresponding values of one or more lists, basically transposing the inputs. We reverse this so
# we can enumerate the pairs to get the indexes, which determine the exponents, starting at 0. The
# list conversion is only because reversed doesn't work on a zip object.

total = 0

for line in open(0):
    left, right = line.replace("ISO-", "").split()
    for exponent, (base, coefficient) in enumerate(reversed(list(zip(left, right)))):
        total += int(base) ** exponent * int(coefficient)

print(total)