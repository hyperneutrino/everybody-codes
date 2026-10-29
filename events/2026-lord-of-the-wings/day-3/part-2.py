# We could multiply (repeat) the standard up to the required length and cut off the leading extra
# digits, but an easier way is to just enumerate the vote string and then index into the standard
# with a modulo to wrap. The first exponent is the last index, then moving backwards, so we start
# at -1 and count down in the negative direction. Modulo will return the sign of the right side.
# Reversing the standard first is also possible. Either will work just fine.

total = 0

for line in open(0):
    left, right = line.replace("ISO-", "").split()
    for exponent, coefficient in enumerate(reversed(right)):
        base = left[(-exponent - 1) % len(left)]
        total += int(base) ** exponent * int(coefficient)

print(total)