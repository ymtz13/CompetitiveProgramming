def f(x):
    r = {x}
    for d in range(2, x + 1):
        if d * d > x:
            break
        if x % d == 0:
            r.add(d)
            r.add(x // d)

    return r


INF = 1 << 60

A, B = sorted(map(int, input().split()))
ans = 0

while A > 0 and B > 0:
    D = B - A
    if D == 0:
        ans += 1
        break
    if D == 1:
        ans += A
        break

    minR = INF
    minRd = None

    for d in f(D):
        rA = A % d
        rB = B % d
        if rA != rB:
            continue

        if rA < minR:
            minR = rA
            minRd = d

    # print(A, B, minR, minRd)

    ans += minR
    A -= minR
    B -= minR
    A //= minRd
    B //= minRd


print(ans)
