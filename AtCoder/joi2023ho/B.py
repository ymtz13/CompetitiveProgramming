from collections import defaultdict

N = int(input())

D = defaultdict(list)
for _ in range(N):
    X, E = map(int, input().split())
    D[X - E].append(X + E)


keys = sorted(list(D.keys()))

ans = 0
h = -(1 << 60)
for k in keys:
    if h < max(D[k]):
        ans += 1
        h = max(D[k])

print(ans)
