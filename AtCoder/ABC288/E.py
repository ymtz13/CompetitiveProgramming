INF = 1 << 60


N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
X = set(map(int, input().split()))

Min = []
for l in range(N):
    mins = [None] * l
    m = INF
    for c in C[l:]:
        m = min(m, c)
        mins.append(m)
    Min.append(mins)


dp = [INF] * (N + 1)
dp[0] = 0
for ia, a in enumerate(A):
    required = (ia + 1) in X

    if required:
        for i in range(ia, -1, -1):
            dp[i + 1] = dp[i] + a + Min[ia - i][ia]
        dp[0] = INF

    else:
        for i in range(ia, -1, -1):
            dp[i + 1] = min(dp[i + 1], dp[i] + a + Min[ia - i][ia])


print(min(dp))
