T = input()
N = int(input())

S = []
for _ in range(N):
    S.append(tuple(input().split()[1:]))

INF = 1 << 60
t = len(T)
dp = [INF] * (t + 1)
dp[0] = 0
for ss in S:
    ndp = dp[:]
    for s in ss:
        l = len(s)
        for i, v in enumerate(dp):
            if i + l > t:
                break
            if s == T[i : i + l]:
                ndp[i + l] = min(ndp[i + l], dp[i] + 1)

    dp = ndp

print(dp[-1] if dp[-1] < INF else -1)
