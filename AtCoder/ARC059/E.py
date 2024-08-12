mod = 10**9 + 7

N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = [[1] * 500]  # P[r][n] = n ^ r
for _ in range(1, 410):
    P.append([n * v % mod for n, v in enumerate(P[-1])])

S = []
for pp in P:
    s = []
    v = 0
    for p in pp:
        v += p
        v %= mod
        s.append(v)
    S.append(s)

dp = [0] * (C + 1)
dp[0] = 1

for a, b in zip(A, B):
    dp_next = [0] * (C + 1)
    for c, v in enumerate(dp):
        for cc in range(C - c + 1):
            i = c + cc

            s = S[cc]
            v = (s[b] - s[a - 1]) % mod
            dp_next[i] += dp[c] * v % mod
            dp_next[i] %= mod

    dp = dp_next

print(dp[-1])
