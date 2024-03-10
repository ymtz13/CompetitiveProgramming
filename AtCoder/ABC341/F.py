N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    E[u].append(v)
    E[v].append(u)

W = list(map(int, input().split()))
A = list(map(int, input().split()))

WI = [(w, i) for i, w in enumerate(W)]
WI.sort()

C = [0] * N

INF = 1 << 60

for w, i in WI:
    dp = [-INF] * w
    dp[0] = 0
    for j in E[i]:
        wj = W[j]
        if wj >= w:
            continue
        cj = C[j]

        for k in range(w - 1, wj - 1, -1):
            dp[k] = max(dp[k], dp[k - wj] + cj)

    c = 1 + max(dp)
    C[i] = c

ans = 0
for a, c in zip(A, C):
    ans += a * c
print(ans)
