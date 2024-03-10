mod = 10**9 + 7

N, K = map(int, input().split())

D = []
for d in range(1, N + 10):
    if d * d > N:
        break

    D.append(d)
    if d != N // d:
        D.append(N // d)

D.sort()
E = [1] + [r - l for l, r in zip(D, D[1:])]


dp = D[:]

for _ in range(K - 1):
    V = []
    for i, v in enumerate(reversed(dp)):
        V.append(E[i] * v % mod)

    S = []
    s = 0
    for v in V:
        s += v
        s %= mod
        S.append(s)

    dp = S

print(dp[-1])
