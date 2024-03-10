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
        ret[nH].append((R, sum(R) - INF))
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

    if K <= 1:
        for r1, _ in R1:
            for r2, _ in R2:
                ss = 0
                i1 = i2 = 1
                for k in range(K):
                    v1 = r1[i1]
                    v2 = r2[i2]
                    if v1 > v2:
                        ss += v1
                        i1 += 1
                    else:
                        ss += v2
                        i2 += 1
                ans = min(ans, ss)
    else:
        for r1, s1 in R1:
            for r2, s2 in R2:
                ss = s1 + s2
                i1 = i2 = 2
                for k in range(H + W - 1 - K):
                    v1 = r1[-i1]
                    v2 = r2[-i2]
                    if v1 < v2:
                        ss -= v1
                        i1 += 1
                    else:
                        ss -= v2
                        i2 += 1
                ans = min(ans, ss)


print(ans)
