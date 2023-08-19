def insert(num, d, D, s, z):
    n0 = num // d
    n1 = num % d

    if z and n0 == 0:
        return None

    return n0 * d * D + s * d + n1


INF = 10**17

T = int(input())
Ans = []
for _ in range(T):
    S, L, R = input().split()
    L = int(L)
    R = int(R)

    D = 10 ** len(S)
    s = int(S)
    z = S[0] == "0"

    ans = 0

    for i in range(18):
        d = 10**i

        if s * d > R:
            break

        ngL = -1
        okL = INF
        while okL - ngL > 1:
            tgt = (okL + ngL) // 2
            t = insert(tgt, d, D, s, z)
            if t is None or t < L:
                ngL = tgt
            else:
                okL = tgt

        if insert(okL, d, D, s, z) > R:
            continue

        ngR = INF
        okR = okL
        while ngR - okR > 1:
            tgt = (okR + ngR) // 2
            t = insert(tgt, d, D, s, z)
            if t > R:
                ngR = tgt
            else:
                okR = tgt

        # print(i, d, okL, okR)
        ans += okR - okL + 1
    # print(ans)

    Ans.append(ans)

for a in Ans:
    print(a)
