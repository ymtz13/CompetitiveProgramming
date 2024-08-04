def popcount(X):
    c = 0
    for i in range(70):
        bit = 1 << i
        if X & bit:
            c += 1
    return c


def solve(a, b, C):
    c = popcount(C)

    if a + b < c:
        return (-1,)

    if (a + b - c) % 2:
        return (-1,)

    d = (a + b - c) // 2

    if d > 60 - c or d > a or d > b:
        return (-1,)

    A = B = 0

    xa = a - d
    xd = d

    for i in range(70):
        bit = 1 << i
        if C & bit:
            if xa:
                xa -= 1
                A += bit
            else:
                B += bit
        else:
            if xd:
                xd -= 1
                A += bit
                B += bit

    # print(f"{A:060b}")
    # print(f"{B:060b}")
    # print(f"{C:060b}")

    return (A, B)


a, b, C = map(int, input().split())
ans = solve(a, b, C)
print(*ans)
