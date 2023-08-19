from collections import deque

N, M = map(int, input().split())
L = N + M + 1
E = [[] for _ in range(L)]

for i in range(M + 1, L):
    input()
    S = map(int, input().split())
    for s in S:
        E[s].append(i)
        E[i].append(s)


INF = 1 << 60

queue = deque([1])
dist = [INF] * L
while queue:
    q = queue.popleft()
    d = q // L
    q = q % L

    if dist[q] != INF:
        continue
    dist[q] = d

    for e in E[q]:
        queue.append((d + 1) * L + e)

dM = dist[M]
ans = dM // 2 - 1 if dM < INF else -1
print(ans)
