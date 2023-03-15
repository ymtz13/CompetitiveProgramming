from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    E[u - 1].append(v - 1)

cnt = 0
for st in range(N):
    queue = deque([st])
    visited = [False] * N
    while queue:
        q = queue.popleft()
        if visited[q]:
            continue
        visited[q] = True

        for e in E[q]:
            queue.append(e)

    cnt += visited.count(True) - 1

print(cnt - M)
