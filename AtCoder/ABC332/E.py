INF = 1 << 90

N, D = map(int, input().split())
W = list(map(int, input().split()))
m = sum(W) / D


S = []
for x in range(1 << N):
    s = sum([v for i, v in enumerate(W) if x & (1 << i)])
    d = s - m
    S.append(d * d)

E = [[] for _ in range(1 << N)]
dp = [INF] * (1 << N)

for x in range((1 << (N - 1)) - 1):
    x = x * 2 + 1

    dp[x] = S[x]

    B = [1 << i for i in range(1, N) if x & (1 << i) == 0]
    b0 = B[0]
    B1 = B[1:]
    for y in range(1 << (len(B) - 1)):
        b = b0 + sum([v for j, v in enumerate(B1) if y & (1 << j)])
        E[x].append(b)


for _ in range(D - 1):
    dp_next = [INF] * (1 << N)
    for x, v in enumerate(dp):
        if v == INF:
            continue
        for b in E[x]:
            y = x + b
            dp_next[y] = min(dp_next[y], v + S[b])
    dp = dp_next

v2 = dp[-1]

ans = v2 / D

print(ans)
