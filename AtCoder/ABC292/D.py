from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
C = [0] * N

for _ in range(M):
    u, v = map(int, input().split())
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)
    C[u - 1] += 1
    C[v - 1] += 1

ans = "Yes"

visited = [False] * N
for st in range(N):
    if visited[st]:
        continue

    cV = cE = 0
    queue = deque([st])
    while queue:
        q = queue.popleft()
        if visited[q]:
            continue
        visited[q] = True
        cV += 1
        cE += C[q]

        for e in E[q]:
            queue.append(e)

    if cV * 2 != cE:
        ans = "No"

print(ans)
