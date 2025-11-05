real, imag = map(int, input()[3:-1].split(","))
A = real + imag * 1j

def div(x, y):
    return int(x.real / y.real) + int(x.imag / y.imag) * 1j

count = 0

for real in range(0, 1001):
    for imag in range(0, 1001):
        P = (A.real + real) + (A.imag + imag) * 1j
        R = 0
        exceeded = False
        for _ in range(100):
            R *= R
            R = div(R, 100000 + 100000j)
            R += P
            if abs(R.real) > 1000000 or abs(R.imag) > 1000000:
                exceeded = True
                break
        if not exceeded:
            count += 1

print(count)