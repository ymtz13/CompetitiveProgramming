N, M = map(int, input().split())
P = [None] + list(map(int, input().split()))

visited = [False] * (N + M + 1)

cN = cM = cB = 0
ans = 0

for st in range(1, N + M + 1):
    if visited[st]:
        continue

    V = []
    q = st
    while True:
        V.append(q)
        visited[q] = True
        q = P[q]
        if q == st:
            break

    minV = min(V)
    maxV = max(V)

    if len(V) == 1:
        continue

    if maxV <= N:
        cN += 1
        ans += len(V)
    elif minV >= N + 1:
        cM += 1
        ans += len(V)
    else:
        cB += 1
        ans += len(V) - 1

ans += max(cN, cM) - min(cN, cM)
print(ans)
