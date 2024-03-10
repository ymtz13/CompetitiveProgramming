X, Y = map(int, input().split())

x = abs(X)
y = abs(Y)


def s(A, B):
    return abs(X * B - Y * A)


def ans(a, b):
    for sx in (-1, 1):
        for sy in (-1, 1):
            A = sx * a
            B = sy * b
            if s(A, B) == 2:
                print(A, B)
                exit()


def no():
    print(-1)
    exit()


if x == 0:
    if y == 1:
        ans(2, 0)
    if y == 2:
        ans(1, 0)
    no()

if y == 0:
    if x == 1:
        ans(0, 2)
    if x == 2:
        ans(0, 1)
    no()


# gcd(a, b)とax+by=gcd(a,b)を満たすx,yを返す
def euclidean(a, b):
    x = w = 1
    y = z = 0
    while b:
        q = a // b
        r = a % b

        x, y, z, w = z, w, x - q * z, y - q * w
        a, b = b, r

    return a, x, y


gcd, a, b = euclidean(x, y)

if gcd == 1:
    ans(b * 2, a * 2)
if gcd == 2:
    ans(b, a)
no()
