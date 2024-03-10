mod = 998244353

N = int(input())
A = list(map(int, input().split()))

dpS = [1]
dpV = [[1] + [0] * N]
p = [0] * (N + 1)
P = [None]

s = 0
S = [0]

for i, a in enumerate(A, 1):
    X = tuple(range(1, N + 1)) if a == -1 else [a]
    # v = dpS[-1] * len(X) % mod
    vprev = dpS[-1]
    dpV_next = [0] * (N + 1)
    dpS_next = 0

    # print((i, a))
    for x in X:
        px = p[x]
        l = i - px

        v = vprev

        if l > x:
            # c = S[i - x - 1] - S[px]
            # v -= dp[px] * pow(N, c, mod) % mod
            v -= dpS[i - x - 1] - dpV[i - x - 1][x]
            v %= mod
            # print(px, l, x, c, v)
            # print(px, l, x, v)

        dpV_next[x] = v
        dpS_next += v
        dpS_next %= mod

    dpV.append(dpV_next)
    dpS.append(dpS_next)

    if a == -1:
        s += 1
    else:
        for b in range(N + 1):
            if b != a:
                p[b] = i

    P.append(p[:])
    S.append(s)


# print(dpS)
print(dpS[-1] % mod)

# for p in P:
#     print(p)
# print("S:", S)
