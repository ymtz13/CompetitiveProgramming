from math import sqrt, cos, pi

A, B = sorted(map(int, input().split()))

if B / A >= 2 / sqrt(3):
    print(A * 2 / sqrt(3))
    exit()


def f(x):
    return min(A / cos(x), B / cos(pi / 6 - x))


l = 0
r = pi / 6
while r - l > 1e-10:
    d = (r - l) / 3

    x1 = l + d
    x2 = x1 + d

    f1 = f(x1)
    f2 = f(x2)

    if f1 > f2:
        r = x2
    else:
        l = x1

print(f(r))
