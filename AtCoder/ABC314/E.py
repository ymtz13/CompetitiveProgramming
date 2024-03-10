N, M = map(int, input().split())

CS = []

for _ in range(N):
    V = tuple(map(int, input().split()))

    C = V[0]
    P = V[1]
    S = V[2:]

    T = [s for s in S if s]

    n0 = P - len(T)
    p0 = n0 / P

    if n0 == P:
        continue

    C = C / (1 - p0)

    CS.append((C, T))

    #    E / (1-p0) = 1 + 2p0 + 3p0^2 + ...
    # p0 E / (1-p0) =     1p0 + 2p0^2 + ...
    #    E          = 1 +  p0 +  p0^2 + ... = 1 / (1-p0)

dp = [0]
for m in range(1, M + 1):
    vmin = 1 << 60
    for C, S in CS:
        v = 0
        for s in S:
            v += dp[max(0, m - s)]
        v /= len(S)
        v += C

        vmin = min(vmin, v)

    dp.append(vmin)

print(dp[-1])
