# real, imag = map(int, input()[3:-1].split(","))
# A = real + imag * 1j

# def div(x, y):
#     return int(x.real / y.real) + int(x.imag / y.imag) * 1j

# R = 0

# for _ in range(3):
#     R *= R
#     R = div(R, 10 + 10j)
#     R += A

# print(f"[{int(R.real)},{int(R.imag)}]")

real, imag = map(int, input()[3:-1].split(","))
A = [real, imag]

def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]

def mul(x, y):
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + y[0] * x[1]]

def div(x, y):
    return [int(x[0] / y[0]), int(x[1] / y[1])]

R = [0, 0]

for _ in range(3):
    R = mul(R, R)
    R = div(R, [10, 10])
    R = add(R, A)

print(R)