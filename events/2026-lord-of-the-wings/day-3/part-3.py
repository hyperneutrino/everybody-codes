# There are *much* smarter ways of doing this, but the inputs are small enough that we can just
# check every possible smaller representation and see if it matches.

def convert(standard, vote):
    total = 0
    for exponent, coefficient in enumerate(vote):
        base = standard[exponent % len(standard)]
        total += base ** exponent * coefficient
    return total

total = 0

for line in open(0):
    left, right = line.replace("ISO2-", "").split()
    standard = list(map(int, left))[::-1]
    vote = list(map(int, right))[::-1]
    value = convert(standard, vote)
    for check in range(1, int(right)):
        sequence = list(map(int, str(check)))[::-1]
        if convert(standard, sequence) == value:
            # This means we found a smaller sequence that works, so we discard this vote.
            break
    else:
        # This means `break` didn't fire, so we keep this vote.
        total += value

print(total)