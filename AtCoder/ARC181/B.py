def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solve(S, X, Y):
    X = list(map(int, X))
    Y = list(map(int, Y))

    nSX = X.count(0)
    nSY = Y.count(0)
    nTX = X.count(1)
    nTY = Y.count(1)
    lS = len(S)

    if nSX == nSY:
        return True

    # nSX * lS + nTX * lT = nSY * lS + nTY * lT
    # (nSX - nSY) * lS = (nTY - nTX) * lT

    d = nTX - nTY
    if d == 0 or (nSX - nSY) * lS % d != 0:
        return False
    lT = -(nSX - nSY) * lS // d

    if lT < 0:
        return False

    if lT == 0:
        return True

    g = gcd(lS, lT)

    return S == S[:g] * (lS // g)


t = int(input())

for _ in range(t):
    S = input()
    X = input()
    Y = input()

    ans = solve(S, X, Y)
    print("Yes" if ans else "No")
