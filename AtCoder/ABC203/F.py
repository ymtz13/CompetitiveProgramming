N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
A.append(0)

E = []
e = 0
for i, a in enumerate(A[:-1]):
    while A[e] > a // 2:
        e += 1
    E.append(e)

INF = 1 << 60
dp = [INF] * (32 * len(A))
dp[0] = 0

for i in range(N):
    for j in range(31):
        v = dp[i * 32 + j]

        kA = (i + 1) * 32 + j
        dp[kA] = min(dp[kA], v + 1)
        kT = E[i] * 32 + j + 1
        dp[kT] = min(dp[kT], v)

for j, v in enumerate(dp[N * 32 :]):
    if v <= K:
        print(j, v)
        break
