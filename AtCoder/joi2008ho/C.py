N, M = map(int, input().split())
P = [int(input()) for _ in range(N)] + [0]

X1 = []
for i, p1 in enumerate(P):
    for p2 in P[i:]:
        X1.append(p1 + p2)

X1.sort()
X2 = [-(1 << 60)] + X1[:] + [1 << 61]

i = 0
ans = 0
for x1 in reversed(X1):
    while x1 + X2[i + 1] <= M:
        i += 1

    ans = max(ans, x1 + X2[i])

print(ans)
