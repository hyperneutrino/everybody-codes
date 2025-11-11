def calculate(line):
    total = 0
    
    slice = line[:1001]
    count = { "A": 0, "B": 0, "C": 0 }
    for ch in slice:
        if ch.isupper():
            count[ch] += 1

    for i in range(len(line)):
        c = line[i]
        if c.islower():
            total += count[c.upper()]
        if i + 1001 < len(line):
            n = line[i + 1001]
            slice += n
            if n.isupper():
                count[n] += 1
        if i >= 1000:
            if slice[0].isupper():
                count[slice[0]] -= 1
            slice = slice[1:]

    return total

line = input()

one = calculate(line)
two = calculate(line * 2)

print(one + (two - one) * 999)