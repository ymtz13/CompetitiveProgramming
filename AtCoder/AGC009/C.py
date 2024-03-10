mod = 10**9 + 7
INF = 1 << 60

N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]

if A < B:
    A, B = B, A

for l, r in zip(S, S[2:]):
    if r - l < B:
        print(0)
        exit()

p = -INF
X = []
for s in S:
    if s - p >= A:
        X.append([])
    X[-1].append(s)
    p = s


ans = 1
for x in X:
    y = [-INF] + x

    i = 0
    L = [None]
    for s in x:
        while y[i + 1] + A <= s:
            i += 1
        L.append(i)
    # print(x, L)

    V = [1]
    R = [0, 1]
    z = -1
    for i, s in enumerate(x, 1):
        j = L[i]
        v = (R[j + 1] - R[min(z + 1, j + 1)]) % mod
        V.append(v)
        R.append((R[-1] + v) % mod)

        if s - y[i - 1] < B:
            z = i - 2

        # print((i, s), V, R, z)

    ans *= R[-1] - R[z + 1]
    ans %= mod

print(ans)
