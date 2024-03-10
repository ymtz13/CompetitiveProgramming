from collections import defaultdict

INF = 1 << 60

H, W, K = map(int, input().split())
A1 = [tuple(map(int, input().split())) for _ in range(H)]

# H, W, K = 13, 3, 26
# A1 = [tuple(range(i * W + 1, i * W + W + 1)) for i in range(H)]

A2 = [t[::-1] for t in A1[::-1]]

N1 = (H + W - 2) // 2
N2 = H + W - 2 - N1


def f(A, N, inc):
    ret = [[] for _ in range(H)]
    for b in range(1 << N):
        M = [(b >> i) & 1 for i in range(N)]
        nH = len([m for m in M if m == 1])
        nW = N - nH
        if nH >= H or nW >= W:
            continue

        h = w = 0
        R = [INF, 0]
        for m in M:
            R.append(A[h][w])

            if m:
                h += 1
            else:
                w += 1
        if inc:
            R.append(A[h][w])
        R.sort(reverse=True)
        ret[nH].append(R)
    return ret


Rs1 = f(A1, N1, True)
Rs2 = f(A2, N2, False)

ans = INF
for h1 in range(H):
    w = N1 - h1
    if not 0 <= w < W:
        continue

    a = A1[h1][w]
    h2 = H - 1 - h1

    R1 = Rs1[h1]
    R2 = Rs2[h2]

    T1 = [defaultdict(lambda: INF) for _ in range(N1 + 2)]
    T2 = [defaultdict(lambda: INF) for _ in range(N2 + 20)]

    Z = 1 << 30

    for r in R1:
        s = -INF
        for n, (p, q) in enumerate(zip(r, r[1:])):
            s += p
            t1 = T1[n]
            key = p * Z + q
            t1[key] = min(t1[key], s)

    for r in R2:
        s = -INF
        for n, (p, q) in enumerate(zip(r, r[1:])):
            s += p
            t2 = T2[n]
            key = p * Z + q
            t2[key] = min(t2[key], s)

    for n1, t1 in enumerate(T1):
        t2 = T2[K - n1]
        for key1, s1 in t1.items():
            for key2, s2 in t2.items():
                p1, q1 = key1 // Z, key1 % Z
                p2, q2 = key2 // Z, key2 % Z

                if q1 > p2:
                    continue
                if q2 > p1:
                    continue
                ans = min(ans, s1 + s2)


print(ans)
