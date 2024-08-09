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

    IX = []
    i = 0
    for x in X:
        IX.append((i, x))
        if x == 0:
            i += lS
        else:
            i += lT

    M = []

    i = 0
    j = 0
    for y in Y:
        if y == 0:
            inxt = i + lS
        else:
            inxt = i + lT

        M.append((IX[j], (i, y)))

        while j + 1 < len(IX) and IX[j + 1][0] < inxt:
            j += 1
            M.append(((i, y), IX[j]))

        i = inxt

    print(M)


solve("araara", "01", "111")
exit()


t = int(input())

for _ in range(t):
    S = input()
    X = input()
    Y = input()

    ans = solve(S, X, Y)
    print("Yes" if ans else "No")
